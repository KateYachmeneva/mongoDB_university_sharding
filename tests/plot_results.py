import json
import matplotlib.pyplot as plt

with open("results/benchmark_results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

operations = [item["operation"] for item in results]
times = [item["total_seconds"] for item in results]
ops_per_sec = [item["ops_per_sec"] for item in results]

plt.figure(figsize=(8, 5))
plt.bar(operations, times)
plt.xlabel("Operation")
plt.ylabel("Time (seconds)")
plt.title("MongoDB benchmark: execution time")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("results/benchmark_time.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(operations, ops_per_sec)
plt.xlabel("Operation")
plt.ylabel("Operations per second")
plt.title("MongoDB benchmark: throughput")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("results/benchmark_ops.png")
plt.close()

print("Plots saved:")
print("- results/benchmark_time.png")
print("- results/benchmark_ops.png")