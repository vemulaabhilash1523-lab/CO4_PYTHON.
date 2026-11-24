from pathlib import Path
import csv
from datetime import datetime

# Folder containing daily attendance files
input_folder = Path("attendance_files")

# Create output folder
output_folder = Path("output")
output_folder.mkdir(exist_ok=True)

# Dictionary to store attendance details
attendance = {}

# List to store damaged records
damaged_records = []

# Count valid records
valid_records = 0

# Get all CSV files from the input folder
files = list(input_folder.glob("*.csv"))

# Process each attendance file
for file in files:

    try:
        with open(file, "r", encoding="utf-8") as f:

            for line_number, line in enumerate(f, start=1):

                fields = line.strip().split(",")

                # Check whether the line has three fields
                if len(fields) != 3:
                    damaged_records.append(
                        f"{file.name}, Line {line_number}: Missing or extra fields"
                    )
                    continue

                register_number, date, status = fields

                # Validate the fields
                if not register_number.strip():
                    damaged_records.append(
                        f"{file.name}, Line {line_number}: Missing register number"
                    )
                    continue

                try:
                    datetime.strptime(date.strip(), "%Y-%m-%d")
                except ValueError:
                    damaged_records.append(
                        f"{file.name}, Line {line_number}: Invalid date"
                    )
                    continue

                status = status.strip().upper()

                if status not in ["P", "A"]:
                    damaged_records.append(
                        f"{file.name}, Line {line_number}: Invalid attendance status"
                    )
                    continue

                register_number = register_number.strip()

                # Create student entry if not available
                if register_number not in attendance:
                    attendance[register_number] = {
                        "present": 0,
                        "absent": 0
                    }

                # Update attendance count
                if status == "P":
                    attendance[register_number]["present"] += 1
                else:
                    attendance[register_number]["absent"] += 1

                valid_records += 1

    except OSError as error:
        damaged_records.append(
            f"{file.name}: File error - {error}"
        )

# Generate monthly attendance report
report_file = output_folder / "attendance_report.csv"

with open(report_file, "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Register Number",
        "Present Days",
        "Absent Days",
        "Total Days",
        "Attendance Percentage",
        "Below 75%"
    ])

    for register_number, details in attendance.items():

        present = details["present"]
        absent = details["absent"]
        total = present + absent

        percentage = (present / total) * 100

        shortage = "Yes" if percentage < 75 else "No"

        writer.writerow([
            register_number,
            present,
            absent,
            total,
            round(percentage, 2),
            shortage
        ])

# Generate damaged records log
log_file = output_folder / "damaged_records.txt"

with open(log_file, "w", encoding="utf-8") as f:

    for record in damaged_records:
        f.write(record + "\n")

# Display final results
print("MONTHLY ATTENDANCE REPORT")
print("-------------------------")

for register_number, details in attendance.items():

    present = details["present"]
    absent = details["absent"]
    total = present + absent

    percentage = (present / total) * 100

    print("Register Number:", register_number)
    print("Present Days:", present)
    print("Absent Days:", absent)
    print("Attendance Percentage:", round(percentage, 2), "%")

    if percentage < 75:
        print("Status: Below 75%")
    else:
        print("Status: Eligible")

    print()

print("Valid Records:", valid_records)
print("Damaged Records:", len(damaged_records))
print("Attendance report saved successfully.")
print("Damaged record log saved successfully.")
