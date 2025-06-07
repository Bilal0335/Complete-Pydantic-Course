from pydantic import BaseModel  # type: ignore
from typing import List
import json

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

example_course = Course(
    course_id=1,
    title="Python Bootcamp",
    modules=[
        Module(
            module_id=101,
            title="Getting Started",
            lessons=[
                Lesson(lesson_id=1, title="Intro", content="Welcome to Python!"),
                Lesson(lesson_id=2, title="Setup", content="Installing Python."),
            ],
        ),
        Module(
            module_id=102,
            title="Advanced Topics",
            lessons=[
                Lesson(lesson_id=3, title="OOP", content="Classes and Objects."),
                Lesson(lesson_id=4, title="Modules", content="Using packages."),
            ],
        ),
    ],
)

print("JSON output using model_dump_json():")
print(example_course.model_dump_json(indent=2))

print("\nJSON output using model_dump() + json.dumps():")
course_dict = example_course.model_dump()
print(json.dumps(course_dict, indent=2))
