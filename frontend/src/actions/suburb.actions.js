import { suburbConstants } from "../constants";
import { configs } from "../helpers";

export const suburbActions = {
  fetchSuburb,
  fetchSuburbWiki,
};

function fetchSuburb(suburb_shim) {
  return (dispatch) => {
    fetch(configs.apiEndpoint + "/api/suburbs/" + suburb_shim)
      .then((response) =>
        response.json().then((data) => ({
          data: data,
          status: response.status,
        }))
      )
      .then((response) => {
        if (response.status !== 200) {
          dispatch({
            type: suburbConstants.SUBURB_NOTFOUND,
          });
        } else {
          dispatch({
            type: suburbConstants.FETCH_SUBURB,
            payload: response.data,
          });
        }
      });
  };
}

function fetchSuburbWiki(suburb_name) {
  var url =
    "https://en.wikipedia.org/api/rest_v1/page/summary/" +
    suburb_name +
    ", Victoria";
  return (dispatch) => {
    fetch(url)
      .then((response) =>
        response.json().then((data) => ({
          data: data,
          status: response.status,
        }))
      )
      .then((response) => {
        if (response.status !== 200) {
          dispatch({
            type: suburbConstants.SUBURB_WIKI_NOTFOUND,
          });
        } else {
          dispatch({
            type: suburbConstants.FETCH_SUBURB_WIKI,
            payload: response.data,
          });
        }
      });
  };
}
