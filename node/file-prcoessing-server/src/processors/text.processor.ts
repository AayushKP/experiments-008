import fs from "node:fs";
import readline from "node:readline";

export interface FileStats {
  lines: number;
  words: number;
  characters: number;
}

export const processTextFile = async (filePath: string): Promise<FileStats> => {
  // TODO:
  // create a readable stream
  const fileStream = fs.createReadStream(filePath, {
    encoding: "utf8",
  });
  // TODO:
  // create a readline interface
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  let lines = 0;
  let words = 0;
  let characters = 0;

  for await (const line of rl) {
    lines++;

    const trimmed = line.trim();
    if (trimmed.length > 0) {
      words += trimmed.split(/\s+/).length;
    }
    characters += line.length;
  }

  return {
    lines,
    words,
    characters,
  };
};
