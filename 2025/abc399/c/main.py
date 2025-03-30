#!/usr/bin/env python3
from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians,ceil,floor
from fractions import Fraction
from decimal import Decimal
import sys
from collections import deque
from typing import *
import collections

def rI(): return int(sys.stdin.readline().rstrip())
def rLI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def rI1(): return (int(sys.stdin.readline().rstrip())-1)
def rLI1(): return list(map(lambda a:int(a)-1,sys.stdin.readline().rstrip().split()))
def rS(): return sys.stdin.readline().rstrip()
def rLS(): return list(sys.stdin.readline().rstrip().split())

#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * -~n
        self.rank = [1] * -~n
        self.count = n
    def root(self, x):
        while (p:=self.parent[x]) != -1:
            x = p
        return x
    def union(self, x, y):
        xr = self.root(x)
        yr = self.root(y)
        if xr == yr: return
        elif (rx:=self.rank[xr]) < (ry:=self.rank[yr]):
            self.parent[xr] = yr
            self.rank[yr] += rx
        else:
            self.parent[yr] = xr
            self.rank[xr] += ry
        self.count -= 1
    def same(self,x,y):
        # err(self.root(x), self.root(y))
        return self.root(x) == self.root(y)
def resolve():
    N, M = rLI()
    uf = UnionFind(N)
    ans = 0
    for i in range(M):
        u,v = rLI()
        if uf.same(u,v):
            ans += 1
        else:
            uf.union(u,v)
    print(ans)

if __name__ == "__main__":
    resolve()