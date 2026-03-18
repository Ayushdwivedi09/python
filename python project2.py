#student portal
# user login
print("Welcome to the Student Portal")
user={
    "admin":"1234",
    "ayush":"abcd",
}
students = []
# Login
def login():
    print("===STUDENT PORTAL LOGIN===")
    uid= input("Enter User ID: ")
    pwd= input("Enter Password: ")
    if uid in user and user[uid]==pwd:
        print("Login successful!")
        return True
    else:
        print("Invalid User ID or Password. Please try again.")
        return False

# Add student
def add_student():
    student = {}
    student["ID"] = input("Enter Student ID: ")
    student["Name"] = input("Enter Name: ")
    student["Age"] = input("Enter Age: ")
    student["Course"] = input("Enter Course: ")
    student["Marks"] = input("Enter Marks: ")
    student["total lectures"] = input("Enter total lectures: ")
    student["total present"] = input("Enter total present: ")
    student["total absent"] = input("Enter total absent: ")
    student["assignment"] = []
    students.append(student)
    print(" Student added successfully!")

# View all students
def view_students():
    if not students:
       print("No students found.")
    for s in students:
            print(f"ID: {s['ID']} \n  Name: {s['Name']} \n Age: {s['Age']} \n Course: {s['Course']} \n  Marks: {s['Marks']} \n  Total Lectures: {s['total lectures']} \n  Total Present: {s['total present']} \n  Total Absent: {s['total absent']} \n ")
            if "assignment" in s and s["assignment"]:
                print("Assignments:")
                for a in s["assignment"]:
                    print(f"  Title: {a['title']} | Content: {a['content']}")
            else:
                print("No assignments uploaded.")
            print("-----------------------------")

# Search student by ID
def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s["ID"] == sid:
            print("  student Found:")
            return
    print(" Student not found.")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            print("Student deleted successfully!")
            return
    print(" Student not found.")

#uplpoad student assignment
def upload_assignment():
    sid = input("Enter Student ID to upload assignment: ")
    for s in students:
        if s["ID"] == sid:
            # Ensure 'assignment' key exists
            if "assignment" not in s:
                s["assignment"] = []
            title = input("Enter assignment title: ")
            content = input("Enter assignment content: ")
            s["assignment"].append({"title": title, "content": content})
            print(f"Assignment for {s['Name']} uploaded successfully!")
            return
    print("Student not found.")

# Main menu
if login(): #if login is successful
    print("Login successful! Welcome to the Student Portal.")
while True:
    print("\n===== Student Portal =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Upload Assignment")
    print("6. Exit")
#choice
    ch= input("Enter your choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        search_student()
    elif ch == "4":
        delete_student()
    elif ch == "5":
        upload_assignment()
    elif ch == "6":
        print(" Exiting...")
        break
    else:
        print(" Invalid choice! Try again.")
