import express from "express";
import { uploadRouter } from "./routes/ upload.route";

export const app = express();

app.use(express.json());

app.use("/upload", uploadRouter);

app.get("/health", (req, res) => {
  res.send("Server working");
});
