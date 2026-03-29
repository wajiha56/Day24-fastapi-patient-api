# 🌟 Day 24 – FastAPI Patient API

<div align="center">
  <a href="https://day24-fastapi-patient-api.onrender.com">
    <img src="https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge"/>
  </a>
  <a href="https://day24-fastapi-patient-api.onrender.com/docs">
    <img src="https://img.shields.io/badge/Swagger-UI-blue?style=for-the-badge"/>
  </a>
</div>

---

## 📌 Project Overview
FastAPI backend for managing **patient data** using SQLite. Fully live-deployed on Render for real client demos.

**Key Features:**  
- Add new patients & retrieve patient list  
- Pydantic for request validation  
- Fully documented API via Swagger UI  
- Cloud deployment for live demonstration  

---

## ⚡ Live Demo
| Endpoint       | URL |
|----------------|-----|
| 🌐 Live API     | [Click Here](https://day24-fastapi-patient-api.onrender.com) |
| 📄 Swagger Docs | [Click Here](https://day24-fastapi-patient-api.onrender.com/docs) |

---

## 🚀 API Endpoints

### 1️⃣ Add Patient
- **POST** `/add_patient/`  
- **Request Body Example:**
```json
{
  "name": "Ali",
  "fee": 500
}
Response Example:
{
  "message": "Patient added successfully!"
}
2️⃣ Get Patients
GET /patients/
Response Example:
[
  {"id":1, "name":"Ali", "fee":500},
  {"id":2, "name":"Sara", "fee":700}
]
⚙️ Local Setup
# Clone repo
git clone <your-repo-url>
cd Day24-fastapi-patient-api

# Create virtual environment (optional)
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn main:app --reload

# Access Swagger UI
http://127.0.0.1:8000/docs
☁️ Cloud Deployment (Render.com)
Connect GitHub repo to Render
Create New Web Service → Python 3
Build Command:
pip install -r requirements.txt
Start Command:
uvicorn main:app --host 0.0.0.0 --port 10000
Share the live URL with clients
🛠 Tech Stack
<div> <img src="https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/FastAPI-0.114.0-green?logo=fastapi&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-3.41.2-orange?logo=sqlite&logoColor=white"/> <img src="https://img.shields.io/badge/Render-Cloud-purple?logo=render&logoColor=white"/> <img src="https://img.shields.io/badge/Pydantic-2.12.5-red?logo=pydantic&logoColor=white"/> </div>
🔮 Next Steps
Add Update & Delete patient endpoints
JWT Authentication for security
Switch to PostgreSQL/MySQL for production
Add unit & integration tests
👩‍💻 Author

Wajiha Arshad – Lead Developer & Founder, The Honeybee Code Studio
