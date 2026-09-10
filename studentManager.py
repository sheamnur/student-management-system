from student import Student
class StudentManager:
    def __init__(self,database):
        self.database=database
        


    def add_student(self):
        print("Your are inserting student in the list.\n")
        student_id=input("Enter student id: ")
        name=input("Enter student name: ")
        age=int(input("Enter student age: "))
        gender=input("Enter gender: ")
        department=input("Enter department: ")
        email=input("Enter student email: ")
        cgpa=float(input("Enter student cgpa: "))
        student=Student(student_id,name,age,gender,department,email,cgpa)
        self.database.save_student(student)

    def view_student(self):
        students=self.database.get_student()
        if not students:
            print("Empty")
            return
        for student in students:
            print(student)


    def search_student(self):
        print("Start searching.\n")
        students=self.database.get_student()
        if not students:
            print("\nNo student in the list.")
            return
        student_id=input("Enter student id: ")
        for student in students:
            if student.student_id==student_id:
                print(student)
                return
        print("\nStudent not found!")



    def update_student(self):
        print("You are updating student information.\n")
        students=self.database.get_student()
        if not students:
            print("\nStudent list are empty.")
            return
        student_id=input("Enter student id: ")
        old_id=student_id
        for student in students:
            if student.student_id==student_id:
                while True:
                    print("1.Update id   " \
                    "2.Update Name\n" \
                    "3.Update age   " \
                    "4.Update gender\n" \
                    "5.Update department   " \
                    "6.Update email\n" \
                    "7.Update cgpa   " \
                    "Anything else to discard\n ")
                    choice=input("Enter your choice for update: ")
                    if choice=='1':
                        student_id=input("Enter new student id: ")
                        student.student_id=student_id
                    elif choice=='2':
                        name=input("Enter new name: ")
                        student.name=name
                    elif choice=='3':
                        age=int(input("Enter updated age: "))
                        student.age=age
                    elif choice=='4':
                        gender=input("Updated gender: ")
                        student.gender=gender
                    elif choice=='5':
                        department=input("Enter department: ")
                        student.department=department
                    elif choice=='6':
                        email=input("Enter updated email: ")
                        student.email=email
                    elif choice=='7':
                        cgpa=float(input("Enter updated cgpa: "))
                        student.cgpa=cgpa
                    
                    else:
                        break
                self.database.update_student(student,old_id)
                return
        print("\nStudent not found.")




    def delete_student(self):
        print("Your are deleting student.\n")
        students=self.database.get_student()
        if not students:
            print("Student list are empty.")
            return
        student_id=input("Enter student id for delete student info: ")
        for student in students:
            if student.student_id==student_id:
                self.database.delete_student(student_id)
                return
        print("\nStudent Not found.")

