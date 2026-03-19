from pymongo import MongoClient
from faker import Faker
import random
from datetime import datetime

fake = Faker()

client = MongoClient("mongodb://mongos:27020")
db = client["university"]

students = db["students"]
courses = db["courses"]
enrollments = db["enrollments"]


def generate_courses():
    courses.delete_many({})

    docs = []
    course_names = [
        "NoSQL Databases",
        "Algorithms",
        "Python Programming",
        "Data Engineering",
        "Machine Learning",
        "Distributed Systems",
        "Operating Systems",
        "Computer Networks",
        "Statistics",
        "Linear Algebra"
    ]

    for i, name in enumerate(course_names, start=1):
        docs.append({
            "course_id": i,
            "course_name": name,
            "teacher": fake.name(),
            "credits": random.randint(2, 5)
        })

    courses.insert_many(docs)
    print(f"Inserted {len(docs)} courses")


def generate_students(n=100000):
    students.delete_many({})

    faculties = ["CS", "Math", "Physics", "Economics", "Biology"]
    docs = []

    for i in range(1, n + 1):
        docs.append({
            "student_id": i,
            "full_name": fake.name(),
            "faculty": random.choice(faculties),
            "year": random.randint(1, 4),
            "group_name": f"G-{random.randint(1, 50)}",
            "email": f"student{i}@university.local",
            "created_at": datetime.utcnow()
        })

        if len(docs) == 5000:
            students.insert_many(docs)
            print(f"Inserted students up to {i}")
            docs = []

    if docs:
        students.insert_many(docs)
        print(f"Inserted final batch, total students: {n}")


def generate_enrollments(n=300000):
    enrollments.delete_many({})

    docs = []

    for i in range(n):
        docs.append({
            "student_id": random.randint(1, 100000),
            "course_id": random.randint(1, 10),
            "semester": random.choice(["2025-fall", "2026-spring"]),
            "grade": random.randint(4, 10),
            "status": random.choice(["active", "completed"]),
            "created_at": datetime.utcnow()
        })

        if len(docs) == 5000:
            enrollments.insert_many(docs)
            print(f"Inserted enrollments: {i + 1}")
            docs = []

    if docs:
        enrollments.insert_many(docs)
        print(f"Inserted final enrollments batch, total: {n}")


if __name__ == "__main__":
    generate_courses()
    generate_students(100000)
    generate_enrollments(300000)
    print("Data initialization completed")