import { uploadService } from "../services/upload.service";
import { Request, Response } from "express";

export const uploadController = (req: Request, res: Response) => {
  if (!req.file) {
    return res.status(400).json({
      message: "No file received",
    });
  }

  const fileData = uploadService(req.file);

  return res.status(201).json({
    message: "File Uploaded Successfully",
    data: fileData,
  });
};
