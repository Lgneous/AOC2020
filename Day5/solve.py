import sys


def seats(inputs):
    inputs = inputs.split()
    return [int("".join(map({"F":"0","B":"1","L":"0","R":"1"}.get, input)), 2) for input in inputs]


def part1(input_file):
    input_file.seek(0)
    return max(seats(input_file.read()))


def part2(input_file):
    input_file.seek(0)
    seats_ = seats(input_file.read())
    seats_ = sorted(filter(lambda n: n >> 3 not in {0b1111111, 0b0000000}, seats_))
    return next(i + 1 for i, j in zip(seats_, seats_[1:]) if j - i == 2)
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            print(part1(f))
            print(part2(f))
