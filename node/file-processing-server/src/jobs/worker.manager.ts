import path from "path/win32";
import { Worker } from "worker_threads";

export const runWorker = (filePath: string) => {
  return new Promise((resolve, reject) => {
    //starts another thread
    const worker = new Worker(
      path.join(__dirname, "../workers/text.worker.ts"),
      {
        workerData: {
          filePath,
        },
      },
    );
    worker.on("message", resolve);

    worker.on("error", reject);

    worker.on("exit", (code) => {
      reject(new Error(`Worker exited with code ${code}`));
    });
  });
};
