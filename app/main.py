from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://mongos:27020")
db = client["university"]
students = db["students"]


def add_student():
    try:
        student_id = int(input("student_id: "))
        full_name = input("full_name: ")
        faculty = input("faculty: ")
        year = int(input("year: "))
        group_name = input("group_name: ")
        email = input("email: ")

        doc = {
            "student_id": student_id,
            "full_name": full_name,
            "faculty": faculty,
            "year": year,
            "group_name": group_name,
            "email": email
        }

        students.insert_one(doc)
        print("Student added successfully")
    except Exception as e:
        print(f"Error: {e}")


def find_student():
    try:
        student_id = int(input("student_id: "))
        student = students.find_one({"student_id": student_id}, {"_id": 0})
        if student:
            pprint(student)
        else:
            print("Student not found")
    except Exception as e:
        print(f"Error: {e}")


def list_students():
    try:
        limit = int(input("How many students to show? "))
        for student in students.find({}, {"_id": 0}).limit(limit):
            pprint(student)
    except Exception as e:
        print(f"Error: {e}")


def update_student():
    try:
        student_id = int(input("student_id: "))
        new_email = input("new email: ")

        result = students.update_one(
            {"student_id": student_id},
            {"$set": {"email": new_email}}
        )

        if result.modified_count:
            print("Student updated successfully")
        else:
            print("Student not found or data unchanged")
    except Exception as e:
        print(f"Error: {e}")


def delete_student():
    try:
        student_id = int(input("student_id: "))
        result = students.delete_one({"student_id": student_id})

        if result.deleted_count:
            print("Student deleted successfully")
        else:
            print("Student not found")
    except Exception as e:
        print(f"Error: {e}")


def show_menu():
    print("\n=== University DB CLI ===")
    print("1. Add student")
    print("2. Find student by ID")
    print("3. List students")
    print("4. Update student email")
    print("5. Delete student")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            find_student()
        elif choice == "3":
            list_students()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            print("Bye")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()