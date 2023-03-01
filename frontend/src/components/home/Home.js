import React, { Component } from "react";
import { ToastContainer, toast } from "react-toastify";
import Select from "react-select";
import { browseActions } from "../../actions";
import { connect } from "react-redux";
import { HashLink } from "react-router-hash-link";
//css
import "react-select/dist/react-select.css";
import "./Home.css";
import { configs } from "../../helpers";

class Home extends Component {
  mustSubmitNotification = (text) =>
    toast(text, {
      type: toast.TYPE.INFO,
      autoClose: 5000,
      hideProgressBar: true,
      bodyClassName: "custom-toast",
    });

  constructor(props) {
    super(props);

    this.state = {};

    this.onSubmit = this.onSubmit.bind(this);
    this.getLanguages = this.getLanguages.bind(this);
    this.getUnis = this.getUnis.bind(this);
    this.clearPreferences = this.clearPreferences.bind(this);
  }

  componentDidMount = function () {
    document.title = "Sheltr | Home";

    if (
      !(
        Object.keys(this.props.preferences).length === 0 &&
        this.props.preferences.constructor === Object
      )
    ) {
      this.setState(this.props.preferences);
    }
  };

  new = true;

  handleSelectChange = function (name) {
    return function (newValue) {
      if (
        typeof newValue !== "undefined" &&
        newValue !== null &&
        name !== "actualLanguage" &&
        name !== "uni"
      ) {
        this.setState({ [name]: newValue.value });
        if (name === "language" && newValue.value === 0) {
          this.setState({ actualLanguage: null });
        }
      } else if (typeof newValue !== "undefined") {
        this.setState({ [name]: newValue, ["raw_" + name]: newValue });
      } else {
        this.setState({ [name]: "" });
      }
    }.bind(this);
  };

  onSubmit = function (e) {
    e.preventDefault();
    this.new = false;

    let params = this.state;

    if (
      Object.keys(params).length === 0 ||
      typeof params.uni === "undefined" ||
      params.uni === null
    ) {
      this.mustSubmitNotification("You must input your preferences!");
    } else {
      const { dispatch } = this.props;
      dispatch(browseActions.enterPreferences(params));
    }
  };

  clearPreferences = function (e) {
    e.preventDefault();
    this.setState({ distance: null });
    this.setState({ uni: null });
  };

  componentWillReceiveProps(nextProps) {
    if (nextProps.preferences && this.new === false) {
      this.props.history.push("/suburb");
    }
  }

  getLanguages(input) {
    if (!input) {
      if (this.state.raw_actualLanguage) {
        input = this.state.raw_actualLanguage.name;
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

  render() {
    const { uni, distance } = this.state;

    return (
      <div id="HomeComponent">
        <ToastContainer />
        <div className="header-container">
          <div className="header-content">
            <div className="header-content-inner text-xs-center">
              <h1>New students, welcome to Victoria!</h1>
              <div className="lead">
                You can start finding a great new place to live here!
              </div>

              <form onSubmit={this.onSubmit}>
                <div className="nooky">
                  <div
                    className="nooky-label-container"
                    style={{ width: "220px" }}
                  >
                    <div className="nooky-label">I plan on studying at</div>
                  </div>

                  <Select.Async
                    placeholder="..."
                    autoload={true}
                    name="uni"
                    filterOption={() => true}
                    className="react-select"
                    value={uni}
                    style={{ width: "350px" }}
                    valueKey="shim"
                    labelKey="name"
                    arrowRenderer={function () {
                      return <span></span>;
                    }}
                    onChange={this.handleSelectChange("uni")}
                    loadOptions={this.getUnis}
                    backspaceRemoves={true}
                  />
                </div>
                <div className="nooky">
                  <div
                    className="nooky-label-container"
                    style={{ width: "300px" }}
                  >
                    <div className="nooky-label">
                      and live within a distance of
                    </div>
                  </div>

                  <Select
                    className="react-select"
                    name="distance"
                    placeholder="..."
                    value={distance}
                    searchable={false}
                    arrowRenderer={function () {
                      return <span></span>;
                    }}
                    style={{ width: "150px" }}
                    onChange={this.handleSelectChange("distance")}
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

                <div className="find-suburbs-btn-container">
                  <button
                    className="btn btn-find-suburbs btn-info btn-lg"
                    type="submit"
                  >
                    {" "}
                    Find suburbs{" "}
                  </button>
                  &nbsp;
                  <button
                    className="btn btn-light btn-clear btn-lg"
                    type="button"
                    onClick={this.clearPreferences}
                  >
                    {" "}
                    <i className="fas fa-times"></i> Clear{" "}
                  </button>
                </div>
              </form>
            </div>
          </div>

          <HashLink
            className="more-info"
            smooth
            to="/#about"
            scroll={(el) =>
              el.scrollIntoView({ behavior: "smooth", block: "start" })
            }
          >
            <i className="fas fa-caret-down"></i>
          </HashLink>
        </div>
        <div id="about"></div>
        <main role="main">
          <div className="container home-container">
            <div className="row">
              <div className="col-md-4">
                <h2 className="featurette-heading">
                  What is this? <span className="text-muted"></span>
                </h2>
                <div className="lead">
                  Our goal is to impart local area knowledge on new students
                  arriving in Victoria. We aim to connect you with safe,
                  affordable, and comfortable places to live.
                </div>
                <img
                  className="featurette-image img-fluid mx-auto"
                  alt="Travelers"
                  style={{ width: 350 + "px" }}
                  src="images/airport.jpg"
                  data-holder-rendered="true"
                />
              </div>
              <div className="col-md-4">
                <h2 className="featurette-heading">How does it work?</h2>
                <div className="lead">
                  Victoria is a world leader in open data.
                </div>
                <div className="lead">
                  We've gathered, analysed, mined, and crunched a tonne of this
                  data to present our findings to you.
                </div>
                <p className="block-of-images">
                  <a
                    href="https://www.data.vic.gov.au"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img
                      alt="Victoria's open data directory"
                      src="images/data-vic.jpg"
                    />
                  </a>
                  <a
                    href="https://data.melbourne.vic.gov.au"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img
                      alt="The City of Melbourne’s open data platform"
                      src="images/data-melb.jpg"
                    />
                  </a>
                  <a
                    href="https://www.crimestatistics.vic.gov.au"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img
                      alt="Crime Statistics Agency Victoria"
                      src="images/crime-stats-vic.jpg"
                    />
                  </a>
                  <a
                    href="http://www.abs.gov.au"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img
                      alt="Australian Bureau of Statistics"
                      src="images/abs.jpg"
                    />
                  </a>
                  <a
                    href="https://www.ptv.vic.gov.au"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img alt="Public Transport Victoria" src="images/ptv.jpg" />
                  </a>
                  <a
                    href="https://www.vic.gov.au"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img alt="Victorian Government" src="images/vic.png" />
                  </a>
                  <a
                    href="https://www.australia.gov.au/about-australia/facts-and-figures/statistics"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img
                      alt="Australian Government"
                      src="images/australiangov.png"
                    />
                  </a>
                  <a
                    href="https://www.vicroads.vic.gov.au"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <img alt="Vicroads" src="images/vicroads.jpg" />
                  </a>
                </p>
              </div>
              <div className="col-md-4">
                <h2 className="featurette-heading">Who made this?</h2>
                <div className="lead">
                  We're a group at Monash University, and we're located at Floor
                  3, Building B, Monash Caulfield.
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }
}

function mapStateToProps(state) {
  const preferences = state.browse;
  return {
    preferences,
  };
}

export default connect(mapStateToProps)(Home);
