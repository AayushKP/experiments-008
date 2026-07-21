import { Router } from "express";
import { jobManager } from "../jobs/job.manager";

export const jobRouter = Router();

jobRouter.get("/:id", (req, res) => {
  const job = jobManager.get(req.params.id);

  if (!job) {
    return res.status(404).json({
      message: "Job not found",
    });
  }
  return res.json(job);
});
