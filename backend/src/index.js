import * as dotenv from "dotenv";
dotenv.config();

import express from "express";
import routes from "./routes";
import config from "./config/config.dev";
import bodyParser from "body-parser";
import cors from "cors";
import { errorHandler } from "./middleware";
import * as Sentry from "@sentry/node";
import setupMongoose from "./config/mongoose";

Sentry.init({
  dsn: "https://0c029a548a484c63954f713a930a1fa6@o4504767695814656.ingest.sentry.io/4504767696994304",
  tracesSampleRate: 1.0,
});

const app = express();
const port = 4000;

setupMongoose();

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
app.use(errorHandler);

app.listen(port);

console.log(`Server started on: ${port}`);
