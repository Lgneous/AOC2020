import sys

import numpy as np
import scipy.ndimage.filters as snf


def game_of_life_4d(board, kernel, n):
  y, x = board.shape
  M = n + 1
  arr = np.zeros((M * 2, M * 2, M * 2 + y, M * 2 + x), dtype=int)
  arr[M, M, M:M+y, M:M+x] = board
  for _ in range(n):
    neighbours = snf.convolve(arr, kernel, mode="constant", cval=0)
    new_gen = (arr == 0) & (neighbours == 3)
    survivors = (arr == 1) & (1 < neighbours) & (neighbours < 4)
    arr = (new_gen | survivors).astype(int)
  return arr.sum()


def get_input(f):
  f.seek(0)
  content = f.read().split()
  arr = []
  for line in content:
    arr.append([int(c == '#') for c in line.strip()])
  return np.array(arr, dtype=int)
  
  
def part1(f):
  arr = get_input(f)
  kernel = np.ones((1,3,3,3))
  kernel[0,1,1,1] = 0
  return game_of_life_4d(get_input(f), kernel, 6)


def part2(f):
  arr = get_input(f)
  kernel = np.ones((3,3,3,3))
  kernel[1,1,1,1] = 0
  return game_of_life_4d(get_input(f), kernel, 6)


with open(sys.argv[1]) as f:
  print(part1(f))
  print(part2(f))
