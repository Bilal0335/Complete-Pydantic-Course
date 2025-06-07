
# ! example 01
# from pydantic import BaseModel, Field,ConfigDict
# from typing import List, Optional
# from datetime import datetime


# class Address(BaseModel):
#     street: str
#     city: str
#     state: str
#     zip_code: str


# class User(BaseModel):
#     user_id: int
#     name: str
#     email: str
#     is_active: bool = True
#     address: Optional[Address] = None
#     # created_at: datetime = Field(default_factory=datetime.utcnow)
#     createdAt: datetime
#     tags: List[str] = []
#     model_config = ConfigDict(
#         json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
#     )

# # user instance
# user = User(
#     user_id=1,
#     name="John Doe",
#     email="bilal@gmail.com",
#     created_at=datetime(2023, 10, 1, 12, 0, 0),
#     address=Address(
#         street="123 Main St",
#         city="Anytown",
#         state="CA",
#         zip_code="12345"
#     ),
#     tags=["admin", "user"]
# )

# #! using model_dump() --> dict
# user_dict = user.model_dump()
# print("User as dict:")
# print(user_dict)
# print("\n=*25\n")
# #! using model_dump_json() --> json   
# user_json = user.model_dump_json(indent=2)
# print("\nUser as JSON:")
# print(user_json)


# ! example 02
# from pydantic import BaseModel, Field, ConfigDict
# from typing import List, Optional
# from datetime import datetime
# import json
# from pydantic.json import pydantic_encoder

# class Address(BaseModel):
#     street: str
#     city: str
#     state: str
#     zip_code: str

# class User(BaseModel):
#     user_id: int
#     name: str
#     email: str
#     is_active: bool = True
#     address: Optional[Address] = None
#     createdAt: datetime
#     tags: List[str] = []

#     model_config = ConfigDict(
#         json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
#     )

# user = User(
#     user_id=1,
#     name="John Doe",
#     email="bilal@gmail.com",
#     createdAt=datetime(2023, 10, 1, 12, 0, 0),
#     address=Address(
#         street="123 Main St",
#         city="Anytown",
#         state="CA",
#         zip_code="12345"
#     ),
#     tags=["admin", "user"]
# )

# # Dump using model_dump (dict)
# user_dict = user.model_dump()
# print("User as dict:")
# print(user_dict)

# print("\n=*25=*\n")

# # Dump using json.dumps + pydantic_encoder + custom encoder
# user_json = json.dumps(user_dict, indent=2, default=pydantic_encoder)
# print("User as JSON (with custom datetime):")
# print(user_json)


# ! example 03
# from pydantic import BaseModel, Field, ConfigDict
# from datetime import datetime
# from typing import List, Optional

# class Address(BaseModel):
#     street: str
#     city: str
#     state: str
#     zip_code: str

# class User(BaseModel):
#     user_id: int
#     name: str
#     email: str
#     is_active: bool = True
#     address: Optional[Address] = None
#     createdAt: datetime
#     tags: List[str] = []

#     model_config = ConfigDict(
#         json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
#     )

# # Create instance
# user = User(
#     user_id=1,
#     name="John Doe",
#     email="bilal@gmail.com",
#     createdAt=datetime(2023, 10, 1, 12, 0, 0),
#     address=Address(
#         street="123 Main St",
#         city="Anytown",
#         state="CA",
#         zip_code="12345"
#     ),
#     tags=["admin", "user"]
# )

# # Print JSON
# print(user.model_dump_json(indent=2))
