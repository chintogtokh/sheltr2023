import searchService from "../services/searchService";

const universitiesController = async (req, res) => {
  let searchText = req.query.q;
  const values = await searchService.searchUniversities(searchText);
  res.send(values);
};

const languagesController = async (req, res) => {
  let searchText = req.query.q;
  const values = await searchService.searchLanguages(searchText);
  res.send(values);
};

const suburbsController = async (req, res) => {
  let searchText = req.query.q;
  const values = await searchService.searchSuburbs(searchText);
  res.send(values);
};

export default {
  universitiesController,
  languagesController,
  suburbsController,
};
