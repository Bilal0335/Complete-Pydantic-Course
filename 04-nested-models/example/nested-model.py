# from typing import Optional, List
# from pydantic import BaseModel

# class Address(BaseModel):
#     street: str
#     city: str
#     postcode: str

# class User(BaseModel):  # Capital U
#     id: int
#     name: str
#     address: Address

# class Comment(BaseModel):
#     id: int
#     content: str
#     user: User  # Yahan 'User' capital U hona chahiye
#     replies: Optional[List['Comment']] = None

# Comment.model_rebuild()  # Forward reference ke liye zaroori

# # Example usage:
# add = Address(street="123 Main St", city="Anytown", postcode="12345")
# user1 = User(id=1, name="John Doe", address=add)

# comment = Comment(
#     id=1,
#     content="First Comment",
#     user=user1,
#     replies=[
#         Comment(id=2, content="reply1", user=user1),
#         Comment(id=3, content="reply2", user=user1)
#     ]
# )
# print(comment)
# print(comment.json(indent=2))

# comment1 = Comment(id=1, content="This is a comment", user=user1)
# comment2 = Comment(id=2, content="This is a reply", user=user1, replies=[comment1])
# print(comment2)
# print(comment2.json(indent=2))

import json
from typing import Optional, List
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postcode: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    user: User
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()

add = Address(street="123 Main St", city="Anytown", postcode="12345")
user1 = User(id=1, name="John Doe", address=add)

comment = Comment(
    id=1,
    content="First Comment",
    user=user1,
    replies=[
        Comment(id=2, content="reply1", user=user1),
        Comment(id=3, content="reply2", user=user1)
    ]
)

# Pydantic V2 way to print pretty JSON:
comment_dict = comment.model_dump()
print(json.dumps(comment_dict, indent=2))