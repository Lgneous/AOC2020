import itertools
import sys


def part1(input_file):
  input_file.seek(0)
  inputs = itertools.combinations((int(s[:-1]) for s in input_file), 2)
  return next(x * y for (x, y) in inputs if x + y == 2020))


def part2(input_file):
  input_file.seek(0)
  inputs = itertools.combinations((int(s[:-1]) for s in input_file), 3)
  return next(x * y * z for (x, y, z) in inputs if x + y + z == 2020))
  
  
if __name__ == "__main__":
  if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
      print(part1(f))
      print(part2(f))
