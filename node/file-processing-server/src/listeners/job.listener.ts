import { eventBus } from "../events/eventBus";
import { jobManager } from "../jobs/job.manager";
import { JobStatus } from "../types/job.types";
import { workerPool } from "../workers/worker.pool";

eventBus.on("job.created", async (job) => {
  try {
    jobManager.update(job.id, {
      status: JobStatus.PROCESSING,
      progress: 25,
    });
    const result = workerPool.addJob(job);

    jobManager.update(job.id, {
      status: JobStatus.COMPLETED,
      progress: 100,
      result,
    });
  } catch (error) {
    jobManager.update(job.id, {
      status: JobStatus.FAILED,
      error: error instanceof Error ? error.message : "Unknown Error",
    });
  }
});
