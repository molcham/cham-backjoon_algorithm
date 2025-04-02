'''
위상정렬 이용하기
0이라는거는 진입차수가 없다

중간부품에 대한 기본부품을 result에 저장해놓기
위상정렬로 누적계산?

기본 부품은 무조건 1,2,3,4

출력은 기본부품 1~4가 각각 몇개 필요한지
더 숫자가 커질 수록 선행 부품이 많아짐

*위상 정렬 + 가중치 포함 으로 푸는 복합적인 그래프 문제
*위상 정렬을 하는 그래프에도 가중치가 있을 수 있음
*예를 들어 작업 스케줄링,프로젝트 완료 시간 계산 
*각 작업에 걸리는 시간도 있고, 순서도 있고

*adj[u].append((v,w))
u에서 v로 가는 데 걸리는 시간/필요한 부품 = w

A를 만들기 위해 B가 3개 필요하다
간선 B->A 에 가중치 3이 붙은 것과 같다.

<이 문제는 어떤 스킬이 필요하냐면...>

위상 정렬 : 순서를 정하고 , 진입차수 0부터 시작
배열 누적 : 필요한 부품 개수 누적(needs 배열)
가중치: 간선에 부품 개수(가중치)가 있으므로 단순 연결이 아님


'''

from collections import deque
import sys

#1단계 : 기본 자료구조 세팅팅
input=sys.stdin.readline

n=int(input()) 
#1부터 n-1 까지는 기본 부품이나 중간 부품의 번호
#n은 완제품의 번호
m=int(input())
#m개의 줄에는 
#어떤 부품을 완성하는데 필요한 부품들의 관계 몇개 받을건지

adj=[ [] for _ in range(n+1) ] #인접 리스트
indegree=[0]*(n+1) #진입 차수
needs = [[0] * (n + 1) for _ in range(n + 1)] 
# needs[x][y]: x를 만들기 위해 y가 몇 개 필요한지


#2단계:관계 입력받기
for _ in range(m):
    x,y,k = map(int,input().split()) #a->b a가 먼저
    adj[y].append((x,k)) #인접리스트로 저장해주기
    #x부품을 만들기 위해 y부품 k개가 필요하다
    #가중치 k는 위상 정렬 주에서 누적 계산할 때 반드시 씀

    indegree[x] += 1 
#x는 선행조건 y가 있으므로 진입차수 1추가

#3단계 : 위상정렬 시작하기
queue=deque()

#진입 차수가 0인 부품 = 기본 부품, 큐에 넣어주기
for i in range(1,n+1):
    if indegree[i]==0:
        queue.append(i)

#4단계:위상 정렬 + 부품 개수 누적 계산
while queue:
    now=queue.popleft() #맨 앞에 있는 부품 pop
    for next,cnt in adj[now]:
    # for a,b in 리스트 : 한 번에 변수 두 개로 꺼내는 문법법
    # 위에서 저장한 형태임 adj[y] 안에 (x,k)로 저장
    # y=now(진입차수가 작아서 queue에 넣었다가 pop한 부품) 
    # x=next(더 큰 부품)
    # k=cnt 필요한 작은 부품의 갯수 
        if all(needs[now][i]==0 for i in range(n+1)):
            #만약 now가 기본 부품이다
            '''
            needs[now]는 now를 만들기 위해 
            어떤 기본 부품이 얼마나 필요한지
            나타내는 리스트

            기본 부품은 다른 부품을 만들기 위해 쓰임
            자신을 위한 부품은 없음
            needs[now] 는 전부 0 이어야 기본 부품
            
            '''
            needs[next][now] += cnt
        else:
            #만약 now가 기본 부품이 아니야 그렇다면?
            #next더큰 부품을 만들기 위한 중간및 기본부품 i의 갯수는
            for i in range(1,n+1):
                needs[next][i] += needs[now][i]*cnt
        indegree[next]-=1
        if indegree[next] == 0:
            queue.append(next)

for i in range(1,n+1):
    if needs[n][i]>0:
        print(i,needs[n][i])
                

