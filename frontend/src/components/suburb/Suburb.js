import React, { Component } from "react";
import "./Suburb.css";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { suburbActions } from "../../actions";
import Leaflet from "leaflet";
import { Map, TileLayer, GeoJSON, Marker, Popup } from "react-leaflet";
import bbox from "turf-bbox";
import { configs } from "../../helpers";
import Select from "react-select";
import ReactStreetview from "react-streetview";
import uniimage from "../../files/uni.png";

class Suburb extends Component {
  constructor(props) {
    super(props);

    this.googleMapsApiKey = configs.googleMapsApiKey;

    this.state = {
      suburb: null,
    };

    this.handleSelectChange = this.handleSelectChange.bind(this);
    this.loaded = false;

    this.markerImage = new Leaflet.Icon({
      iconUrl: uniimage,
      iconSize: [60, 60], // size of the icon
      shadowSize: [64, 64], // size of the shadow
      iconAnchor: [60, 60], // point of the icon which will correspond to marker's location
      shadowAnchor: [4, 62], // the same for the shadow
      popupAnchor: [-3, -76], // point from which the popup should open relative to the iconAnchor
    });
  }

  getStatFromArray(arr, desc) {
    return arr[desc];
  }

  componentWillMount() {
    let suburb_shim = this.props.match.params.name;

    fetch(configs.apiEndpoint + "/api/suburbs/" + suburb_shim)
      .then((response) =>
        response.json().then((data) => ({
          data: data,
          status: response.status,
        }))
      )
      .then((response) => {
        this.loaded = true;

        if (this.props.preferences.raw_uni) {
          fetch(
            configs.apiEndpoint +
              "/api/university/" +
              this.props.preferences.raw_uni.shim
          )
            .then((response) =>
              response.json().then((data) => ({
                data: data,
                status: response.status,
              }))
            )
            .then((uniResponse) => {
              if (uniResponse.status !== 200) {
                // window.location = "/404";
              } else {
                let bboxArray; // = bbox(suburb.geojson);
                let corner1; // = [bboxArray[1], bboxArray[0]];
                let corner2; // = [bboxArray[3], bboxArray[2]];
                let bounds; // = [corner1, corner2];

                var tempjson = JSON.parse(
                  JSON.stringify(response.data.geojson)
                );

                tempjson.geometry.coordinates[0][0].push([
                  uniResponse.data.coords.lng,
                  uniResponse.data.coords.lat,
                ]);

                bboxArray = bbox(tempjson);

                corner1 = [bboxArray[1], bboxArray[0]];
                corner2 = [bboxArray[3], bboxArray[2]];
                bounds = [corner1, corner2];

                this.setState({ suburb: response.data, bounds: bounds });

                document.title = "Sheltr | " + this.state.suburb.name;

                const { dispatch } = this.props;
                dispatch(suburbActions.fetchSuburbWiki(this.state.suburb.name));

                this.setState({
                  streetViewPanoramaOptions: {
                    addressControl: false,
                    disableDefaultUI: true,
                    motionTracking: false,
                    motionTrackingControl: false,
                    showRoadLabels: false,
                    position: {
                      lat: response.data.coords.lat,
                      lng: response.data.coords.lng,
                    },
                    pov: { heading: 100, pitch: 0 },
                    zoom: 1,
                  },
                });
              }

              this.setState({ uni_coords: uniResponse.data.coords });
            });
        } else {
          let bboxArray; // = bbox(suburb.geojson);
          let corner1; // = [bboxArray[1], bboxArray[0]];
          let corner2; // = [bboxArray[3], bboxArray[2]];
          let bounds; // = [corner1, corner2];

          var tempjson = JSON.parse(JSON.stringify(response.data.geojson));

          bboxArray = bbox(tempjson);

          corner1 = [bboxArray[1], bboxArray[0]];
          corner2 = [bboxArray[3], bboxArray[2]];
          bounds = [corner1, corner2];

          this.setState({ suburb: response.data, bounds: bounds });

          document.title = "Sheltr | " + this.state.suburb.name;

          const { dispatch } = this.props;
          dispatch(suburbActions.fetchSuburbWiki(this.state.suburb.name));
        }
      });
  }

  getStyle(feature, layer) {
    return {
      color: "#112660",
      weight: 5,
      opacity: 0.65,
    };
  }

  getSuburbs(input) {
    if (!input) {
      return Promise.resolve({ options: [] });
    }

    return fetch(configs.apiEndpoint + `/api/search/suburbs?q=${input}`)
      .then((response) => response.json())
      .then((json) => {
        return { options: json };
      });
  }

  handleSelectChange = function (value) {
    window.open("/suburb/" + value.shim);
  };

  numberToRanking = (num) => {
    let tmp = {
      10: "high priority",
      7: "moderate priority",
      4: "neutral",
      1: "low priority",
      0: "not a priority",
    };
    return tmp[num.toString()];
  };

  numberToStar = function (number) {
    var ret = [];

    var rating = Math.floor(number / 10);

    var i = 0;
    for (i = 0; i < Math.floor(rating / 2); i++) {
      ret.push(<i key={i} className="fas fa-star"></i>);
    }
    if (rating % 2 !== 0) {
      ret.push(<i key={i} className="fas fa-star"></i>);
    }

    return [
      <span key={1} className="empty">
        <i className="far fa-star"></i>
        <i className="far fa-star"></i>
        <i className="far fa-star"></i>
        <i className="far fa-star"></i>
        <i className="far fa-star"></i>
      </span>,
      <span key={2} className="actual">
        {ret}
      </span>,
    ];
  };

  render() {
    var { wiki, selected_suburb, preferences } = this.props;

    if (wiki) {
      var ret = "";
      var wikiNew = wiki.replace(/([.?!])\s*(?=[A-Z])/g, "$1|").split("|");
      for (var i = 0; i < wikiNew.length; i++) {
        if (wikiNew[i].toLowerCase().indexOf("population") === -1) {
          ret += wikiNew[i] + " ";
        }
      }
      wiki = ret;
    }

    return (
      <div id="SuburbComponent">
        <main role="main">
          {!this.loaded && (
            <div className="container">
              <div className="row">
                <div className="col-md-12" style={{ textAlign: "center" }}>
                  <h1>
                    loading data <i className="fas fa-spinner fa-spin"></i>
                  </h1>
                </div>
              </div>
            </div>
          )}
          {this.state.suburb && (
            <div>
              {this.state.streetViewPanoramaOptions && (
                <div>
                  <div className="streetview-container">
                    <div
                      style={{
                        width: "100%",
                        height: "100%",
                        backgroundColor: "white",
                      }}
                    >
                      <ReactStreetview
                        apiKey={this.googleMapsApiKey}
                        streetViewPanoramaOptions={
                          this.state.streetViewPanoramaOptions
                        }
                      />
                    </div>
                  </div>
                  <div className="streetview-container-after"></div>
                </div>
              )}

              <div className="container">
                <nav aria-label="breadcrumb">
                  <ol className="breadcrumb">
                    {this.props.history.length > 1 && (
                      <li className="breadcrumb-item">
                        <a onClick={this.props.history.goBack}>
                          <i className="fas fa-chevron-circle-left"></i>
                        </a>
                      </li>
                    )}
                    <li className="breadcrumb-item">
                      <Link to="/">Home</Link>
                    </li>
                    <li className="breadcrumb-item">
                      <Link to="/suburb">Suburb Suggestions</Link>
                    </li>
                    <li className="breadcrumb-item active" aria-current="page">
                      {this.state.suburb.name}
                    </li>
                  </ol>
                </nav>

                <div className="row">
                  <div className="col-md-8">
                    <h1>{this.state.suburb.name}</h1>
                  </div>

                  <div className="col-md-4">
                    <Select.Async
                      placeholder="search for another suburb?"
                      name="selected_suburb"
                      autoload={true}
                      className="react-select-single-suburb"
                      value={selected_suburb}
                      valueKey="shim"
                      labelKey="name"
                      onChange={this.handleSelectChange}
                      loadOptions={this.getSuburbs}
                      backspaceRemoves={true}
                    />
                  </div>
                </div>

                <div className="row">
                  <div className="col-md-8">
                    <p>
                      {wiki}
                      {wiki && (
                        <a
                          className="wiki-link"
                          href={
                            "https://en.wikipedia.org/wiki/" +
                            this.state.suburb.name +
                            ", Victoria"
                          }
                        >
                          <i>(data automatically extracted from Wikipedia)</i>
                        </a>
                      )}
                    </p>

                    <h3>Main indicators</h3>
                    <ul className="rating-list">
                      <li>
                        {" "}
                        <div className="star-label">Safety rating</div>
                        <div className="star-ratings">
                          {this.numberToStar(this.state.suburb.rating_safety)}
                        </div>{" "}
                      </li>

                      <li>
                        {" "}
                        <div className="star-label">Affordability rating</div>
                        <div className="star-ratings">
                          {this.numberToStar(
                            this.state.suburb.rating_affordability
                          )}
                        </div>
                      </li>

                      {preferences.filter === "language" &&
                        preferences.language &&
                        preferences.language !== 0 && (
                          <li>
                            <div className="star-label">
                              International student language rating for{" "}
                              {preferences.raw_language.name}
                            </div>
                            <div className="star-ratings">
                              {this.numberToStar(
                                this.state.suburb.language[
                                  preferences.raw_language.shim
                                ]
                              )}
                            </div>
                          </li>
                        )}

                      {preferences.raw_uni && (
                        <li>
                          <div className="star-label">
                            Distance from {preferences.raw_uni.name}{" "}
                          </div>
                          <div className="star-ratings">
                            {this.state.suburb.university_distances[
                              preferences.raw_uni.shim
                            ].number.toFixed(2) + " km"}
                          </div>
                        </li>
                      )}
                    </ul>

                    <br />

                    <h3>
                      Statistics (
                      {
                        this.getStatFromArray(
                          this.state.suburb.stats,
                          "suburb-residents"
                        ).year
                      }
                      )
                    </h3>

                    <div className="stats-section">
                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/team.svg"
                            alt="Population"
                            height="50"
                            width="50"
                          />
                          <h4> Population </h4>
                        </div>
                        <div className="col-md-4">
                          {
                            this.getStatFromArray(
                              this.state.suburb.stats,
                              "suburb-residents"
                            ).number
                          }
                        </div>
                      </div>

                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/graduated.svg"
                            alt="International student population"
                            height="50"
                            width="50"
                          />
                          <h4> International student population </h4>
                        </div>
                        <div className="col-md-4">
                          {
                            this.getStatFromArray(
                              this.state.suburb.stats,
                              "total-int-students-per-suburb"
                            ).number
                          }
                          &nbsp; (
                          {(
                            (this.getStatFromArray(
                              this.state.suburb.stats,
                              "total-int-students-per-suburb"
                            ).number /
                              this.getStatFromArray(
                                this.state.suburb.stats,
                                "suburb-residents"
                              ).number) *
                            100
                          ).toFixed(2)}{" "}
                          %)
                        </div>
                      </div>

                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/prisoner.svg"
                            alt="Crime per 10000 population"
                            height="50"
                            width="50"
                          />
                          <h4> Number of offences per 10,000 residents</h4>
                        </div>
                        <div className="col-md-4">
                          {this.getStatFromArray(
                            this.state.suburb.stats,
                            "offences-per-10000"
                          ).number.toFixed(2)}
                        </div>
                      </div>

                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/money.svg"
                            alt="Average rental range"
                            height="50"
                            width="50"
                          />
                          <h4> Most common rental price range </h4>
                        </div>
                        <div className="col-md-4">
                          {
                            this.getStatFromArray(
                              this.state.suburb.stats,
                              "suburb-most-common-expense-tier"
                            ).number
                          }
                        </div>
                      </div>

                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/planet-earth.svg"
                            alt="Most popular language"
                            height="50"
                            width="50"
                          />
                          <h4> Most popular international student language </h4>
                        </div>
                        <div className="col-md-4">
                          {
                            this.getStatFromArray(
                              this.state.suburb.stats,
                              "suburb-most-int-student-lang"
                            ).number
                          }
                        </div>
                      </div>

                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/athletics.svg"
                            alt="public transport"
                            height="50"
                            width="50"
                          />
                          <h4> Popular modes of transport </h4>
                        </div>
                        <div className="col-md-4">
                          {this.getStatFromArray(
                            this.state.suburb.stats,
                            "train-station-flag"
                          ).number ? (
                            <img
                              className="stat-image"
                              src="/otherimages/train.svg"
                              alt="Train"
                              title="Train"
                              height="50"
                              width="50"
                            />
                          ) : (
                            ""
                          )}
                          {this.getStatFromArray(
                            this.state.suburb.stats,
                            "tram-line-flag"
                          ).number ? (
                            <img
                              className="stat-image"
                              src="/otherimages/tram.svg"
                              alt="Tram"
                              title="Tram"
                              height="50"
                              width="50"
                            />
                          ) : (
                            ""
                          )}
                          {this.getStatFromArray(
                            this.state.suburb.stats,
                            "bus-line-flag"
                          ).number ? (
                            <img
                              className="stat-image"
                              src="/otherimages/school-bus.svg"
                              alt="Bus"
                              title="Bus"
                              height="50"
                              width="50"
                            />
                          ) : (
                            ""
                          )}
                          {this.getStatFromArray(
                            this.state.suburb.stats,
                            "ferry-flag"
                          ).number ? (
                            <img
                              className="stat-image"
                              src="/otherimages/ferry.svg"
                              alt="Ferry"
                              title="Ferry"
                              height="50"
                              width="50"
                            />
                          ) : (
                            ""
                          )}

                          {!this.getStatFromArray(
                            this.state.suburb.stats,
                            "ferry-flag"
                          ).number &&
                          !this.getStatFromArray(
                            this.state.suburb.stats,
                            "tram-line-flag"
                          ).number &&
                          !this.getStatFromArray(
                            this.state.suburb.stats,
                            "bus-line-flag"
                          ).number &&
                          !this.getStatFromArray(
                            this.state.suburb.stats,
                            "train-station-flag"
                          ).number ? (
                            <img
                              className="stat-image"
                              src="/otherimages/no.svg"
                              alt="None"
                              title="None"
                              height="50"
                              width="50"
                            />
                          ) : (
                            ""
                          )}
                        </div>
                      </div>

                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/hospital.svg"
                            alt="Hospital"
                            height="50"
                            width="50"
                          />
                          <h4> Medical Facilities </h4>
                        </div>
                        <div className="col-md-4">
                          {this.getStatFromArray(
                            this.state.suburb.stats,
                            "aged-care-residential-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "allied-health-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "ambulance-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "chiropractic-and-osteopathic-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "dental-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "general-practice-medical-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "hospitals"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "medical-and-other-health-care-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "medical-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "no-medical-facilities-in-the-area"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "optometry-and-optical-dispensing"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "other-allied-health-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "other-residential-care-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "pathology-and-diagnostic-imaging-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "physiotherapy-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "residential-care-services"
                          ).number ||
                          this.getStatFromArray(
                            this.state.suburb.stats,
                            "specialist-medical-services"
                          ).number ? (
                            <img
                              className="stat-image"
                              title="Available"
                              src="/otherimages/yes.svg"
                              alt="yes"
                              height="50"
                              width="50"
                            />
                          ) : (
                            <img
                              className="stat-image"
                              title="None"
                              src="/otherimages/no.svg"
                              alt="yes"
                              height="50"
                              width="50"
                            />
                          )}
                        </div>
                      </div>

                      <div className="row">
                        <div className="col-md-6">
                          <img
                            className="stat-image"
                            src="/otherimages/police.svg"
                            alt="police"
                            height="50"
                            width="50"
                          />
                          <h4> Police Stations </h4>
                        </div>
                        <div className="col-md-4">
                          {this.getStatFromArray(
                            this.state.suburb.stats,
                            "suburb-police-station-flag"
                          ).number ? (
                            <img
                              className="stat-image"
                              src="/otherimages/yes.svg"
                              title="Available"
                              alt="yes"
                              height="50"
                              width="50"
                            />
                          ) : (
                            <img
                              title="None"
                              className="stat-image"
                              src="/otherimages/no.svg"
                              alt="yes"
                              height="50"
                              width="50"
                            />
                          )}
                        </div>
                      </div>
                    </div>

                    <br />

                    <h3>Search for properties</h3>
                    <div className="realestate-section">
                      <i>
                        Disclaimer: The following are external sites and not
                        affiliated with us in any way.
                      </i>
                      <br />
                      <br />
                      <button className="btn btn-light">
                        <a
                          target="_blank"
                          href={
                            "https://www.domain.com.au/rent/?terms=" +
                            this.state.suburb.name.toLowerCase() +
                            " vic"
                          }
                        >
                          <img
                            alt="Domain.com.au"
                            style={{ height: "25px" }}
                            src="/externallogos/domain.png"
                          />
                        </a>
                        &nbsp;
                        <i className="fas fa-external-link-alt"></i>
                      </button>
                      <button className="btn btn-light">
                        <a
                          target="_blank"
                          href={
                            "https://www.realestate.com.au/rent/in-" +
                            this.state.suburb.name.toLowerCase() +
                            ",+vic/list-1"
                          }
                        >
                          <img
                            alt="Realestate.com.au"
                            style={{ height: "40px" }}
                            src="/externallogos/realestate.png"
                          />
                        </a>
                        &nbsp;
                        <i className="fas fa-external-link-alt"></i>
                      </button>
                    </div>
                    <br />
                  </div>
                  <div className="col-md-4">
                    {this.state.suburb && (
                      <Map
                        style={{ height: 500 + "px", width: 100 + "%" }}
                        bounds={this.state.bounds}
                      >
                        <TileLayer
                          attribution='&amp;copy <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />
                        <GeoJSON
                          key={this.state.suburb.shim}
                          data={this.state.suburb.geojson}
                          style={this.getStyle}
                        />
                        {this.state.uni_coords && (
                          <Marker
                            position={this.state.uni_coords}
                            icon={this.markerImage}
                          >
                            <Popup>
                              <span>{preferences.raw_uni.name}</span>
                            </Popup>
                          </Marker>
                        )}
                      </Map>
                    )}
                  </div>
                </div>
              </div>
            </div>
          )}
        </main>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  preferences: state.browse,
  wiki: state.suburb.wiki_extract,
});

// export default connect(mapStateToProps)(Suburb);

export default connect(mapStateToProps)(Suburb);
