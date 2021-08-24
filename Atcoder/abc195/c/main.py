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
    n=(input())
    s=len(n)
    nn=int(n)
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    ans=0
    if 3<s<7:
        ans=nn-999
    if 6<s<10:
        ans=10**6-10**3+(2*(nn-999999))
    if 9<s<13:
        ans=(10**6-10**3)+(2*(10**9-10**6))+(3*(nn-999999999))
    if 12<s<16:
        ans=(10**6-10**3)+(2*(10**9-10**6))+(3*(10**12-10**9))+(4*(nn-999999999999))

3998998998999009
3998998998999000
    

if __name__ == "__main__":
    resolve()


