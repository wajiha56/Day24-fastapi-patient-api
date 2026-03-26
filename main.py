from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# Create database table automatically
def create_table():
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            fee REAL
        )
    """)
    conn.commit()
    conn.close()


create_table()


class Patient(BaseModel):
    name: str
    fee: float


@app.post("/add_patient/")
def add_patient(patient: Patient):
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO patients (name, fee) VALUES (?, ?)",
        (patient.name, patient.fee)
    )

    conn.commit()
    conn.close()

    return {"message": "Patient added successfully!"}


@app.get("/patients/")
def get_patients():
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()

    conn.close()

    result = [{"id": p[0], "name": p[1], "fee": p[2]} for p in patients]

    return result