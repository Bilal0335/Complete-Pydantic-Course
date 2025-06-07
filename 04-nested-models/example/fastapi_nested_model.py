from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# -------------------------------
# Models
# -------------------------------

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Optional[Address] = None

class Comment(BaseModel):
    id: int
    content: str
    user: User
    replies: Optional[List['Comment']] = None  # Forward reference

# Recursive model fix
# Hum Comment model ke andar khud Comment ka reference use kar rahe hain (i.e. nested structure). Isay recursive model kehte hain.
Comment.model_rebuild()

class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    image: Optional[HttpUrl] = None
    author: User
    comments: Optional[List[Comment]] = None

# -------------------------------
# In-memory data store
# -------------------------------

posts: List[BlogPost] = []

# -------------------------------
# Root Route (Optional)
# -------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to the Blog API!"}

# -------------------------------
# API Endpoints
# -------------------------------

@app.post("/posts/")
def create_post(post: BlogPost):
    posts.append(post)
    return {"message": "Post added successfully!", "post_id": post.id}

@app.get("/posts/")
def get_posts():
    return posts
