from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()

@app.get("/hello")
def hello():
    return JSONResponse(content={"Hello World"}, status_code=200)

@app.get("/welcome")
def welcome(name : str):
    return JSONResponse(content={f"Welcome {name}"}, status_code=200)

class Students(BaseModel):
    Reference: str
    FistName: str
    LastName: str
    Age: int

student_list: List[Students] = []

def add_student():
    all_student: []
    for student in student_list:
        all_student.append(student.model_dump())
    return all_student

@app.post("/students")
def students():
    return {"CREATED"}

@app.get("/students")
def getStudent():
    return JSONResponse(content={"Success": add_student()}, status_code=200)