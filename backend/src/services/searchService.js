import universityModel from "../models/universities";
import suburbModel from "../models/suburbs";
import languageModel from "../models/languages";

const searchUniversities = async (searchText = "") => {
  var srches = searchText.split(" ");

  var query = [];

  for (var i = 0; i < srches.length; i++) {
    query.push({ name: { $regex: srches[i], $options: "i" } });
  }

  return await universityModel.find({ $and: query }).limit(10).exec();
};

const searchSuburbs = async (searchText = "") => {
  var srches = searchText.split(" ");

  var query = [];

  for (var i = 0; i < srches.length; i++) {
    query.push({ name: { $regex: srches[i], $options: "i" } });
  }

  return await suburbModel.find({ $and: query }).limit(10).exec();
};

const searchLanguages = async (searchText = "") => {
  var srches = searchText.split(" ");

  var query = [];

  for (var i = 0; i < srches.length; i++) {
    query.push({ name: { $regex: srches[i], $options: "i" } });
  }

  return await languageModel.find({ $and: query }).limit(10).exec();
};

export default { searchUniversities, searchSuburbs, searchLanguages };
