import express from "express";
import { uploadRouter } from "./routes/ upload.route";
import { jobRouter } from "./routes/job.route";

export const app = express();

app.use(express.json());

app.use("/upload", uploadRouter);
app.use("/jobs", jobRouter);

app.get("/health", (req, res) => {
  res.send("Server working");
});
