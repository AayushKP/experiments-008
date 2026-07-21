import { Router } from "express";
import { upload } from "../config/multer";
import { uploadController } from "../controllers/upload.controller";

export const uploadRouter = Router();

uploadRouter.post("/", upload.single("file"), uploadController);
