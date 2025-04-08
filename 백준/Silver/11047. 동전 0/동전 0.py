'''
greedy 사용하기

동전을 그냥 큰 것부터 담으면 된다.

'''

import sys

n,k=map(int,input().split())
#동전은 총 n종류,그 가치의 합을 K로 만든다.

coin_list=[]

#동전의 가치 A가 오름차순으로 주어진다.
for i in range(1,n+1):
    coin_list.append(int(input()))
    coin_list.sort(reverse=True) #큰 수 부터 정렬

#print(*coin_list) 저장 확인용

#만약 '특정 화폐'보다 '거슬러 줄 돈'이 크다면 
#돈을 거슬러 주기 
#역순으로 정렬했으니까 아래의 식 상관없음
answer=0
for coin in coin_list:
    if k>=coin:
        answer +=k//coin
        k%=coin
        if k<=0: #거슬러 줄 돈이 없다면
           break
print(answer)





