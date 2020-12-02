import sys


def part1(input_file):
  res = 0
  for line in input_file:
    n, (c, _), password = line[:-1].split(' ')
    min_n, max_n = map(int, n.split('-'))
    res += password.count(c) in range(min_n, max_n + 1)
  return res


def part2(input_file):
  res = 0
  for line in input_file:
    n, (c, _), password = line[:-1].split(' ')
    min_n, max_n = map(int, n.split('-'))
    res += (password[min_n - 1] == c) ^ (password[max_n - 1] == c)
  return res


if __name__ == "__main__":
  if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
      print(part1(f))
      print(part2(f))
