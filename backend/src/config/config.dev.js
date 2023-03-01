import path from "path";

let config = {};

config.logFileDir = path.join(__dirname, "../../log");
config.logFileName = "app.log";
config.dbHost = "db";
config.dbPort = "27017";
config.dbName = "sheltr";
config.dbUser = "sheltr";
config.dbPass = "sheltr";
config.serverPort = 4000;
config.bodyLimit = "100kb";
config.corsHeaders = ["Link"];
config.jwtSecret = "dummysecret";

export default config;
