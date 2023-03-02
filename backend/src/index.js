import * as dotenv from "dotenv";
dotenv.config();

import express from "express";
import routes from "./routes";
import config from "./config/config.dev";
import mongoose from "mongoose";
import bodyParser from "body-parser";
import cors from "cors";
import { clientErrorHandler, errorHandler } from "./middleware";

const app = express();
const port = 4000;

const dbHost = process.env.MONGO_DBHOST;
const dbPort = process.env.MONGO_DBPORT;
const dbName = process.env.MONGO_DBNAME;
const dbUser = process.env.MONGO_DBUSER;
const dbPass = encodeURIComponent(process.env.MONGO_DBPASS);

// mongoose.Promise = global.Promise;

mongoose.Promise = global.Promise;
mongoose.set("debug", true);

var uri = `mongodb://${dbUser}:${dbPass}@${dbHost}:${dbPort}`;
console.log(uri);
mongoose.connect(uri);

app.use(
  cors({
    exposedHeaders: config.corsHeaders,
  })
);

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

//routing
app.use(routes);

//error handling middleware
// app.use(clientErrorHandler)
app.use(errorHandler);

app.listen(port);

console.log(`Server started on: ${port}`);
