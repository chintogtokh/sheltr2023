import path from "path";

let config = {};

config.logFileDir = path.join(__dirname, "../../log");
config.logFileName = "app.log";
config.dbHost = process.env.MONGO_DBHOST;
config.dbPort = process.env.MONGO_DBPORT;
config.dbName = process.env.MONGO_DBNAME;
config.dbUser = process.env.MONGO_DBUSER;
config.dbPass = process.env.MONGO_DBPASS;
config.serverPort = 4000;
config.bodyLimit = "100kb";
config.corsHeaders = ["Link"];
config.jwtSecret = process.env.MONGO_JWTSECRET;

export default config;
