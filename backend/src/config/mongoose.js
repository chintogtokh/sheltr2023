import mongoose from "mongoose";

const setupMongoose = () => {
  const dbHost = process.env.MONGO_DBHOST;
  const dbPort = process.env.MONGO_DBPORT;
  const dbUser = process.env.MONGO_DBUSER;
  const dbPass = encodeURIComponent(process.env.MONGO_DBPASS);

  mongoose.Promise = global.Promise;
  mongoose.set("debug", true);

  var uri = `mongodb://${dbUser}:${dbPass}@${dbHost}:${dbPort}`;
  console.log(uri);
  mongoose.connect(uri);
};

export default setupMongoose;
