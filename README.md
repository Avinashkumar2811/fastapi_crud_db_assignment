# 📝 To-Do List Web Application (FastAPI)

This project is a simple **To-Do List web application** developed as part of a Python assignment.  
It provides **RESTful APIs for CRUD operations**, uses **HTML templates for UI rendering**, and stores data in a **SQLite database** using **raw SQL (without ORM)**.

The application follows clean project structure, proper separation of concerns, logging, testing, and API documentation.

---

## 📌 Objective

To develop a web application using **Python and FastAPI** that:
- Manages tasks in a To-Do list
- Exposes RESTful APIs for CRUD operations
- Uses templates for a basic web interface
- Stores data in a database
- Includes testing, logging, and API documentation

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** – Web framework
- **SQLite** – Database
- **sqlite3** – Raw SQL queries (❌ No ORM used)
- **Jinja2** – HTML Templates
- **pytest** – Automated testing
- **logging** – Application logging

> ⚠️ Note: ORM and generic viewsets are **not used**, as per assignment instructions.

---
🖥️ Web Interface (Templates)
The application also provides a basic UI using HTML templates:

Home Page (/)
Displays list of all tasks

Add Task Page (/add)
Form to add a new task

Templates are rendered using Jinja2 and interact with backend logic.


📑 API Documentation
FastAPI provides automatic interactive API documentation:

Swagger UI:
👉 http://127.0.0.1:8000/docs

This includes:
Endpoint descriptions
Request/response formats
Sample payloads


🧪 Testing
Basic automated tests are implemented using pytest.

Run Tests:
In project folder run --> python -m pytest -v


Tests cover:
Create task API
Retrieve tasks API


📜 Logging & Exception Handling
Logging is configured using Python’s built-in logging module
Errors are handled gracefully using try/except and HTTPException
Logs are stored in app.log


▶️ Setup & Run Instructions
1️⃣ Create Virtual Environment
python -m venv .virt

source .virt/bin/activate   # Linux / Mac

.virt\Scripts\activate      # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Application
In project folder run --> uvicorn app.main:app --reload --port 9067

uvicorn app.main:app --reload

4️⃣ Access Application

Web UI: http://127.0.0.1:8000/

API Docs: http://127.0.0.1:8000/docs

✅ Assignment Requirements Coverage

✔ RESTful CRUD APIs
✔ SQLite database integration
✔ Raw SQL (No ORM used)
✔ HTML templates for UI
✔ API & template integration
✔ Logging & exception handling
✔ Automated testing with pytest
✔ API documentation
✔ Clean project structure
✔ README with setup & usage instructions

