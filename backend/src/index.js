import express from "express";
import routes from "./routes";
import config from "./config/config.dev";
import mongoose from "mongoose";
import bodyParser from "body-parser";
import cors from "cors";
import { clientErrorHandler, errorHandler } from "./middleware";

const app = express();
const port = 4000;

let dbHost = config.dbHost;
let dbPort = config.dbPort;
let dbName = config.dbName;
let dbUser = config.dbUser;
let dbPass = encodeURIComponent(config.dbPass);

// mongoose.Promise = global.Promise;

mongoose.Promise = global.Promise;
mongoose.set("debug", true);

var uri = `mongodb://${dbUser}:${dbPass}@${dbHost}:${dbPort}/${dbName}`;
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
