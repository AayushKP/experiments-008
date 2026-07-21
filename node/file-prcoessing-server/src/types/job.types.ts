export enum JobStatus {
  PENDING = "pending",
  PROCESSING = "processing",
  COMPLETED = "completed",
  FAILED = "failed",
}

export interface Job {
  id: string;
  filePath: string;
  status: JobStatus;
  progress: number;
  result?: unknown;
  error?: string;
}
