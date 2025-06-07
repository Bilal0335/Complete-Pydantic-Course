from typing import List, Optional
from pydantic import BaseModel, HttpUrl

# Address model (optional, just to add depth)
class Address(BaseModel):
    street: str
    city: str
    country: str

# User model
class User(BaseModel):
    id: int
    name: str
    email: str
    address: Optional[Address] = None

# Comment model
class Comment(BaseModel):
    id: int
    content: str
    user: User
    replies: Optional[List['Comment']] = None  # Recursive replies

# Forward reference resolve
Comment.model_rebuild()

# BlogPost model
class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    image: Optional[HttpUrl] = None
    author: User
    comments: Optional[List[Comment]] = None

# Example usage
import json

# Sample data
address = Address(street="123 Main St", city="Lahore", country="Pakistan")
user1 = User(id=1, name="Ali", email="ali@example.com", address=address)

# Comment tree
comment1 = Comment(id=1, content="Nice post!", user=user1)
comment2 = Comment(id=2, content="Thanks!", user=user1, replies=[comment1])

# Blog post
post = BlogPost(
    id=101,
    title="My First Blog",
    content="Yeh mera pehla blog post hai.",
    image="https://example.com/image.jpg",
    author=user1,
    comments=[comment2]
)

# Pretty print using json
# print(json.dumps(post.model_dump(), indent=2))
print(json.dumps(post.model_dump(mode="json"), indent=2))


# 

"""
Zaroor! Aapka code **bohot achha** likha gaya hai aur main aapko **step by step**, **beginner-friendly** aur **deep explanation** ke sath har part samjhaata hoon. Let's break it down from the very top:

---

## ✅ 1. Importing Modules

```python
from typing import List, Optional
from pydantic import BaseModel, HttpUrl
import json
```

### 🔍 Explanation:

* `List`: agar kisi field mein multiple cheezen store karni hain (e.g. list of comments)
* `Optional`: ye batata hai ke koi field zaroori (**required**) nahi hai, wo `None` bhi ho sakta hai
* `BaseModel`: Pydantic ka base class jisse hum apne data model banate hain
* `HttpUrl`: ek special type jo ensure karta hai ke jo URL diya gaya hai wo **valid URL** ho (e.g., `https://example.com`)
* `json`: built-in Python module jo Python objects ko JSON string mein convert karta hai

---

## ✅ 2. Address Model

```python
class Address(BaseModel):
    street: str
    city: str
    country: str
```

### 🔍 Explanation:

Ye ek **simple data structure** hai jo ek banda ka address represent karta hai.

* `street`, `city`, `country` — teen string fields hain.

---

## ✅ 3. User Model

```python
class User(BaseModel):
    id: int
    name: str
    email: str
    address: Optional[Address] = None
```

### 🔍 Explanation:

Yahan humne ek **User ka model** banaya hai:

* `id`: user ka unique ID (number)
* `name`: user ka naam
* `email`: email address
* `address`: optional field — ye `Address` model ka object hoga. Agar address diya gaya hai to theek warna default `None` hoga.

---

## ✅ 4. Comment Model

```python
class Comment(BaseModel):
    id: int
    content: str
    user: User
    replies: Optional[List['Comment']] = None
```

### 🔍 Explanation:

Ye model ek **comment ko represent karta hai**, jaise kisi post ke neeche log likhte hain.

* `id`: comment ka ID
* `content`: comment ka text
* `user`: jis user ne ye comment kiya
* `replies`: ek comment ke andar **replies ka list** (matlab nested comments). Ye optional hai, ho bhi sakti hain aur nahi bhi.

> 🔁 **Recursive model** hai — `Comment` ke andar phir `Comment` list. Isi liye `'Comment'` string mein likha gaya hai.

---

## ✅ 5. `Comment.model_rebuild()`

```python
Comment.model_rebuild()
```

### 🔍 Explanation:

Yeh line sirf **Pydantic 2.x** ke liye hai. Jab aap kisi model ke andar usi model ka reference dete hain (self-referencing model), to Pydantic ko kehna padta hai:
**"Ab sab cheezen define ho gayi hain, ab ja ke dobara model build karo."**

---

## ✅ 6. BlogPost Model

```python
class BlogPost(BaseModel):
    id: int
    title: str
    content: str
    image: Optional[HttpUrl] = None
    author: User
    comments: Optional[List[Comment]] = None
```

### 🔍 Explanation:

Ye model ek **Blog Post** represent karta hai:

* `id`: post ka ID
* `title`: post ka title
* `content`: post ka likha gaya text
* `image`: optional image URL (HttpUrl ensure karta hai ke ye valid URL ho)
* `author`: jis user ne post likhi
* `comments`: is post ke comments (list of `Comment` objects)

---

## ✅ 7. Sample Data (Object Creation)

```python
address = Address(street="123 Main St", city="Lahore", country="Pakistan")
user1 = User(id=1, name="Ali", email="ali@example.com", address=address)
```

### 🔍 Explanation:

Yahan humne ek `Address` aur `User` object banaya.

---

```python
comment1 = Comment(id=1, content="Nice post!", user=user1)
comment2 = Comment(id=2, content="Thanks!", user=user1, replies=[comment1])
```

### 🔍 Explanation:

* `comment1`: ek comment banaya hai ("Nice post!")
* `comment2`: doosra comment hai jisme reply hai `comment1` (nested reply)

---

```python
post = BlogPost(
    id=101,
    title="My First Blog",
    content="Yeh mera pehla blog post hai.",
    image="https://example.com/image.jpg",
    author=user1,
    comments=[comment2]
)
```

### 🔍 Explanation:

Ab humne ek **complete blog post** banaya:

* Usme title hai
* Content hai
* Ek image ka URL hai
* Author hai (user1)
* Ek comment hai jisme ek nested reply hai

---

## ✅ 8. JSON Convert and Print

```python
print(json.dumps(post.model_dump(mode="json"), indent=2))
```

### 🔍 Explanation:

* `model_dump(mode="json")`: ye sab objects ko JSON-compatible bana deta hai
* `json.dumps(..., indent=2)`: JSON ko **pretty print** karta hai (indentation se readable banata hai)

---

## 🎯 Output Mein Kya Aayega?

Output ek JSON hoga jo aapko complete post, user info, comments aur replies sab dikhaayega, kuch is tarah:

```json
{
  "id": 101,
  "title": "My First Blog",
  "content": "Yeh mera pehla blog post hai.",
  "image": "https://example.com/image.jpg",
  "author": {
    "id": 1,
    "name": "Ali",
    "email": "ali@example.com",
    "address": {
      "street": "123 Main St",
      "city": "Lahore",
      "country": "Pakistan"
    }
  },
  "comments": [
    {
      "id": 2,
      "content": "Thanks!",
      "user": {
        "id": 1,
        "name": "Ali",
        "email": "ali@example.com",
        "address": {
          "street": "123 Main St",
          "city": "Lahore",
          "country": "Pakistan"
        }
      },
      "replies": [
        {
          "id": 1,
          "content": "Nice post!",
          "user": {
            "id": 1,
            "name": "Ali",
            "email": "ali@example.com",
            "address": {
              "street": "123 Main St",
              "city": "Lahore",
              "country": "Pakistan"
            }
          },
          "replies": null
        }
      ]
    }
  ]
}
```

---

## 🧠 Aap Aage Kya Seekh Sakte Hain?

Agar aap chahen to next level pe:

1. **FastAPI endpoints** banana seekhein (e.g., POST, GET blog)
2. **Image upload** endpoint banana
3. **Data ko database (e.g. SQLite, PostgreSQL) mein store karna**
4. **Frontend (React/Vue)** se connect karna

---

Aap bolo, **agla step aap kis taraf le jaana chahte ho?**
Main code ke sath samjhaata rahunga.



"""