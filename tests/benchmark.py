import json
import random
import string
import time
from pymongo import MongoClient

client = MongoClient("mongodb://mongos:27020")
db = client["university"]
students = db["students"]


def random_name():
    return ''.join(random.choices(string.ascii_letters, k=12))


def benchmark_insert(n=10000, start_id=1000000):
    docs = []
    for i in range(n):
        docs.append({
            "student_id": start_id + i,
            "full_name": random_name(),
            "faculty": random.choice(["CS", "Math", "Physics", "Economics"]),
            "year": random.randint(1, 4),
            "group_name": f"G-{random.randint(1, 100)}",
            "email": f"user{start_id + i}@example.com"
        })

    start = time.perf_counter()
    students.insert_many(docs)
    end = time.perf_counter()

    total = end - start
    return {
        "operation": "insert",
        "count": n,
        "total_seconds": total,
        "ops_per_sec": n / total if total else 0
    }


def benchmark_read(n=10000, min_id=1000000, max_id=1009999):
    ids = [random.randint(min_id, max_id) for _ in range(n)]

    start = time.perf_counter()
    for sid in ids:
        students.find_one({"student_id": sid})
    end = time.perf_counter()

    total = end - start
    return {
        "operation": "read",
        "count": n,
        "total_seconds": total,
        "ops_per_sec": n / total if total else 0
    }


def benchmark_update(n=5000, min_id=1000000, max_id=1009999):
    ids = [random.randint(min_id, max_id) for _ in range(n)]

    start = time.perf_counter()
    for sid in ids:
        students.update_one(
            {"student_id": sid},
            {"$set": {"year": random.randint(1, 4)}}
        )
    end = time.perf_counter()

    total = end - start
    return {
        "operation": "update",
        "count": n,
        "total_seconds": total,
        "ops_per_sec": n / total if total else 0
    }


def benchmark_delete(n=5000, min_id=1000000, max_id=1009999):
    ids = [random.randint(min_id, max_id) for _ in range(n)]

    start = time.perf_counter()
    for sid in ids:
        students.delete_one({"student_id": sid})
    end = time.perf_counter()

    total = end - start
    return {
        "operation": "delete",
        "count": n,
        "total_seconds": total,
        "ops_per_sec": n / total if total else 0
    }


def main():
    results = []

    insert_result = benchmark_insert()
    print(insert_result)
    results.append(insert_result)

    read_result = benchmark_read()
    print(read_result)
    results.append(read_result)

    update_result = benchmark_update()
    print(update_result)
    results.append(update_result)

    delete_result = benchmark_delete()
    print(delete_result)
    results.append(delete_result)

    with open("results/benchmark_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Benchmark finished. Results saved to results/benchmark_results.json")


if __name__ == "__main__":
    main()