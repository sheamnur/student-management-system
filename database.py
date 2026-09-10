import psycopg
from psycopg import errors
from student import Student
class Database:
    def __init__(self):
        self.connection=psycopg.connect(
            host="localhost",
            dbname="student",
            port=5432,
            user="postgres",
            password="your password()"
        )
        self.cursor=self.connection.cursor()
        


    def save_student(self,student):
        try:
            self.cursor.execute(
                "insert into students " \
                "values(%s,%s,%s,%s,%s,%s,%s)",(student.student_id,student.name,
                                                student.gender,student.department,student.email,student.cgpa,student.age)
            )
            self.connection.commit()
            print("\nStudent successfully added.")
        except errors.UniqueViolation:
            self.connection.rollback()
            print("\nStudent id already exists.\n")
        except errors.NotNullViolation:
            self.connection.rollback()
            print("\nRequired field cannot be empty.\n")
        except errors.NumericValueOutOfRange:
            self.connection.rollback()
            print("\nCgpa is not valid\n")

    def get_student(self):
        self.cursor.execute(
            "select * from students " \
            "order by student_id"
        )
        students=[]
        rows=self.cursor.fetchall()
        for row in rows:
            student_id=row[0]
            name=row[1]
            age=row[6]
            gender=row[2]
            department=row[3]
            email=row[4]
            cgpa=row[5]
            student=Student(student_id,name,age,gender,department,email,cgpa)
            students.append(student)
        return students

    def update_student(self,student,student_id):
        try:
            self.cursor.execute(
                "update students " \
                "set student_id=%s, name=%s, gender=%s, department=%s, email=%s,cgpa=%s,age=%s "
                 "where student_id=%s",
                 (student.student_id,student.name,student.gender,student.department,student.email,student.cgpa,student.age,student_id)
            )
            self.connection.commit()
            print("\nStudent information update successfully")
        except errors.UniqueViolation:
            self.connection.rollback()
            print("\nStudent id already exists.\n")
        except errors.NotNullViolation:
            self.connection.rollback()
            print("\nRequired field cannot be empty.\n")
        except errors.NumericValueOutOfRange:
            self.connection.rollback()
            print("\nCgpa is not valid\n")

    def delete_student(self,student_id):
        self.cursor.execute(
            "delete from students " \
            "where student_id=%s",
            (student_id,)
        )
        self.connection.commit()
        print("\nStudent delete successfully.")

    
        
