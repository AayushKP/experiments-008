import { parentPort, workerData } from "node:worker_threads";
import { processTextFile } from "../processors/text.processor";

//sends file to another thread to get processed
(async () => {
  try {
    const result = await processTextFile(workerData.filePath);
    parentPort?.postMessage(result);
  } catch (error) {
    parentPort?.postMessage({
      error: error instanceof Error ? error.message : "Unknown Error",
    });
  }
})();
