'''
최단 거리 찾기 
bfs이용해서 풀기
'''

import sys
from collections import deque


input=sys.stdin.readline
n,m,k,x=map(int,input().split()) # 첫 줄에 받기 
'''
n=도시의 개수
m=도로의 개수
k=거리의 정보
x=출발도시

1.bfs로 모든 도시의 최단거리를 구함
2.최단 거리중에 거리가 k인 것을 모두 출력함
3.만약 해당하는게 없다면 -1을 출력함 
'''


graph={i: [] for i in range(1, n+1)}
my_list=[] #이어져 있는 도시 받기 

for i in range (m):
    a,b =map(int,input().split())
    my_list.append((a,b)) #라스트 쌍 입력 받기

for a,b in my_list:
    graph.setdefault(a,[]).append(b) # 단방향 도로
    #graph.setdefault(b,[]).append(a) <= 이거까지 하면 양방향
    #graph 만들어짐, 어떤 도시에 이어져있는지

def bfs_find_distance(graph,start,k,n):
    distance=[-1]*(n+1) 
    #인덱스 번호를 도시번호와 맞추기 위해서 0번 인덱스는 안쓰고
    #-1로 초기화 한다음 n+1까지 만들어주기
    distance[start]=0

    queue=deque([start]) 
    #큐를 생성하고 start노드를 초기값으로 넣어둔다.

    while queue:
        current = queue.popleft()
        #제일 최근은 앞에있는 노드(지금 막 방문하려는 도시)
        for neighbor in graph[current]:
            #현재 도시 current의 이웃 도시들을 순회
            if distance[neighbor]==-1: #아직 방문하지 않은 도시라면
                distance[neighbor]=distance[current]+1
            #bfs는 항상 한칸씩만 이동하니까 
            #시작 도시로 부터 이렇게 하면 정확히 최단거리 구해짐
                queue.append(neighbor)
                #이웃도시를 큐에 넣어 다음에 방문할 수 있게 
                '''

                그럼 이건 이웃도시들의 거리를 +1 해주고 
                queue에 넣어서 다음번에 들릴 수 있게 해준다는 거야?
                queue.append(neighbor)
                이웃 도시를 큐에 넣어 → 다음에 방문할 수 있게 대기열에 추가

                '''

    result=[i for i in range(1,n+1) if distance[i]==k]
    return sorted(result) if result else [-1]

result=bfs_find_distance(graph,x,k,n)

for city in result:
    print(city)













