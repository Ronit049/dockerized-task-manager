# 🐳 Dockerized Task Manager

A simple full-stack Task Manager built with FastAPI, MongoDB, HTML/CSS/JavaScript and Docker Compose.

## Features

- Create tasks
- View tasks
- Complete/undo tasks
- Delete tasks
- MongoDB persistence
- FastAPI REST API
- Dockerized backend
- MongoDB Docker container
- Nginx frontend container
- Docker Compose orchestration
- Health check endpoint

## Tech Stack

- HTML, CSS, JavaScript
- FastAPI
- Python
- MongoDB
- Docker
- Docker Compose
- Nginx

## Run

Make sure Docker Desktop is running, then:

```bash
docker compose up --build
```

Open:

- Frontend: http://localhost:8080
- Backend: http://localhost:8000
- Swagger docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Useful Commands

```bash
docker compose up -d
docker compose ps
docker compose logs
docker compose logs backend
docker compose down
```

To remove the MongoDB volume too:

```bash
docker compose down -v
```

## Architecture

```text
Browser
   |
   v
Nginx Frontend :8080
   |
   v
FastAPI Backend :8000
   |
   v
MongoDB :27017
   |
   v
Docker Volume
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | API status |
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

## Author

Ronit Raj
GitHub: https://github.com/Ronit049
