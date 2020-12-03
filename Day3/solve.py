import sys


def solve(input_file, slopes):
    map_ = [row.strip() for row in input_file]
    tot = 1
    for width, height in slopes:
        count = 0
        for i in range(0, len(map_), height):
            row = map_[i]
            count += row[i // height * width % len(row)] == "#"
        tot *= count
    return tot


def part1(input_file):
    input_file.seek(0)
    return solve(input_file, [(3, 1)])


def part2(input_file):
    input_file.seek(0)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return solve(input_file, slopes)


if __name__ == "__main__":
  if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
      print(part1(f))
      print(part2(f))
