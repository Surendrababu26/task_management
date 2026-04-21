# Task Manager Application

## Description  
This is a simple Task Manager application built using React (Frontend) and Django REST API (Backend). It allows users to perform basic CRUD operations such as adding, viewing, updating, and deleting tasks.

---

## Features  
- Add new tasks  
- View all tasks  
- Toggle task status  
- Delete tasks  

---

## Technologies  
- React.js  
- Django REST Framework  
- SQLite  

---

## Setup  

### Backend  
cd backend  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

### Frontend  
cd frontend  
npm install  
npm start  

---

## Run Project  
1. Run backend using:  
   python manage.py runserver  

2. Run frontend using:  
   npm start  

3. Open browser → http://localhost:3000  

---

## API Endpoints  

GET /api/tasks/  
POST /api/tasks/  
PUT /api/tasks/:id/  
DELETE /api/tasks/:id/  

---

## Author  
YANAMADALA SURENDRABABU  