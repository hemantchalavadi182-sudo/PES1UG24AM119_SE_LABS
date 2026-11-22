import math


def parse_application(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split(':')

    if len(parts) != 2:
        raise ValueError("Invalid application format")

    visa = parts[0].strip()
    entries_text = parts[1].strip()

    if not visa:
        raise ValueError("Visa type cannot be empty")

    try:
        entries = int(entries_text)
    except ValueError:
        raise ValueError("Entries must be an integer")

    if entries < 0:
        raise ValueError("Entries cannot be negative")

    return visa.title(), entries


def processing_average(days_csv):
    if not isinstance(days_csv, str):
        raise ValueError("Input must be a string")

    parts = days_csv.split(',')

    if not parts or any(not value.strip() for value in parts):
        raise ValueError("Invalid processing days")

    try:
        values = [int(value.strip()) for value in parts]
    except ValueError:
        raise ValueError("Processing days must be integers")

    if any(value < 0 for value in values):
        raise ValueError("Processing days cannot be negative")

    return sum(values) // len(values)


def payable_fee(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    parts = text.split('|')

    if len(parts) != 2:
        raise ValueError("Invalid fee format")

    try:
        fee = float(parts[0].strip())
        discount = float(parts[1].strip())
    except ValueError:
        raise ValueError("Fee and discount must be numbers")

    if not math.isfinite(fee) or not math.isfinite(discount):
        raise ValueError("Fee and discount must be finite")

    if fee < 0 or discount < 0:
        raise ValueError("Fee and discount cannot be negative")

    total = fee * 1.18 - discount

    return max(total, 0)


def main():
    print("==== Running parse_application ====")
    user_input = input("Enter visa type:entries (e.g. tourist:2): ")
    result = parse_application(user_input)
    print("Visa Type and Entries:", result)

    print("\n==== Running processing_average ====")
    user_input = input("Enter processing days as CSV (e.g. 5,10,21): ")
    result = processing_average(user_input)
    print("Average Processing Days:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 6000|500): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()
