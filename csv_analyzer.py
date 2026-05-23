import csv
import json

def load_students(filename):
    students = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append(row)
    return students
def analyze(students):
    total = 0
    countries = {}
    completed = 0

    for student in students:
        total += 1  # 1. total 加 1
        # 2. 把 student["country"] 计入 countries 字典
        countries[student["country"]] = countries.get(student["country"], 0) + 1
        if student["bet_status"] == "completed":
            completed += 1  # 3. 如果 student["bet_status"] == "completed"，completed 加 1

    completion_rate = completed / total if total > 0 else 0  # 用 completed 除以 total 算出来

    return {
        "total": total,
        "by_country": countries,
        "completion_rate": completion_rate
    }
def save_report(report, filename):
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

students = load_students("students.csv")
report = analyze(students)
save_report(report, "report.json")
print("完成！报告已保存到 report.json")
print(report)