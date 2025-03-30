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
def resolve():
    n=int(input())
    sum_s=[]
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    for i in range(n):
        s = input()
        if i == 0:
            sum_s.append(s)
        for j in range(len(sum_s)):
            if len(sum_s[j]) < len(s):
                sum_s.append(s)
                break
            if len(sum_s[j]) > len(s):
                sum_s.insert(j,s)
                break
    print(''.join(sum_s))

if __name__ == "__main__":
    resolve()