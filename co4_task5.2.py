def read_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()


def percentage(attended, total):
    if total <= 0:
        raise ValueError("Total attendance must be greater than zero")
    return attended / total * 100


def write_report(filename, report):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)


if __name__ == "__main__":
    records = read_data("attendance.txt")
    result = percentage(20, 25)
    write_report(
        "report.txt",
        f"Attendance: {result:.2f}%"
    )
    print("Report generated.")
