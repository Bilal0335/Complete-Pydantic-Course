
# from pydantic import BaseModel

# class User(BaseModel):
#     id:int
#     name:str
#     is_active:bool = True

#     class Config:
# #         forbid ka Simple Matlab:
# # Koi bhi unknown (extra) field allow na karo — agar aaye, to error do!


#         extra = "forbid"

# input_data = {
#     "id": "1010",
#     "name": "John Doe",
#     "isActive": "True"
# }
# # Create an instance of User using the input data
# user = User(**input_data)
# # Print the user instance
# print(user)
# # print(user.dict())


from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {'id': 101, 'name': "ChaiCode", 'is_active': True}

user = User(**input_data)
print(user)