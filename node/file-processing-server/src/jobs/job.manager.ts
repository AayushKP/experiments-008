import crypto from "node:crypto";
import type { Job } from "../types/job.types";
import { JobStatus } from "../types/job.types";

export class JobManager {
  private jobs = new Map<string, Job>(); //this map is stored in V8 Heap Memory

  create(filePath: string): Job {
    const job: Job = {
      id: crypto.randomUUID(),
      filePath,
      status: JobStatus.PENDING,
      progress: 0,
    };

    this.jobs.set(job.id, job);
    return job;
  }

  get(id: string) {
    return this.jobs.get(id);
  }

  update(id: string, updates: Partial<Job>) {
    const job = this.jobs.get(id);

    if (!job) return;

    Object.assign(job, updates);
  }

  getAll() {
    return [...this.jobs.values()];
  }
}

export const jobManager = new JobManager();
