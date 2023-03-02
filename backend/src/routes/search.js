import { Router } from "express";
import searchControllers from "../controllers/searchControllers";

const searchRouter = Router()
  .get("/universities", searchControllers.universitiesController)
  .get("/languages", searchControllers.languagesController)
  .get("/suburbs", searchControllers.suburbsController);

export default searchRouter;
