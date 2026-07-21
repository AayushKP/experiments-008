import type { Express } from "express";
import { eventBus } from "../events/eventBus";
import { jobManager } from "../jobs/job.manager";

export const uploadService = async (file: Express.Multer.File) => {
  const job = jobManager.create(file.path);
  eventBus.emit("job.created", job);

  return {
    jobId: job.id,
    status: job.status,
    message: "Processing started",
  };
};
