from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Models
class Lesson(BaseModel):
    lesson_id: int
    title: str
    content: str

class Module(BaseModel):
    module_id: int
    title: str
    lessons: List[Lesson]

class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]

# In-memory store for courses (just for demo)
courses: List[Course] = []

# API Endpoints

@app.post("/courses/")
def create_course(course: Course):
    # Add course to the list
    courses.append(course)
    return {"message": "Course created successfully!", "course_id": course.course_id}

@app.get("/courses/")
def get_courses():
    # Return all courses
    return courses

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    # Find course by id
    for course in courses:
        if course.course_id == course_id:
            return course
    return {"error": "Course not found"}

# Run this app with:
# uvicorn your_file_name:app --reload
