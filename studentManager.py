from student import Student
class StudentManager:
    def __init__(self,database):
        self.database=database
        


    def add_student(self):
        print("Your are inserting student in the list.\n")
        student_id=input("Enter student id: ")
        while True:
            name=input("Enter student name: ")
            if name.strip()!="" and name.replace(" ","").isalpha():
                break
            else:
                print("\nName cannot be empty and only contain alphabet\n")
        while True:
            try:
                age=int(input("Enter student age: "))
                break
            except ValueError:
                print("\nPlease enter valid age.\n")
        while True:        
            gender=input("Enter gender: ")
            if gender.lower()=="male"or gender.lower()=="female":
                break
            else:
                print("\nGender must be Male or Female.\n")
        while True:
            department=input("Enter department: ")
            if department.isalpha() and department!="":
                break
            else:
                print("\nEnter a valid department.\n")
        while True:
            email=input("Enter student email: ")
            if "@gmail.com" in email:
                break
            else:
                print("\nEnter a valid email.\n")
        while True:
            try:
                cgpa=float(input("Enter student cgpa: "))
                if cgpa>=0 and cgpa<=4:
                    break
                else:
                    print("Cgpa must be between 0 to 4.")
                    continue
            except ValueError:
                print("\nEnter Valid cgpa.\n")
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
                        while True:
                            name=input("Enter new name: ")
                            if name.strip()!="" and name.replace(" ","").isalpha():
                                break
                            else:
                                print("\nName cannot be empty and only contain alphabet\n")
                        student.name=name
                    elif choice=='3':
                        while True:
                            try:
                                age=int(input("Enter updated age: "))
                                break
                            except ValueError:
                                print("\nPlease enter valid age.\n")
                        student.age=age
                    elif choice=='4':
                        while True:        
                            gender=input("Updated gender: ")
                            if gender.lower()=="male"or gender.lower()=="female":
                                break
                            else:
                                print("\nGender must be Male or Female.\n")
                        student.gender=gender
                    elif choice=='5':
                        while True:
                            department=input("Enter department: ")
                            if department.isalpha() and department!="":
                                break
                            else:
                                print("\nEnter a valid department.\n")
                        student.department=department
                    elif choice=='6':
                        while True:
                            email=input("Enter student email: ")
                            if "@gmail.com" in email:
                                break
                            else:
                                print("\nEnter a valid email.\n")
                        student.email=email
                    elif choice=='7':
                        while True:
                            try:
                                cgpa=float(input("Enter updated cgpa: "))
                                if cgpa>=0 and cgpa<=4:
                                    break
                                else:
                                    print("Cgpa must be between 0 to 4.")
                                    continue
                            except ValueError:
                                print("\nEnter Valid cgpa.\n")
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

