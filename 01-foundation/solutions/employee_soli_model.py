
# ! example 01

# from pydantic import BaseModel, Field
# from typing import Optional
# # Todo: Create a Pydantic model for Employee with the following fields:
# #! fields:
# #* id: int
# #* name: str (min 3 char)
# #* age: int
# #* department: optional str (default "General")
# #* salary: float (min must be >= 1000)

# class Employee(BaseModel):
#     id:int
#     name:str = Field( ..., min_length=3, description="Name of the employee, must be at least 3 characters long", example="John Doe", max_length=50)
#     department: Optional[str] = Field("General", description="Department of the employee, defaults to 'General'", example="Engineering")
#     age:int = Field(..., ge=18, description="Age of the employee, must be at least 18", example=30)
#     salary:float = Field(...,ge=1000, description="Salary of the employee, must be at least 1000", example=5000.0)
#     # id: int
#     # name: str = Field(..., min_length=3)
#     # age: int
#     # department: str = "General"
#     # salary: float = Field(..., ge=1000)

# ! example 02

# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from typing import Optional, List

# app = FastAPI(title="Employee API", description="Manage employee data", version="1.0")

# # In-memory fake database
# fake_db = []

# # Pydantic Model with validation using Field()
# class Employee(BaseModel):
#     id: int = Field(..., description="Unique ID for the employee", example=1)
#     name: str = Field(..., min_length=3, max_length=50, description="Full name (min 3 characters)", example="Ali Khan")
#     age: int = Field(..., ge=18, le=60, description="Age between 18 and 60", example=30)
#     department: Optional[str] = Field("General", description="Optional department, default is 'General'", example="Engineering")
#     salary: float = Field(..., ge=1000, description="Minimum salary must be 1000", example=5000.0)

#     class Config:
#         schema_extra = {
#             "example": {
#                 "id": 1,
#                 "name": "Ali Khan",
#                 "age": 30,
#                 "department": "Engineering",
#                 "salary": 5500.0
#             }
#         }

# # POST endpoint to create employee
# @app.post("/employees", summary="Create new employee", response_model=Employee)
# def create_employee(emp: Employee):
#     fake_db.append(emp)
#     return emp

# # GET endpoint to return all employees
# @app.get("/employees", summary="Get all employees", response_model=List[Employee])
# def get_employees():
#     return fake_db

# # GET endpoint to return employee by ID
# @app.get("/employees/{emp_id}", summary="Get employee by ID", response_model=Employee)
# def get_employee_by_id(emp_id: int):
#     for emp in fake_db:
#         if emp.id == emp_id:
#             return emp
#     return {"error": "Employee not found"}


# ! Example 03
from pydantic import BaseModel # type: ignore

# TODO: Create Product model with id, name, price, in_stock

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True