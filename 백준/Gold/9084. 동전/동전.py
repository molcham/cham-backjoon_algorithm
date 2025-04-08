'''
테스트 케이스를 모두 받고

한번에 출력하기 

T,N(동전의 가짓수)
각 동전의 금액을 오름차순으로 받기
M: 동전으로 만들어야 할 금액

가능한 모든 동전의 조합을 출력하기

dp 테이블(배열)을 먼저 만들어 놓고
그 안을 하나씩 채워나가면서 문제를 해결
이전 결과를 기반으로 다음 결과를 쌓아가는 방식이기에
저장공간 dp[i]이 미리 존재해야 한다.


dp[i]=i원을 만들 수 있는 조합의 수
dp[0]=1 로 시작 
=> 0원을 만드는 방법은 아무 동전도 사용하지 않는 1가지

'''

import sys
input=sys.stdin.readline

result=[]
count=0

t=int(input()) #테스트 케이스 개수

while count<t:
    n=int(input()) #동전의 가지 수
    coins=list(map(int, input().split())) 
    #case.sort(reverse=True) #큰 수 부터 정렬
    # 배열에 저장하기
    m=int(input())

    dp=[0]*(m+1)
    dp[0]=1

    for coin in coins:
        for i in range(coin,m+1):
            dp[i] += dp[i-coin]
    result.append(dp[m])
    count+=1

for i in result:
    print(i)

