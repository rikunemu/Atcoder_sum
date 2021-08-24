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
    s=(input())
    c="AKIHABARA"
    for i in range(50):
        target = 'AA' + i*'A'
        if target in s:
            print('NO')
            exit()
    if len(s)>len(c):
        print("NO")
        exit()
    if len(s)==len(c):
        for i in range(len(s)):
            if s[i]!=c[i]:
                print("NO")
                exit()
        print("YES")
        exit()
    


    if "KA" in s or "IA" in s:
        print("NO")
        exit()
    s=s.replace("A","")
    if s=="KIHBR":
        print("YES")
    else:
        print("NO")
    #print(ans-ans1)
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))

if __name__ == "__main__":
    resolve()


