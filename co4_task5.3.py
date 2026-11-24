def read_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def percentage(present, total):
    if total == 0:
        return 0.0
    return present / total * 100


def write_report(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":
    records = read_data("attendance.txt")
    result = percentage(20, 25)

    write_report(
        "report.txt",
        f"Attendance: {result:.2f}%"
    )

    print("Report generated.")
