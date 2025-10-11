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

u'''
2部グラフの判定を行うプログラム

N := 頂点の数
M := 辺の数

A,B　:= 頂点Aから頂点Bにかけて無向の辺があることを示す

dict := 辺のつながりを格納する
　　　　 collections の　dict　だとValueに配列を格納しやすい

color　:= 頂点が何色で塗られているか

'''
from collections import defaultdict 
def dfs(v,c,queue=[]):
    u'''
    v : 現在のグラフの頂点
    c : 現在参照するフラグ,1=>-1=>1と使うので渡す必要がある
    queue : 探索したグラフの頂点を入れていく
    res : global変数を使いたくないが,再帰のreturnがよくわからないのでとりあえず
    '''

    global color
    global res 
    queue.append(v)
    
    for i in list(dict[v]):
        if color[i] == c:#隣の頂点が同じ値を与えられている際Falseを返す
            res = 'No'
        elif i not in queue:#探索済みでなければ再帰する
            color[i] = c*-1#0ならcとは異なる値を格納
            dfs(i,-c,queue)#引数に-cとすることで,cが1=>-1=>1を繰り返す


#rstripが必要なことも
#input = lambda: sys.stdin.readline().rstrip()
#inputの高速化、基本はいらない、入力が長いときに使用
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')
#n=int(input())
n, m = map(int, input().split())
dict = defaultdict(set)
A=[]

color = [0 for i in range(n+1)]
res = 'Yes'
CNT=0
B=[]

#A = list(map(int, input().split()))
for i in range(m):
    a, b = map(int, input().split())
    res="Yes"
    color[1] = 1#最初の頂点を1で塗る
    dict[a].add(b)
    dict[b].add(a)
    dfs(1,1)
    if res == 'No':
        CNT+=1
    


dfs(1,1)



print(CNT)

