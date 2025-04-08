'''
DP 사용하는 문제 

상향식 사용하기

'''
import sys

input=sys.stdin.readline

n=int(input())

#테이블화를 이용한 피보나치 수열
def fib_dp_tab(n):
    f=[None]*(n+1)
    #기반 상황 저장해주기
    f[0]=0
    f[1]=1
    for i in range(2,n+1):
        #이미 1은 저장됨 2부터
        f[i]=f[i-1]+f[i-2]
    return f[n] #i는 n까지 도니까

print(fib_dp_tab(n))