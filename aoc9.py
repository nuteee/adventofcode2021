def check_left(val, arr, i, j):
    return j == 0 or (j > 0 and arr[i][j - 1] > val)


def check_right(val, arr, i, j):
    length = len(arr[i])
    return j == length - 1 or (j < length - 1 and arr[i][j + 1] > val)


def check_up(val, arr, i, j):
    return i == 0 or (i > 0 and arr[i - 1][j] > val)


def check_down(val, arr, i, j):
    length = len(arr)
    return i == length - 1 or (i < length - 1 and arr[i + 1][j] > val)


def is_low_point(val, arr, i, j):
    # print(f"\t left: {check_left(val, arr, i, j)}")
    # print(f"\t right: {check_right(val, arr, i, j)}")
    # print(f"\t up: {check_up(val, arr, i, j)}")
    # print(f"\t down: {check_down(val, arr, i, j)}")
    return check_left(val, arr, i, j) and check_right(val, arr, i, j) and check_up(val, arr, i, j) and check_down(val, arr, i, j)


def main():
    arr = []
    with open('aoc9_input.txt', 'r') as f:
        arr = [line.strip() for line in f.readlines()]

    risk_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # print(f"Checking {arr[i][j]}:")
            if is_low_point(arr[i][j], arr, i, j):
                # print(f"\t\t{arr[i][j]} is a low point")
                risk_sum += 1 + int(arr[i][j])

    print(risk_sum)


if __name__ == '__main__':
    main()
