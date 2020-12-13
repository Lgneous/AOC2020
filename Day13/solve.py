import math
import sys


def find_first_bus(target, x):
  return (target + (x - 1)) // x * x
 
 
# Implementation of CRT stolen from rosetta
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def part1(input_file):
  input_file.seek(0)
  timestamp, buses = input_file.read().split()
  timestamp = int(timestamp)
  buses = [int(x) for x in buses.split(',') if x != 'x']
  t, bus = min((find_first_bus(timestamp, bus), bus) for bus in buses)
  return (t - timestamp) * bus


def part2(input_file):
  input_file.seek(0)
  _, buses = input_file.read().split()
  buses = [(i, int(x)) for i, x in enumerate(buses.split(',')) if x != 'x']
  moduli = [x for _, x in buses]
  residues = [x - i for i, x in buses]
  return chinese_remainder(moduli, residues)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            print(part1(f))
            print(part2(f))
