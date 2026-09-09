class Student:
    def __init__(self,student_id,name,age,gender,department,email,cgpa):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.gender=gender
        self.department=department
        self.email=email
        self.cgpa=cgpa


    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.age} | {self.gender} | {self.department} | {self.email} | {self.cgpa}"