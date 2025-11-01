#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys
import itertools
import copy
import json

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
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
def resolve():
    N,M=map(int, input().split())
    S=[input() for i in range(N)]
    ans_sum = 0
    S_kari =  [[[0] * M for i in range(M)] for j in range((N-M+1)*(N-M+1))]
    for i in range(N-M+1):
        for j in range(N-M+1):
            for z in range(M):
                for k in range(M):
                    S_kari[ans_sum][z][k]=  S[i+z][j+k]
            ans_sum +=1
    S_kari1 = [json.loads(x) for x in set(json.dumps(sub) for sub in S_kari)]

        
    print(len(S_kari1))

if __name__ == "__main__":
    resolve()