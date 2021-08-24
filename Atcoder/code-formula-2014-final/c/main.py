#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys
#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
s=input()
x = False
a = ''
b = set()
for i in range(len(s)):
  if s[i] == '@':
    if x:
      b.add(a)
    a = ''
    x = True
  elif s[i] == ' ':
    if x:
      b.add(a)
    x = False
  elif x:
    a += s[i]
if x:
  b.add(a)
if len(b)==0:
    print("")
    exit()
for i in sorted(list(b)):
  if i != '':
    print(i)






