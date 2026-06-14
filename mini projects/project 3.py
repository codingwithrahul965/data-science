students = []
def add_student():
    name = input("enter name:")
    marks =input("enter marks:")
    student ={"name":name , "marks":marks}
    students.append(student)
    print("student added successfully")

def show_students():
        for s in students:
            print(s["name"],"-",s["marks"])

def average_marks():
    total = 0
    for s in students:
        total += int(s["marks"])

    if len(students) > 0:
            print("average", total/ len(students))
    else:
             print("no students found")
while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Average Marks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        average_marks()

    elif choice == "4":
        break

    else:
        print("Invalid choice")


