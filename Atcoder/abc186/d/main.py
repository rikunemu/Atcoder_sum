#!/usr/bin/env python3
# coding: utf-8
# Your code here!
n=int(input())
A = list(map(int, input().split()))
ans=result=0
A.sort()
sumA=sum(A)
for i in range(n):
    ans=A[i]
    sumA-=ans
    result+=sumA-ans*(n-i-1)

#print(sumA)
print(result)
    



