'''
위상정렬 사용

두 학생의 키를 비교 , 일부 학생들의 키만 비교 
비교한 결과를 가지고 줄 세우기 

위상 정렬은 선후 관계가 있을 때 순서대로 정리

전제 조건
1.방향 그래프여야 하고
2.사이클이 없어야 한다.

대표적인 알고리즘 2가지
1.진입 차수: 가장 직관적, 큐를 사용(탐욕+반복복)
2.DFS + 스택 : 백트래킹 느낌, 후위 순회 기반 

정렬결과가 여러개일 수 있음 답 아무거나 출력

선행과목이 있는게 진입차수가 +1
선행과목이 없는게 진입차수가 0 인거!!!

큐는 먼저 입력된게 먼저 출력됨!

'''
from collections import deque
import sys

input=sys.stdin.readline

n,m=map(int,input().split())
#n명의 학생들을 키 순서대로 줄을 세운다
#m은 키를 비교한 횟수이다
#입력 간선을 생각해주기

adj=[ [] for _ in range(n+1) ] #인접 리스트
indegree=[0]*(n+1) #진입 차수

for i in range(m):
    a,b = map(int,input().split()) #a->b a가 먼저
    adj[a].append(b) #인접리스트로 저장해주기
    indegree[b] += 1 
#b는 선행조건 a가 있으므로 진입차수 1추가
    
#1.진입 차수가 0인 노드를 먼저 큐에 넣어주기
#진입 차수가 0이라는건 제일 먼저 나와도 상관없다는거임
queue=deque()
for i in range(1,n+1): #학생 n명
    if indegree[i]==0:
        queue.append(i) #i번 학생 넣어주기

#2.위상 정렬
result=[] # 마지막에 출력할 키순으로 정렬한 리스트
while queue: #큐가 비어있지 않을때 까지 반복
    node=queue.popleft() #제일 앞의 원소를 node로
    result.append(node)

    for neighbor in adj[node]: 
    #인접한 노드 즉 , 진입차수가 1차이나는 원소들
    #-1해줘서 0으로 만들고 while문 반복 queue가 빌때까지지
        indegree[neighbor] -=1
        if indegree[neighbor]==0:
            queue.append(neighbor)

print(*result) #괄호없이 원소만 출력
        




    

