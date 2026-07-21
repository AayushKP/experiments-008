import { Request, Response } from "express";
import { uploadService } from "../services/upload.service";

export const uploadController = async (req: Request, res: Response) => {
  if (!req.file) {
    return res.status(400).json({
      message: "No file received",
    });
  }

  const data = await uploadService(req.file);

  return res.status(201).json({
    message: "File uploaded successfully",
    data,
  });
};
