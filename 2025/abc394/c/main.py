#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys,re
#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
def resolve():
    s=input()
    ans = []
    #a, b = map(int, input().split())
    #A = list(map(int, input().split()))
    j = 0
    #l = s.split(', ')
    #pat = re.compile('({})'.format('|'.join(map(re.escape,s))))
    #print(pat)
    for i in range(len(s),-1,-1):
        if 'W'*i+'A' in s:
            #pat = pat.replace('W'*i+'A','A'+'C'*i)
            #re.sub('W'*i+'A','A'+'C'*i,s)
            re.sub(['W'],'A',s)
    print(s)              

if __name__ == "__main__":
    resolve()