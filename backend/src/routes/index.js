import { version } from "../../package.json";
import { Router } from "express";
import suburbs from "./suburbs";
import ranked_suburbs from "./ranked_suburbs";
import search from "./search";
import unis from "./unis";
import versionService from "../services/versionService";

const api = Router();

api.use("/api/suburbs", suburbs);
api.use("/api/ranked_suburbs", ranked_suburbs);
api.use("/api/university", unis);
api.use("/api/search", search);

api.get("/api", (req, res) => {
  res.json(versionService.version);
});

api.get("*", function (req, res) {
  res.redirect("/api");
});

export default api;
