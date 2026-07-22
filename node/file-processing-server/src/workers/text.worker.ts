import { parentPort } from "node:worker_threads";
import { processTextFile } from "../processors/text.processor";

parentPort?.on(
  "message",
  async ({ jobId, filePath }: { jobId: string; filePath: string }) => {
    try {
      const result = await processTextFile(filePath, (progress) => {
        parentPort?.postMessage({
          type: "progress",
          jobId,
          progress,
        });
      });

      parentPort?.postMessage({
        type: "completed",
        jobId,
        success: true,
        result,
      });
    } catch (error) {
      parentPort?.postMessage({
        type: "completed",
        jobId,
        success: false,
        error: error instanceof Error ? error.message : "Unknown Error",
      });
    }
  },
);
