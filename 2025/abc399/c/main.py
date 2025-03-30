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
# 遷移元の頂点

#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらん、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#float型の無限大inf
def resolve():
    N, m = map(int, input().split())
    graph: List[List[int]] = [[] for i in range(N)]
    # 入次数を記録する配列
    indegree: List[int] = [0] * N
    # グラフの構築
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        # 無向グラフなので入次数はどちらの頂点も増える
        indegree[u] += 1
        indegree[v] += 1
    in_cycle: List[bool] = [len(g) != 1 for i, g in enumerate(graph)]
    candidate = collections.deque([i for i, g in enumerate(graph) if len(g) == 1])
    while candidate:
        node: int = candidate.popleft()
        for next_node in graph[node]:
            # サイクルに含まれないことが確定している場合、スキップする
            if not in_cycle[next_node]:
                continue
            # 頂点nodeを削除する(nodeが消えたことで、頂点next_nodeの入次数は1つ減る)
            indegree[next_node] -= 1
            # 頂点nodeを削除したことにより入次数が1以下になった場合、その頂点は閉路には属さない。
            if indegree[next_node] <= 1:
                in_cycle[next_node] = False
                candidate.append(next_node)
    # UnionFind木
    uf = UnionFind(N)
    # 閉路に属する頂点集合S
    cycle: Set[int] = {i for i, b in enumerate(in_cycle) if b}
    # 探索済みかどうかを表す配列(幅優先探索で使う)
    explored: List[bool] = [False] * N
    # 閉路に属する各頂点s(つまり各部分木の根)から探索を開始する
    for start in cycle:
        # 幅優先探索により、各部分木の頂点全てを根と紐付ける
        candidate = collections.deque([start])
        explored[start] = True

        while candidate:
            node: int = candidate.popleft()

            for next_node in graph[node]:
                if next_node in cycle or explored[next_node]:
                    continue
                explored[next_node] = True
                candidate.append(next_node)
                uf.unite(start, next_node)

if __name__ == "__main__":
    resolve()