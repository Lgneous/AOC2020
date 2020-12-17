import sys

import numpy as np
import scipy.ndimage.filters as snf


def get_input(f):
  f.seek(0)
  content = f.read().split()
  arr = []
  for line in content:
    arr.append([int(c == '#') for c in line.strip()])
  return np.array(arr, dtype=int)


def game_of_life_nd(board, n, dims):
  kernel = np.ones((3,)*dims)
  kernel[(1,)*dims] = 0
  y, x = board.shape
  M = n + 1
  arr = np.zeros((M * 2,) * (dims - 2) + (M * 2 + y, M * 2 + x), dtype=int)
  arr[((M,) * (dims - 2)) + (slice(M, M+y), slice(M, M+x))] = board
  for _ in range(n):
    neighbours = snf.convolve(arr, kernel, mode="constant", cval=0)
    new_gen = (arr == 0) & (neighbours == 3)
    survivors = (arr == 1) & (1 < neighbours) & (neighbours < 4)
    arr = (new_gen | survivors).astype(int)
  return arr.sum()


with open(sys.argv[1]) as f:
  print(game_of_life_nd(get_input(f), 6, 3))
  print(game_of_life_nd(get_input(f), 6, 4))
