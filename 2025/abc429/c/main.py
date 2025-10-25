from operator import mul
from functools import reduce
from collections import Counter
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

# 入力
def rI(): return int(sys.stdin.readline().rstrip())
def rLI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def rI1(): return (int(sys.stdin.readline().rstrip())-1)
def rLI1(): return list(map(lambda a:int(a)-1,sys.stdin.readline().rstrip().split()))
def rS(): return sys.stdin.readline().rstrip()
def rLS(): return list(sys.stdin.readline().rstrip().split())

#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらない、入力が長いときに使用
from sys import setrecursionlimit
setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
n=int(input())
#a, b = map(int, input().split())
A = rLI()
c = Counter(A)
sum_comb_c = cmb(n, 3)
cnt_count = len(c)
for i in range(len(c)):
    cnt_common = c.most_common()[i][1]
    if cnt_common >= 3:
        sum_comb_c -= cmb(cnt_common, 3)
    else:
        break
for i in range(len(c)):
    cnt_common = c.most_common()[i][1]
    n -= cnt_common
    cnt_count -= 1
    if cnt_count >= 2:
        sum_comb_c -= cmb(n, 2) * cnt_common
print(sum_comb_c)
