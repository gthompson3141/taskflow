# TaskFlow - Team Task Management System

A modern, full-stack task management application built with FastAPI, Next.js, PostgreSQL, and Redis.

## Features (First Stage)

- ✅ User authentication (JWT)
- ✅ Task CRUD operations
- ✅ Task assignment
- ✅ Priority and status tracking
- ✅ RESTful API
- 🔄 Real-time updates (Coming in Phase 2)
- 📎 File attachments (Coming in Phase 2)

## Tech Stack

**Backend:**

- FastAPI (Python 3.10+)
- PostgreSQL 15
- SQLModel (ORM)
- JWT Authentication
- Redis (cache/queue)

**Frontend:**

- Next.js 14
- TypeScript
- Tailwind CSS
- (Coming soon)

## Quick Start

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Node.js 18+ (for frontend)

### 1. Clone and Setup

```bash
git clone <your-repo>
cd taskflow
```

### 2. Start Database (Docker)

```bash
# Start PostgreSQL and Redis
docker-compose up -d

# Check they're running
docker-compose ps
```

### 3. Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Run the server
uvicorn app.main:app --reload

# Server will be at http://localhost:8000
```
