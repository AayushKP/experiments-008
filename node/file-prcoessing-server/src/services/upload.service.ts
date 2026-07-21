import { Express } from "express";
import { processTextFile } from "../processors/text.processor";

export const uploadService = async (file: Express.Multer.File) => {
  const stats = await processTextFile(file.path);

  return {
    filename: file.filename,
    originalName: file.originalname,
    mimeType: file.mimetype,
    size: file.size,
    uploadedAt: new Date(),
    ...stats,
  };
};
