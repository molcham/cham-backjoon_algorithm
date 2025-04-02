'''
최소 신장 트리 구하기

mst: 최소 신장 트리(MST)
가중치가 있는 무방향 그래프에서 모든 정점을 연결하되,
간선의 가중치의 합이 최소가 되는 트리 구조

크루스칼 or 프림 알고리즘

'''

import sys
import heapq #이거 deque랑 다름 최소힙임 애초에 
input=sys.stdin.readline

v,e=map(int,input().split())
#v:정점의 개수, e:간선의 개수
adj = [[] for _ in range (v+1)]
for i in range (e): # 간선의 개수만큼 입력받기
    a,b,c=map(int,input().split())
    adj[a].append((c,b)) # 비용,도착 정점
    adj[b].append((c,a)) #무방향이니까 양쪽 다 연결

'''
adj = [
    [],  # index 0은 사용 안 함 (정점 1부터 시작)
    정점1[(1, 2), (3, 3)],  # 정점 1: 2번 정점(비용 1), 3번 정점(비용 3)
    정점2[(1, 1), (2, 3)],  # 정점 2: 1번 정점(비용 1), 3번 정점(비용 2)
    정점3[(3, 1), (2, 2)]   # 정점 3: 1번 정점(비용 3), 2번 정점(비용 2)
]

왜 이렇게 저장 했냐면?
prim 알고리즘에서 정점 1부터 시작
adj[1]을 보면 1번 정점과 연결된 
모든 정점을 바로 알 수 있음

그래서 최소 힙에 adj[u]에서 (비용,정점)을 넣고 
=> 최소 간선부터 하나씩 선택하는 구조이다.
'''

#prim 알고리즘 시작
visited = [False] * (v+1) #초기화 시켜주기 아직 다 방문 안함
min_heap=[] #최소힙 생성, 우선순위 큐의 역할
#현재 mst에 연결 가능한 간선들 중에서
#가장 비용이 적은 것 부터 고르기 위해 사용
#heapq를 통해 저장해줌 push/pop으로!

#최소신장트리에 포함된 정점 수와 총 비용
total_weight=0
count=0 #포함된 정점 수

#1번 정점부터 시작

visited[1]=True
for edge in adj[1]:
#정점 1번 adj안에는 (비용,정점)형태로 저장
    heapq.heappush(min_heap,edge) #비용,도착 정점
    #min_heap 리스트안에 우선순위큐로 저장

    '''
    왜 v-1으로 간선을 계산하는지 궁금했음
    e: 입력으로 주어진 전체 간선 수(모든 후보 간선)
    count: 최소 신장 트리에 실제로 선택된 간선 수
    이 조건을 주지 않으면 mst가 완성됐는데도 쓸데없이 더 고를수도
    트리는 항상 (정점 수-1)개의 간선만 필요하다!
    '''
while min_heap and count < v-1:

    #prim 알고리즘에서 
    #최소 신장트리를 정확하게 언제 멈출지
    cost,node = heapq.heappop(min_heap) 
    #(비용,정점)의 형태
    #node는 정점

    if visited[node]: #이미 방문한 정점이면 건너뛰기
    #prim은 사이클이 생기면 안됨
        continue
    visited[node]=True 
    #만약 아직 방문안한 곳이면 mst에 포함 : True
    total_weight +=cost #정점의 비용 추가
    count +=1

    for edge in adj[node]: #새로운 정점
        if not visited[edge[1]]: 
        #만약 정점이 아직mst에 포함안됨?
        #edge[0]=비용,edge[1]=정점
            heapq.heappush(min_heap,edge)
        #해당 간선을 heap에 추가해서 
        #다음에 우선순위 큐에서 가장 비용이 작은간선
print(total_weight)

    
