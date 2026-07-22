import { parentPort } from "node:worker_threads";
import { processTextFile } from "../processors/text.processor";

parentPort?.on(
  "message",
  async ({ jobId, filePath }: { jobId: string; filePath: string }) => {
    try {
      const result = await processTextFile(filePath);
      parentPort?.postMessage({
        jobId,
        success: true,
        result,
      });
    } catch (error) {
      parentPort?.postMessage({
        jobId,
        success: false,
        error: error instanceof Error ? error.message : "Unknown Error",
      });
    }
  },
);
