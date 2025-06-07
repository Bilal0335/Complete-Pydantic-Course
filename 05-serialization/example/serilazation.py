
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class User(BaseModel):
    user_id: int
    name: str
    email: str
    is_active: bool = True
    address: Optional[Address] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    tags: List[str] = []

# user instance
user = User(
    user_id=1,
    name="John Doe",
    email="bilal@gmail.com",
    created_at=datetime(2023, 10, 1, 12, 0, 0),
    address=Address(
        street="123 Main St",
        city="Anytown",
        state="CA",
        zip_code="12345"
    ),
    tags=["admin", "user"]
)

#! using model_dump() --> dict
user_dict = user.model_dump()
print("User as dict:")
print(user_dict)

#! using model_dump_json() --> json   
user_json = user.model_dump_json(indent=2)
print("\nUser as JSON:")
print(user_json)
