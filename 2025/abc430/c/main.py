#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys

# 入力
def rI(): return int(sys.stdin.readline().rstrip())
def rLI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def rI1(): return (int(sys.stdin.readline().rstrip())-1)
def rLI1(): return list(map(lambda a:int(a)-1,sys.stdin.readline().rstrip().split()))
def rS(): return sys.stdin.readline().rstrip()
def rLS(): return list(sys.stdin.readline().rstrip().split())

N, A, BB = map(int, input().split())
S = input()

def calc(B):
  i, j, countX, countY, res = 0, 0, 0, 0, 0
  while i != len(B):
    while j != len(B) and (countX == 0 or countY == 0):
      if B[j] == 'a':
        countX += 1
      if B[j] == 'b':
        countY += 1
      j += 1
    if countX >= A and countY < B:
      res += len(B) + 1 - j
    if B[i] == 'a':
      countX -= 1
    if B[i] == 'b':
      countY -= 1
    i += 1
  return res


i, ans = 0, 0
while i != N:
  B = []
  while i != N and i < (A+BB-1):
    B.append(S[i])
    i += 1
  if len(B) != 0:
    ans += calc(B)
  else:
    i += 1
print(ans)