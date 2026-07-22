import type { Job } from "../types/job.types";

export class JobQueue {
  private jobs: Job[] = [];

  enqueue(job: Job) {
    this.jobs.push(job);
  }

  dequeue() {
    return this.jobs.shift();
  }

  isEmpty() {
    return this.jobs.length === 0;
  }

  size() {
    return this.jobs.length;
  }
}

export const jobQueue = new JobQueue();
