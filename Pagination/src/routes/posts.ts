import { Router, Request, Response } from "express";
import axios from "axios";
import { Post } from "../types/posts";

const router = Router();
const API_URL = "https://jsonplaceholder.typicode.com/posts";

// Fetch all posts once
async function fetchPosts(): Promise<Post[]> {
  const response = await axios.get<Post[]>(API_URL);
  return response.data;
}

//PAGE-BASED PAGINATION
router.get("/page", async (req: Request, res: Response) => {
  const page = Number(req.query.page) || 1;
  const limit = Number(req.query.limit) || 5;

  const posts = await fetchPosts();
  const total = posts.length;

  const start = (page - 1) * limit;
  const end = start + limit;

  const data = posts.slice(start, end);

  res.json({
    type: "page",
    page,
    limit,
    total,
    totalPages: Math.ceil(total / limit),
    nextPage: end < total ? page + 1 : null,
    prevPage: page > 1 ? page - 1 : null,
    data,
  });
});

// OFFSET-BASED PAGINATION
router.get("/offset", async (req: Request, res: Response) => {
  const offset = Number(req.query.offset) || 0;
  const limit = Number(req.query.limit) || 5;

  const posts = await fetchPosts();
  const total = posts.length;

  const data = posts.slice(offset, offset + limit);

  res.json({
    type: "offset",
    offset,
    limit,
    total,
    nextOffset: offset + limit < total ? offset + limit : null,
    prevOffset: offset - limit >= 0 ? offset - limit : null,
    data,
  });
});

// CURSOR-BASED PAGINATION
router.get("/cursor", async (req: Request, res: Response) => {
  const cursor = req.query.cursor ? Number(req.query.cursor) : null;
  const limit = Number(req.query.limit) || 5;

  const posts = await fetchPosts();

  let startIndex = 0;

  if (cursor) {
    startIndex = posts.findIndex((post) => post.id === cursor) + 1;
  }

  const data = posts.slice(startIndex, startIndex + limit);

  const nextCursor = data[data.length - 1]?.id ?? null;

  res.json({
    type: "cursor",
    cursor,
    limit,
    nextCursor,
    data,
  });
});

export default router;
