# DevForge - Developer Platform

A unified platform combining coding practice, backend challenges, online judge, project/snippet sharing, technical blogging, community features, and contests.

## Quick Start

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements/dev.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Judge Engine Setup
```bash
cd judge-engine
# Build Docker images for each language
docker build -t devforge-python-runner docker-images/python-runner/
docker build -t devforge-js-runner docker-images/javascript-runner/
```

## Project Structure

- `backend/` - Django REST API
- `frontend/` - React TypeScript frontend
- `judge-engine/` - Code execution sandbox
- `infra/` - Infrastructure & deployment configs
- `docs/` - Documentation
- `scripts/` - Utility scripts

## API Documentation

Visit http://localhost:8000/api/docs/ for interactive API documentation.
