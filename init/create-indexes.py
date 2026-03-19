from pymongo import MongoClient

client = MongoClient("mongodb://mongos:27020")
db = client["university"]

db.students.create_index("student_id", unique=True)
db.courses.create_index("course_id", unique=True)
db.enrollments.create_index([("student_id", 1), ("course_id", 1)])

print("Indexes created successfully")