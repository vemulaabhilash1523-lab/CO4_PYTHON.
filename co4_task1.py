def calculate_mess_bill(filename):
    total = 0.0
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected 3 fields")

                    register_no = parts[0].strip()
                    name = parts[1].strip()
                    amount = float(parts[2].strip())

                    report.append(f"{name} {amount:.2f}")
                    total += amount

                except (ValueError, IndexError) as error:
                    rejected.append(
                        (line_number, line.strip(), str(error))
                    )

        print("MESS BILL REPORT")
        for item in report:
            print(item)

        print("Total:", f"{total:.2f}")

        print("\nRejected Records:")
        for item in rejected:
            print(item)

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    return total, rejected


calculate_mess_bill("mess_oct.txt")
