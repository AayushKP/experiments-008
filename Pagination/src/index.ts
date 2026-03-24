import express from "express";
import { Request, Response } from "express";
import axios from "axios";
import { Post } from "./types";

const app = express();
const PORT = 3000;

const API_URL = "https://jspnplaceholder.typicode.com/posts";

app.get("/offset", async (req: Request, res: Response) => {
  try {
    const page = parseInt(req.query.page as string) || 1;
    const limit = parseInt(req.query.limit as string) || 10;

    const response = await axios.get<Post[]>(API_URL);
    const data = response.data;

    const startIndex = (page - 1) * limit;
    const endIndex = startIndex + limit;

    const paginatedData = data.slice(startIndex, endIndex);

    res.json({
      page,
      limit,
      total: data.length,
      totalPage: Math.ceil(data.length / limit),
      hasNextPage: endIndex < data.length,
      hasPrevPage: startIndex > 0,
      data: paginatedData,
    });
  } catch (error) {
    res.status(500).json({ message: "Error Fetching Data" });
  }
});
