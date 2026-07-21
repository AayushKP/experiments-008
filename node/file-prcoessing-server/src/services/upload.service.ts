import { Express } from "express";

export const uploadService = (file: Express.Multer.File) => {
  return {
    filename: file.filename,
    originalName: file.originalname,
    mimeType: file.mimetype,
    size: file.size,
    uploadedAt: new Date(),
  };
};
