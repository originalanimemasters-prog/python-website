#!/bin/bash
# setup.sh - Local development setup

echo "Setting up DevForge development environment..."

# Backend setup
echo "Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt
python manage.py migrate
python manage.py createsuperuser

# Frontend setup
echo "Setting up frontend..."
cd ../frontend
npm install

# Return to root
cd ..

echo "Setup complete!"
echo "Backend: cd backend && source venv/bin/activate && python manage.py runserver"
echo "Frontend: cd frontend && npm run dev"
