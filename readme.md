Finance Tracker Backend

A simple FastAPI-based finance tracking backend system built as part of a Python Developer Internship assignment.

The backend allows users to manage financial records such as income and expenses, apply filters, and generate financial summaries.



🚀 Features
- Create financial records
- View all records
- Update existing records
- Delete records
- Filter by category, type, and date
- Total income summary
- Total expense summary
- Current balance calculation
- Input validation using Pydantic
- Proper error handling
- SQLite database
- Swagger API documentation

---

 🛠️ Tech Stack
- Python
- FastAPI
- REST API
- SQLite
- SQLAlchemy ORM
- Pydantic
- Uvicorn

---

📁 Project Structure

bash

finance_tracker/

├── main.py

├── database.py

├── models.py

├── schemas.py

├── services.py

├── requirements.txt

└── README.md

Setup Instrustions 

1 Open the project 

--bash

--cd finance_tracker

2 Create Virtual Environment 

--bash

--python -m venv venv

3 Activate Environment 

--bash

--venv/Scripts/activate

4 Install Dependencies

--bash

--pip install -r requirements.txt

5 Run FastApi Server

--bash

--uvicorn main:app --reload
