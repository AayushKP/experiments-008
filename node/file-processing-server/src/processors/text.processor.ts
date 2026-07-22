import fs from "node:fs";
import readline from "node:readline";

export async function processTextFile(
  filePath: string,
  onProgress?: (progress: number) => void,
) {
  const stream = fs.createReadStream(filePath);

  const rl = readline.createInterface({
    input: stream,
    crlfDelay: Infinity,
  });

  let lines = 0;
  let words = 0;
  let characters = 0;

  for await (const line of rl) {
    lines++;
    words += line.split(/\s+/).filter(Boolean).length;
    characters += line.length;

    if (lines % 100 === 0) {
      onProgress?.(lines);
    }
  }

  return {
    lines,
    words,
    characters,
  };
}
