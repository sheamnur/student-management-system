from studentManager import StudentManager
from database import Database
database=Database()
studentManager=StudentManager(database)
print("\n----------Welcome to the Student Management System----------\n")
print("          1.Add Student\n" \
"          2.View Student\n" \
"          3.Search Student\n" \
"          4.Update Student\n" \
"          5.Delete Student\n" \
"\n      Press anything else for exit.\n")

while True:
    choice=input("\nEnter you choice: ")
    print()
    if choice=='1':
        studentManager.add_student()
    elif choice=='2':
        studentManager.view_student()
    elif choice=='3':
        studentManager.search_student()
    elif choice=='4':
        studentManager.update_student()
    elif choice=='5':
        studentManager.delete_student()
    else:
        print("Thank you for using , Bye.")
        break

database.cursor.close()
database.connection.close()
