import sys


def part1(input_file):
  input_file.seek(0)
  inputs = input_file.read()
  inputs = inputs.split()
  deg = 0
  ship = 0
  for i in inputs:
    c, n = i[0], int(i[1:])
    if c == 'N':
      ship += 1j * n
    if c == 'S':
      ship -= 1j * n
    if c == 'E':
      ship += n
    if c == 'W':
      ship -= n
    if c == 'F':
      ship += 1j ** (deg // 90) * n
    if c == 'L':
      deg += n
    if c == 'R':
      deg -= n
  return int(abs(ship.real) + abs(ship.imag))

def part2(input_file):
  input_file.seek(0)
  inputs = input_file.read()
  inputs = inputs.split()
  ship = 0
  waypoint = 10 + 1j
  for i in inputs:
    c, n = i[0], int(i[1:])
    diff = waypoint - ship
    if c == 'N':
      waypoint += 1j * n
    if c == 'S':
      waypoint -= 1j * n
    if c == 'E':
      waypoint += n
    if c == 'W':
      waypoint -= n
    if c == 'F':
      ship += diff * n
      waypoint = ship + diff
    if c == 'L':
      waypoint = ship + diff * 1j ** (n // 90)
    if c == 'R':
      waypoint = ship + diff * 1j ** (-n // 90)
  return int(abs(ship.real) + abs(ship.imag))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            print(part1(f))
            print(part2(f))
