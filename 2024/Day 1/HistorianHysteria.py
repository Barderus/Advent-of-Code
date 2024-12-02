def read_input():
    with open('input.txt') as file:
        data = file.read().split()

        # Convert to integer
        data = [int(x) for x in data]

        right = []
        left = []
        for i in range(len(data)):
            if i % 2 == 0:
                right.append(data[i])
            else:
                left.append(data[i])
        right.sort()
        left.sort()

        return right, left


def calculate_sum(right, left):
    abs_difference = 0
    for i in range(len(right)):
        abs_difference += abs(right[i] - left[i])

    return abs_difference


def calc_score(right, left):
    # Calculate the sum of a * left.count(a) for each element in 'right'
    count_sum = 0
    for a in right:
        count_sum += a * left.count(a)

    return count_sum


def main():
    right, left = read_input()
    print("Sum of absolute differences: ", calculate_sum(right, left))
    print("Score: ", calc_score(right, left))


main()
