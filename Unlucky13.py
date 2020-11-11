'''
Problem Statement: https://www.hackerearth.com/practice/codemonk/
'''



from functools import lru_cache
@lru_cache(maxsize=1024)
def f(n):
    return 10**n - g(n)
def g(n):
    return sum(f(i)*10**(n-(i+2)) for i in range(n-1))
k=int(input())
for i in range(k):
    n=int(input())
    print(f(n)%1000000009)

'''
k=int(input())
for i in range(k):
    n=int(input())
    a=[0,10,99]
    if n>2:
        for i in range(3,n+1):
            temp=a[-1]
            a[-1]=((a[-1]*10)-(a[-2]))
            a[-2]=temp
    print(a[-1] % 1000000009)
'''
