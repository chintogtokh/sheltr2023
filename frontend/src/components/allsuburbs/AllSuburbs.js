import React, { Component } from "react";
import "./AllSuburbs.css";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import Select from "react-select";
import { browseActions } from "../../actions";
import { configs } from "../../helpers";
import ReactStreetview from "react-streetview";
import Pagination from "react-js-pagination";

class AllSuburbs extends Component {
  constructor(props) {
    super(props);
    this.state = {
      suburbs: {},
      loaded: false,
      activePage: 1,
    };

    this.googleMapsApiKey = configs.googleMapsApiKey;

    this.getUnis = this.getUnis.bind(this);
    this.getLanguages = this.getLanguages.bind(this);
    this.getRankedSuburbs = this.getRankedSuburbs.bind(this);
    this.handlePageChange = this.handlePageChange.bind(this);

    this.handleSelectChange = this.handleSelectChange.bind(this);
  }

  handleSelectChange = function (value) {
    window.open("/suburb/" + value.shim);
  };

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

  handlePageChange(pageNumber) {
    console.log(`active page is ${pageNumber}`);
    this.setState({ activePage: pageNumber });
  }

  mustSubmitNotification = (text) =>
    toast(text, {
      type: toast.TYPE.INFO,
      autoClose: 5000,
      hideProgressBar: true,
      bodyClassName: "custom-toast",
    });

  componentDidMount = function () {
    document.title = "Sheltr | Suggestions";

    if (
      !(
        Object.keys(this.props.preferences).length === 0 &&
        this.props.preferences.constructor === Object
      )
    ) {
      this.setState(this.props.preferences);
    }
  };

  getLanguages(input) {
    if (!input) {
      if (this.state.raw_language) {
        input = this.state.raw_language.name;
      } else {
        return Promise.resolve({ options: [] });
      }
    }

    return fetch(configs.apiEndpoint + `/api/search/languages?q=${input}`)
      .then((response) => response.json())
      .then((json) => {
        return { options: json };
      });
  }

  getUnis(input) {
    if (!input) {
      if (this.state.raw_uni) {
        input = this.state.raw_uni.name;
      } else {
        return Promise.resolve({ options: [] });
      }
    }

    if (input.length <= 2) {
      return Promise.resolve({ options: [] });
    }

    return fetch(configs.apiEndpoint + `/api/search/universities?q=${input}`)
      .then((response) => response.json())
      .then((json) => {
        return { options: json };
      });
  }

  getWiki = function (name, count) {
    fetch(
      "https://en.wikipedia.org/api/rest_v1/page/summary/" + name + ", Victoria"
    )
      .then((response) =>
        response.json().then((data) => ({
          data: data,
          status: response.status,
        }))
      )
      .then((response) => {
        if (response.status === 200) {
          return response.data.extract;
        }
      });
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

  componentWillMount() {
    let { preferences } = this.props;

    let params = JSON.parse(JSON.stringify(preferences));

    // delete params.raw_uni;
    // delete params.raw_language;

    if (params.uni && params.uni.shim) {
      let tmp = params.uni.shim;
      delete params.uni;
      params.uni = tmp;
    }

    if (params.language && params.language.shim) {
      let tmp = params.language.shim;
      delete params.language;
      params.language = tmp;
    }

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
        .then((response) => {
          this.setState({
            streetViewPanoramaOptions: {
              addressControl: false,
              motionTracking: false,
              motionTrackingControl: false,
              disableDefaultUI: true,
              showRoadLabels: false,
              position: {
                lat: response.data.coords.lat,
                lng: response.data.coords.lng,
              },
              pov: { heading: 100, pitch: 0 },
              zoom: 1,
            },
          });
        });
    }

    this.getRankedSuburbs(params);
  }

  getRankedSuburbs = function (params) {
    this.setState({ activePage: 1 });

    if (!(params.uni && params.distance)) {
      this.mustSubmitNotification(
        "You must enter a university and distance first."
      );
      this.setState({ invalidPreferences: true });
    } else {
      this.setState({ invalidPreferences: false });
    }

    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(params),
    };

    if (
      params.filter === "language" &&
      (params.language === null || typeof params.language === "undefined")
    ) {
      return;
    }

    this.setState({ loaded: false });

    fetch(configs.apiEndpoint + "/api/ranked_suburbs", requestOptions)
      .then((response) =>
        response.json().then((data) => ({
          data: data,
          status: response.status,
        }))
      )
      .then((response) => {
        // setTimeout(function() { this.setState({loaded: true}); }.bind(this), 1000);
        this.setState({ loaded: true });
        if (response.status !== 200) {
          this.mustSubmitNotification("Could not fetch suburbs");
        } else {
          this.setState({ itemsCount: response.data.length });

          this.setState({ suburb: {} });

          for (let i = 0; i < response.data.length; i++) {
            let shel = response.data[i];

            fetch(
              "https://maps.googleapis.com/maps/api/streetview/metadata?location=" +
                shel.coords.lat +
                "," +
                shel.coords.lng +
                "&key=" +
                this.googleMapsApiKey
            )
              .then((metaResponse) =>
                metaResponse.json().then((data) => ({
                  data: data,
                  status: metaResponse.status,
                }))
              )
              .then((metaResponse) => {
                var imageURL = "";
                if (metaResponse.data.status !== "OK") {
                  imageURL = "images/noimage.png";
                } else {
                  imageURL =
                    "http://maps.googleapis.com/maps/api/streetview?size=640x480&location=" +
                    shel.coords.lat +
                    "," +
                    shel.coords.lng +
                    "&pitch=0&sensor=false&key=" +
                    this.googleMapsApiKey;
                }

                this.setState({
                  suburb: {
                    ...this.state.suburb,
                    [i]: (
                      <Link to={"/suburb/" + shel.shim} className="suburb-link">
                        <div className="card mb-4 box-shadow h-md-250">
                          <img
                            className="card-img-top"
                            src={imageURL}
                            alt={shel.name}
                          />
                          <div className="card-body">
                            <h3 className="mb-0">{shel.name}</h3>
                            <div className="card-text">
                              <div className="star-label"> Safety </div>
                              <div className="star-ratings">
                                {this.numberToStar(shel.rating_safety)}
                              </div>
                              <br />
                              <div className="star-label">Affordability</div>
                              <div className="star-ratings">
                                {this.numberToStar(shel.rating_affordability)}
                              </div>
                              <br />
                              {params.uni && (
                                <div>
                                  <div className="star-label">Distance</div>
                                  <div className="star-ratings">
                                    {shel.university_distances[
                                      params.uni
                                    ].number.toFixed(2) + " km"}
                                  </div>
                                </div>
                              )}
                              {params.language &&
                                params.filter === "language" && (
                                  <div>
                                    <div className="star-label">
                                      Language (
                                      {params.language
                                        .split("-")
                                        .join(" ")
                                        .replace(/\b\w/g, (l) =>
                                          l.toUpperCase()
                                        )}
                                      )
                                    </div>
                                    <div className="star-ratings">
                                      {this.numberToStar(
                                        shel.language[params.language]
                                      )}
                                    </div>
                                  </div>
                                )}
                            </div>
                          </div>
                        </div>
                      </Link>
                    ),
                  },
                });
              });
          }
        }
      });
  };

  handleFilterChange = function (name) {
    return function (newValue) {
      var getRankedSubs = () => {
        var params = {
          distance: this.state.distance,
          language: this.state.language ? this.state.language.shim : null,
          uni: this.state.uni ? this.state.uni.shim : null,
          filter: this.state.filter,
        };
        const { dispatch } = this.props;

        var preferences = {
          distance: this.state.distance,
          raw_language: this.state.raw_language,
          raw_uni: this.state.raw_uni,
          language: this.state.raw_language,
          uni: this.state.raw_uni,
          filter: this.state.filter,
        };

        if (this.state.filter === "language") {
          if (this.state.raw_language) {
            dispatch(browseActions.enterPreferences(preferences));
          }
        } else {
          dispatch(browseActions.enterPreferences(preferences));
        }

        this.getRankedSuburbs(params);
      };

      if (
        typeof newValue !== "undefined" &&
        newValue !== null &&
        name !== "language" &&
        name !== "uni"
      ) {
        this.setState({ [name]: newValue.value }, getRankedSubs);
      } else if (typeof newValue !== "undefined") {
        this.setState(
          { [name]: newValue, ["raw_" + name]: newValue },
          getRankedSubs
        );
      } else {
        this.setState({ [name]: "" }, getRankedSubs);
      }
    }.bind(this);
  };

  render() {
    const { uni, distance, filter, language, selected_suburb } = this.state;

    return (
      <div id="AllSuburbsComponent">
        <ToastContainer />
        <main role="main">
          {this.state.suburb && this.state.streetViewPanoramaOptions && (
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
                <li className="breadcrumb-item active" aria-current="page">
                  Suburb Suggestions
                </li>
              </ol>
            </nav>

            <div className="row">
              <div className="col-md-8">
                <h1>Suburb Suggestions</h1>
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

            <div>
              The following suburbs might fit your needs. Start drilling down
              using the filters!
            </div>

            <div className="sortable-section-container">
              <div className="sortable-section">
                <div className="filter-text-container">
                  <div className="filter-text">University</div>
                </div>
                <Select.Async
                  placeholder="Select..."
                  autoload={true}
                  name="uni"
                  filterOption={() => true}
                  className="react-select"
                  value={uni}
                  style={{ width: "200px" }}
                  valueKey="shim"
                  labelKey="name"
                  onChange={this.handleFilterChange("uni")}
                  loadOptions={this.getUnis}
                  backspaceRemoves={true}
                />
              </div>

              <div className="sortable-section">
                <div className="filter-text-container">
                  <div className="filter-text">Distance:</div>
                </div>
                <Select
                  className="react-select"
                  name="distance"
                  placeholder={distance}
                  value={distance}
                  searchable={false}
                  style={{ width: "150px" }}
                  onChange={this.handleFilterChange("distance")}
                  options={[
                    { value: "2", label: "2km" },
                    { value: "5", label: "5km" },
                    { value: "10", label: "10km" },
                    { value: "20", label: "20km" },
                    { value: "50", label: "50km" },
                    { value: "100", label: "100km" },
                  ]}
                />
              </div>

              <div className="sortable-section">
                <div className="filter-text-container">
                  <div className="filter-text">Filter by:</div>
                </div>
                <Select
                  className="react-select"
                  name="filter"
                  placeholder="distance"
                  value={filter}
                  searchable={false}
                  style={{ width: "150px" }}
                  onChange={this.handleFilterChange("filter")}
                  options={[
                    { value: "safety", label: "safety" },
                    { value: "affordability", label: "affordability" },
                    { value: "distance", label: "distance" },
                    { value: "language", label: "language" },
                  ]}
                />
              </div>

              {filter === "language" && (
                <div className="sortable-section">
                  <div className="filter-text-container">
                    <div className="filter-text">Language:</div>
                  </div>
                  <Select.Async
                    placeholder=""
                    autoload={true}
                    name="language"
                    filterOption={() => true}
                    className="react-select"
                    value={language}
                    style={{ width: "150px" }}
                    valueKey="shim"
                    labelKey="name"
                    onChange={this.handleFilterChange("language")}
                    loadOptions={this.getLanguages}
                    backspaceRemoves={true}
                  />
                </div>
              )}
            </div>

            {!this.state.loaded && (
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

            {this.state.loaded && this.state.suburb && (
              <div>
                <div className="row">
                  {[...Array(8)].map((e, i) => {
                    return (
                      <div
                        key={i + (this.state.activePage - 1) * 8}
                        className="col-md-3"
                      >
                        {this.state.suburb[i + (this.state.activePage - 1) * 8]}
                      </div>
                    );
                  })}
                </div>

                {this.state.itemsCount === 0 &&
                  this.state.uni &&
                  this.state.distance && (
                    <div className="row">
                      <div
                        className="col-md-12"
                        style={{ textAlign: "center" }}
                      >
                        <h1>no suburbs matching that criteria :(</h1>
                      </div>
                    </div>
                  )}

                {this.state.invalidPreferences && (
                  <div>
                    <div className="row">
                      <div
                        className="col-md-12"
                        style={{ textAlign: "center" }}
                      >
                        <h1>invalid preferences entered :(</h1>
                        <h3>you must enter both a university and distance</h3>
                      </div>
                    </div>
                  </div>
                )}

                {this.state.itemsCount !== 0 && (
                  <Pagination
                    activePage={this.state.activePage}
                    prevPageText="prev"
                    nextPageText="next"
                    itemsCountPerPage={8}
                    totalItemsCount={this.state.itemsCount}
                    pageRangeDisplayed={Math.floor(this.state.itemsCount / 8)}
                    onChange={this.handlePageChange}
                    itemClass="page-item"
                    linkClass="page-link"
                  />
                )}
              </div>
            )}
          </div>
        </main>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  preferences: state.browse,
});

export default connect(mapStateToProps)(AllSuburbs);
