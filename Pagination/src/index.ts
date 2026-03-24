import express from "express";
import axios from "axios";
import { Post } from "./types";

const app = express();
const PORT = 3000;

const API_URL = "https://jspnplaceholder.typicode.com/posts";
