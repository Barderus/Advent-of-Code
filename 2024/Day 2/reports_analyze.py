def read_input():
    with open("input.txt") as file:
        data = file.read().splitlines()

    # Transform the values into integers
    reports = [list(map(int, line.split())) for line in data if line.strip()]
    return reports


def is_safe_report(report):
    direction = None
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        # Differences must be within the range [1, 3]
        if diff < -3 or diff > 3 or diff == 0:
            return False

        # Establish or enforce direction
        current_direction = 1 if diff > 0 else -1
        if direction is None:
            direction = current_direction
        elif current_direction != direction:
            return False
    return True


def can_be_safe_with_dampener(report):
    for i in range(len(report)):
        # Remove one level (i-th element) from the report
        modified_report = report[:i] + report[i + 1:]
        if is_safe_report(modified_report):
            return True
    return False


def check_safety(reports):
    return sum(1 for report in reports if is_safe_report(report) or can_be_safe_with_dampener(report))


def main():
    reports = read_input()
    print(f"Safe reports: {check_safety(reports)}")


main()
