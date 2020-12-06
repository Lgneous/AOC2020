import sys
from collections import Counter


def part1(input_file):
    input_file.seek(0)
    content = input_file.read()
    inputs = content.split("\n\n")
    return sum(len(set(list(input.replace("\n", "")))) for input in inputs)


def part2(input_file):
    input_file.seek(0)
    content = input_file.read()
    inputs = content.split("\n\n")
    return sum(
        v == n_users
        for input in inputs
        if (n_users := len(input.split()))
        for v in Counter(list(input.replace("\n", ""))).values()
    )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            print(part1(f))
            print(part2(f))
