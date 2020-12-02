import itertools
import sys

def part1(input_file):
  inputs = itertools.combinations((int(s[:-1]) for s in input_file), 2)
  return next(x * y for (x, y) in inputs if x + y == 2020))


def part2(input_file):
  inputs = itertools.combinations((int(s[:-1]) for s in input_file), 3)
  return next(x * y * z for (x, y, z) in inputs if x + y + z == 2020))
  
  
if __name__ == "__main__":
  if len(sys.argv) == 2:
    print(part1(sys.argv[1]))
    print(part2(sys.argv[2]))
