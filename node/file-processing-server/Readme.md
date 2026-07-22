# File Processing Server

## Overview

A TypeScript-based file processing server using Express, Multer, and a worker pool for asynchronous job processing.

## Architecture

```
                                        ┌─────────────┐
                                        │   Express   │
                                        │   Server    │
                                        └──────┬──────┘
                                               │
                        ┌──────────────────────┼──────────────────────┐
                        │                      │                      │
                        ▼                      ▼                      ▼
                    ┌─────────────┐     ┌──────────────┐      ┌──────────────┐
                    │   Upload    │     │     Job      │      │   Health     │
                    │   Routes    │     │    Routes    │      │    Route     │
                    └──────┬──────┘     └──────┬───────┘      └──────────────┘
                           │                   │
                           ▼                   ▼
                    ┌──────────────────┐  ┌──────────────┐
                    │  Upload Ctrlr &  │  │  Job Ctrlr & │
                    │  Upload Service  │  │ Job Manager  │
                    └──────┬───────────┘  └──────┬───────┘
                           │                     │
                           └──────────┬──────────┘
                                      │
                                      ▼
                        ┌─────────────────────────────┐
                        │  Event Bus & Job Queue      │
                        ├─────────────────────────────┤
                        │ Create jobs with PENDING    │
                        │ Emit events, manage states  │
                        └──────────────┬──────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────┐
                        │    Worker Pool           │
                        ├──────────────────────────┤
                        │ Worker 1 │ Worker 2      │
                        │ Worker 3 │ Worker N...   │
                        │ (CPU core count)         │
                        └──────────────┬───────────┘
                                       │
                                       ▼
                        ┌──────────────────────────┐
                        │  Text Job Processor      │
                        │  (Process uploaded file) │
                        └──────────────┬───────────┘
                                       │
                                       ▼
                        ┌──────────────────────────┐
                        │  Result & Status Update  │
                        │  (sent back to Worker)   │
                        └──────────────┬───────────┘
                                       │
                                       ▼
                        ┌──────────────────────────┐
                        │    Job Manager           │
                        │  (Update: COMPLETED/     │
                        │   FAILED)                │
                        └──────────────────────────┘
```

## Request Flow

```

User Request
│
▼
POST /upload
│
├─→ Multer Middleware (file validation & storage)
│
├─→ Upload Controller
│
├─→ Upload Service
│
├─→ Create Job (PENDING)
│
├─→ Emit Job Event
│
├─→ Return Job ID to Client
│
└─→ Worker Pool Picks Job
│
├─→ Update Status: PROCESSING
│
├─→ Text Processor
│
├─→ Update Status: COMPLETED with result
│
└─→ Emit Completion Event

```

## Core Components

**Upload Service**: Handles file validation, storage initialization, and job creation.

**Job Manager**: Manages in-memory job storage, state updates, and job retrieval using a Map data structure.

**Job Queue**: Receives job creation events and distributes tasks to available workers.

**Worker Pool**: Manages multiple worker threads for parallel processing, distributes jobs, collects results, prevents memory exhaustion and blocking.

**Text Processor**: Processes uploaded files, extracts content, performs analysis, returns processed results.

**Job Listener**: Listens to events, triggers workers, updates job states, handles success and failure scenarios.

**Event Bus**: Centralized event emission for job creation, processing start, completion, and error handling.

## API Endpoints

**POST /upload**: Upload file and create processing job.

**GET /jobs**: Retrieve all jobs.

**GET /jobs/:id**: Retrieve job status and details.

## Setup

```bash
npm install
npm run build
npm run dev
```

Runs on port 3000.
