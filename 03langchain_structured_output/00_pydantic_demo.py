from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class Student(BaseModel):
    name: str
    age: int = 12
    grade: int = 8
    division: Literal["L", "M", "N", "O"] = None
    email: Optional[EmailStr] = None
    cgpa: float = Field(ge=0, le=10, default=0, description="CGPA of the student must be between 0 and 10")

# in below line, division will automatically be filled with default value None and age will be filled with default value 12.
# Other values will be picked from the initialization and override the defaults.
# The value of grade will be coerced from string to int by pydantic
new_student = {'name':"Champu", 'grade':"7", 'email':"champu@example.com", 'cgpa': 8.5}

student = Student(**new_student)

print(student)
