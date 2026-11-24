def read_attendance(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def attendance_percentage(present, total):
    if total == 0:
        return 0.0
    return present / total * 100


def write_report(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    records = read_attendance("attendance.txt")
    result = attendance_percentage(20, 25)

    write_report(
        "report.txt",
        f"Attendance: {result:.2f}%"
    )

    print("Report generated.")
