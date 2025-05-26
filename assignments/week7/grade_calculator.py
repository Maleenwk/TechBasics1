from sys import argv
import csv
import random
import statistics

# Global variables
students = []
WEEKS = [f"Week {i}" for i in range(1, 14) if i != 6]  # Skip Week 6
GRADE_OPTIONS = ["", 1, 2, 3]

# Step 1
def read_csv(filename):
    global students
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = [row for row in reader]
            print("CSV Headers:", students[0].keys())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()

# Step 2
def populate_scores():
    for student in students:
        for week in WEEKS:
            # Fill in random score only if value is empty and week >= 7
            if week not in student or student[week].strip() == "":
                week_number = int(week.split()[1])
                if week_number >= 7:
                    student[week] = str(random.choice(GRADE_OPTIONS))

# Step 3
def calculate_all():
    for student in students:
        scores = [safe_int(student[week]) for week in WEEKS]
        total = calculate_total(scores)
        average = calculate_average(scores)
        student["Total Points"] = total
        student["Average Points"] = average

def calculate_total(scores):
    top_scores = sorted([s for s in scores if s > 0], reverse=True)[:10]
    total = sum(top_scores)
    return min(total, 30)

def calculate_average(scores):
    valid_scores = [s for s in scores if s > 0]
    if valid_scores:
        return round(statistics.mean(valid_scores), 2)
    else:
        return 0.0

def safe_int(value):
    try:
        return int(value)
    except:
        return 0

# Save new CSV
def write_csv(filename):
    if not students:
        return
    fieldnames = list(students[0].keys())
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

# Bonus
def print_analysis():
    print("\n🎓 Average Points by Stream")
    print("----------------------------")
    for stream in ['A', 'B']:
        avg = stream_average(stream)
        print(f"Stream {stream}: {avg} points")

    print("\nAverage Points per Week")
    print("----------------------------")
    for week in WEEKS:
        avg = week_average(week)
        print(f"{week:8}: {avg} points")

def stream_average(stream_name):
    filtered = [s for s in students if s["Stream"].strip().lower() == stream_name.lower()]
    if not filtered:
        return 0.0
    return round(statistics.mean([float(s["Average Points"]) for s in filtered]), 2)

def week_average(week):
    values = [safe_int(s[week]) for s in students if week in s and s[week].strip() != ""]
    if not values:
        return 0.0
    return round(statistics.mean(values), 2)

# Entry point
if __name__ == "__main__":
    script, filename = argv

    print("Open file:", filename)

    read_csv(filename)

    populate_scores()
    calculate_all()

    user_name = "maleen"  # ← Update with your name

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname)
    print("New file written:", newname)

    print_analysis()