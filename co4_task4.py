def save_returns(books):
    with open("returns.log", "a", encoding="utf-8") as log:
        for book in books:
            if book.strip():
                log.write(book.strip() + "\n")


def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as file:
            books = file.readlines()

        save_returns(books)

    except FileNotFoundError as error:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(f"{day_file}: {error}\n")

    except PermissionError as error:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(f"{day_file}: {error}\n")


process("day1.txt")
process("day2.txt")
process("day3.txt")

print("Processing completed.")
