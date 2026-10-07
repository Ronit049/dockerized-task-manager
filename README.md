# 🐳 Dockerized Task Manager

<p align="center">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">
  <img src="https://img.shields.io/badge/Nginx-Frontend-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx">
</p>

<p align="center">
  <strong>A simple full-stack Task Manager demonstrating Docker, Docker Compose, FastAPI, MongoDB, and Nginx.</strong>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-api-documentation">API</a> •
  <a href="#-docker-commands">Docker</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## 📌 Overview

**Dockerized Task Manager** is a lightweight full-stack task management application built to demonstrate how multiple services can work together using **Docker Compose**.

The application allows users to:

- ➕ Create tasks
- 📋 View tasks
- ✅ Complete or undo tasks
- 🗑️ Delete tasks
- 💾 Persist tasks using MongoDB
- 🔌 Communicate with a FastAPI REST API

The entire application runs through **Docker containers**, making the project easy to set up and run on any machine with Docker installed.

---

## ✨ Features

### 📝 Task Management

- Create new tasks
- Add task descriptions
- View all tasks
- Mark tasks as completed
- Undo completed tasks
- Delete tasks
- Automatic task persistence

### 🐳 Docker

- Dockerized FastAPI backend
- MongoDB container
- Nginx frontend container
- Docker Compose orchestration
- Persistent MongoDB volume
- Container restart policies
- Environment-based configuration

### ⚡ Backend

- FastAPI REST API
- Pydantic request validation
- MongoDB integration
- CRUD operations
- API health check
- Interactive Swagger documentation

### 🎨 Frontend

- Clean responsive interface
- Vanilla HTML/CSS/JavaScript
- REST API integration
- Task status management
- Error handling

---

# 🏗️ Architecture

```text
                         🌐 Browser
                              │
                              ▼
                 ┌────────────────────────┐
                 │   🟢 Nginx Frontend    │
                 │       Port: 8080       │
                 └────────────┬───────────┘
                              │
                              │ HTTP Requests
                              ▼
                 ┌────────────────────────┐
                 │  ⚡ FastAPI Backend     │
                 │       Port: 8000       │
                 └────────────┬───────────┘
                              │
                              │ MongoDB Driver
                              ▼
                 ┌────────────────────────┐
                 │    🍃 MongoDB          │
                 │      Port: 27017       │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │   💾 Docker Volume     │
                 │     mongodb_data       │
                 └────────────────────────┘
```

---

# 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | FastAPI |
| Language | Python |
| Database | MongoDB |
| Web Server | Nginx |
| Containerization | Docker |
| Orchestration | Docker Compose |
| API Documentation | Swagger / OpenAPI |
| Database Driver | PyMongo |

---

# 📂 Project Structure

```text
dockerized-task-manager/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   └── models.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .dockerignore
├── .env.example
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Prerequisites

Make sure you have installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git

Verify Docker:

```bash
docker --version
```

Verify Docker Compose:

```bash
docker compose version
```

---

## 2️⃣ Clone the Repository

```bash
git clone https://github.com/Ronit049/dockerized-task-manager.git
```

Move into the project:

```bash
cd dockerized-task-manager
```

---

## 3️⃣ Build and Run

Run:

```bash
docker compose up --build
```

Docker will:

```text
1. Build the FastAPI backend
2. Pull the MongoDB image
3. Pull the Nginx image
4. Create the Docker network
5. Create the MongoDB volume
6. Start all containers
```

---

# 🚀 Access the Application

Once the containers are running:

### 🌐 Frontend

```text
http://localhost:8080
```

### ⚡ FastAPI Backend

```text
http://localhost:8000
```

### 📚 Swagger API Documentation

```text
http://localhost:8000/docs
```

### ❤️ Health Check

```text
http://localhost:8000/health
```

---

# 🐳 Docker Services

Docker Compose starts three services:

```text
┌──────────────────────────────┐
│       Docker Compose         │
├──────────────────────────────┤
│                              │
│ 🟢 frontend                  │
│    Nginx :8080               │
│                              │
│ 🟢 backend                   │
│    FastAPI :8000             │
│                              │
│ 🟢 mongodb                   │
│    MongoDB :27017            │
│                              │
└──────────────────────────────┘
```

---

# 🔌 API Documentation

## Get API Status

```http
GET /
```

Response:

```json
{
  "message": "Dockerized Task Manager API is running 🚀"
}
```

---

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy",
  "database": "connected"
}
```

---

## Get All Tasks

```http
GET /tasks
```

Example response:

```json
[
  {
    "id": "65123abc...",
    "title": "Learn Docker",
    "description": "Learn Docker Compose",
    "completed": false
  }
]
```

---

## Create Task

```http
POST /tasks
```

Request:

```json
{
  "title": "Learn Docker",
  "description": "Learn Docker Compose and containers"
}
```

---

## Update Task

```http
PUT /tasks/{task_id}
```

Example:

```json
{
  "completed": true
}
```

---

## Delete Task

```http
DELETE /tasks/{task_id}
```

---

# 🐳 Docker Commands

### Start

```bash
docker compose up
```

### Build and Start

```bash
docker compose up --build
```

### Run in Background

```bash
docker compose up -d
```

### Stop

```bash
docker compose down
```

### View Running Containers

```bash
docker compose ps
```

### View All Logs

```bash
docker compose logs
```

### Backend Logs

```bash
docker compose logs backend
```

### MongoDB Logs

```bash
docker compose logs mongodb
```

### Frontend Logs

```bash
docker compose logs frontend
```

### Follow Logs

```bash
docker compose logs -f
```

---

# 💾 MongoDB Persistence

MongoDB uses a Docker named volume:

```yaml
volumes:
  mongodb_data:
```

This means your tasks remain available even if the containers are stopped or recreated.

To completely remove the containers **and database data**:

```bash
docker compose down -v
```

> ⚠️ `docker compose down -v` permanently removes the MongoDB volume and stored tasks.

---

# 🔐 Environment Variables

Create a `.env` file if you need custom configuration.

Example:

```env
MONGO_URL=mongodb://mongodb:27017
DATABASE_NAME=task_manager
```

Never commit real secrets or credentials to GitHub.

The repository contains:

```text
.env.example
```

instead of sensitive environment files.

---

# 🧪 Testing the API

You can test the API directly through Swagger:

```text
http://localhost:8000/docs
```

Or using `curl`.

### Create Task

```bash
curl -X POST "http://localhost:8000/tasks" \
-H "Content-Type: application/json" \
-d "{\"title\":\"Learn Docker\",\"description\":\"Practice Docker Compose\"}"
```

### Get Tasks

```bash
curl http://localhost:8000/tasks
```

---

# 📸 Screenshots

> Add screenshots of your running application here.

### 🏠 Task Dashboard

```text
docs/screenshots/dashboard.png
```

### 📚 Swagger API

```text
docs/screenshots/swagger.png
```

### 🐳 Docker Containers

```text
docs/screenshots/docker.png
```

---

# 🔄 Application Flow

```text
User
 │
 ▼
Nginx Frontend
 │
 │ REST API
 ▼
FastAPI
 │
 │ PyMongo
 ▼
MongoDB
 │
 ▼
Docker Volume
```

---

# 🎯 Learning Objectives

This project was created to practice:

- Docker fundamentals
- Dockerfiles
- Docker Compose
- Container networking
- Docker volumes
- Environment variables
- REST APIs
- FastAPI
- MongoDB
- Nginx
- Multi-container architecture
- Backend/frontend communication

---

# 🗺️ Roadmap

Future improvements:

- [ ] 🔐 User authentication
- [ ] 👤 User-specific tasks
- [ ] 🔎 Task search
- [ ] 🏷️ Task categories
- [ ] 📅 Due dates
- [ ] 🚦 Task priorities
- [ ] 🌙 Dark mode
- [ ] 📊 Task statistics
- [ ] 🧪 Automated tests
- [ ] 🔄 GitHub Actions CI/CD
- [ ] ☁️ Cloud deployment
- [ ] 🔒 HTTPS support
- [ ] 📈 Application monitoring

---

# 🤝 Contributing

Contributions are welcome!

### Fork the repository

```bash
git clone https://github.com/Ronit049/dockerized-task-manager.git
```

Create a branch:

```bash
git checkout -b feature/new-feature
```

Make your changes and commit:

```bash
git add .
git commit -m "Add new feature"
```

Push:

```bash
git push origin feature/new-feature
```

Then open a Pull Request.

---

# 📜 License

This project is open source and available under the **MIT License**.

---

# 👨‍💻 Author

## Ronit Raj

💻 Computer Science Student  
🐍 Python Developer  
🌐 Web Developer  
🤖 AI & Agentic AI Enthusiast  
🐳 Docker & DevOps Learner

### Connect with me

<p>
  <a href="https://github.com/Ronit049">
    <img src="https://img.shields.io/badge/GitHub-Ronit049-181717?style=for-the-badge&logo=github">
  </a>
  <a href="https://www.linkedin.com/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin">
  </a>
</p>

---

<p align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with ❤️ and 🐳 Docker**

</p>