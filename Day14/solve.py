import collections
import itertools
import re
import sys


def masked(i, mask):
  i = i | int(mask.replace("X", "0"), 2)
  n_x = mask.count("X")
  prod = itertools.product("01", repeat=n_x)
  ret = []
  i_as_string = "{:036b}".format(i)
  for p in prod:
    p = iter(p)
    mask_lst = list(mask.replace("1", "0"))
    for i in range(len(mask_lst)):
      if mask_lst[i] == "X":
        mask_lst[i] = next(p)
      else:
        mask_lst[i] = i_as_string[i]

    ret.append(int("".join(mask_lst), 2))
  return ret

def part1(f):
  f.seek(0)
  content = f.read().split('\n')
  mem = [0] * 2 ** 16
  for line in content:
    var, val = line.split(" = ")
    if var == "mask":
      mask = val
      continue
    i = int(re.search(r"mem\[(\d+)\]", var).group(1))
    mask_one = int(mask.replace("0", "0").replace("X", "1"), 2)
    mask_two = int(mask.replace("X", "0"), 2)
    val = int(val)
    mem[i] = (val & mask_one) | mask_two
  return sum(mem)

def part2(f):
  f.seek(0)
  content = f.read().split("\n")
  mem = collections.defaultdict(int)
  for line in content:
    var, val = line.split(" = ")
    if var == "mask":
      mask = val
      continue
    i = int(re.search(r"mem\[(\d+)\]", var).group(1))
    val = int(val)
    for i in masked(i, mask):
      mem[i] = val
  return sum(mem.values())


with open(sys.argv[1]) as f:
  print(part1(f))
  print(part2(f))
