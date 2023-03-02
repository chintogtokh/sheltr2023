import path from "path";

let config = {};

config.logFileDir = path.join(__dirname, "../../log");
config.logFileName = "app.log";
config.serverPort = 4000;
config.bodyLimit = "100kb";
config.corsHeaders = ["Link"];
// config.jwtSecret = process.env.MONGO_JWTSECRET;

export default config;
