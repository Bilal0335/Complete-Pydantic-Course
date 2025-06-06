from pydantic import BaseModel, field_validator, model_validator, computed_field # type: ignore


class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values
    
class Product(BaseModel):
    price: float
    quantity: int

#** @compute_field :  This decorator is used to define a computed field in a Pydantic model. A computed field is a property that is derived from other fields in the model, and it is not stored in the database. It is calculated dynamically when accessed.

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


