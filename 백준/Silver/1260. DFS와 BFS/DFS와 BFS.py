'''

'''
import sys
from collections import deque

input=sys.stdin.readline


def dfs(node,visited,path):
    visited.add(node)
    path.append(node)
    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            dfs(neighbor,visited,path)
    return path
visited_dfs=set()
path_dfs=[]
#path_bfs=[]
#visited_bfs=[]


#queue를 사용해서 구현한다.
def bfs(graph,start):
    visited={start}
    que=deque([start])

    while que:
        v=que.popleft()
        print(v,end=' ')
        for u in graph.get(v,[]):
            if u not in visited:
                visited.add(u)
                que.append(u)


n,m,v =map(int,input().split())

my_list=[]
graph={i: [] for i in range(1, n+1)}

for i in range (m):
    a,b =map(int,input().split())
    my_list.append((a,b)) #라스트 쌍 입력 받기

for a,b in my_list:
    graph.setdefault(a,[]).append(b)
    graph.setdefault(b,[]).append(a)

# 이웃 노드 정렬 (작은 수부터 방문하도록)
for key in graph:
    graph[key].sort()


print(*dfs(v,visited_dfs,path_dfs))
bfs(graph,v)










