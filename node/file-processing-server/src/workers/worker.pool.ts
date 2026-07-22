import type { Job } from "../types/job.types";
import { jobManager } from "../jobs/job.manager";
import { JobStatus } from "../types/job.types";
import { jobQueue } from "../queue/job.queue";
import { Worker } from "node:worker_threads";
import path from "node:path";
import os from "node:os";

interface WorkerInstance {
  worker: Worker;
  busy: boolean;
}

export class WorkerPool {
  private workers: WorkerInstance[] = [];

  constructor() {
    const workerCount = os.cpus().length;

    for (let i = 0; i < workerCount; i++) {
      const worker = new Worker(path.join(__dirname, "text.worker.js"));

      this.workers.push({
        worker,
        busy: false,
      });

      worker.on("message", (message) => {
        const workerInstance = this.workers.find((w) => w.worker === worker);

        if (!workerInstance) {
          return;
        }

        if (message.type === "progress") {
          jobManager.update(message.jobId, {
            progress: message.progress,
          });

          return;
        }

        const { jobId, success, result, error } = message;

        if (success) {
          jobManager.update(jobId, {
            status: JobStatus.COMPLETED,
            progress: 100,
            result,
          });
        } else {
          jobManager.update(jobId, {
            status: JobStatus.FAILED,
            error,
          });
        }

        workerInstance.busy = false;

        this.processQueue();
      });

      worker.on("error", (err) => {
        console.error(err);

        const workerInstance = this.workers.find((w) => w.worker === worker);

        if (!workerInstance) {
          return;
        }

        workerInstance.busy = false;

        this.processQueue();
      });
    }
  }

  private findIdleWorker() {
    return this.workers.find((w) => !w.busy);
  }

  private processQueue() {
    while (!jobQueue.isEmpty()) {
      const worker = this.findIdleWorker();

      if (!worker) {
        return;
      }

      const job = jobQueue.dequeue();

      if (!job) {
        return;
      }

      worker.busy = true;

      jobManager.update(job.id, {
        status: JobStatus.PROCESSING,
        progress: 10,
      });

      worker.worker.postMessage({
        jobId: job.id,
        filePath: job.filePath,
      });
    }
  }

  public addJob(job: Job) {
    jobQueue.enqueue(job);

    this.processQueue();
  }
}

export const workerPool = new WorkerPool();
