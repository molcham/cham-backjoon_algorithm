import sys
from collections import deque

visited=set()
queue=deque([1])
input=sys.stdin.readline



com=int(input()) # 컴퓨터의 수
coms=int(input()) #연결된 컴퓨터 쌍의 수

sick_list=[]
graph={}

for i in range (coms):
    a,b =map(int,input().split())
    sick_list.append((a,b)) #라스트 쌍 입력 받기

for a,b in sick_list:
    graph.setdefault(a,[]).append(b)
    graph.setdefault(b,[]).append(a)

def dfs(node,visited):
    visited.add(node)
    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            dfs(neighbor,visited)
visited=set()
dfs(1,visited)

print(len(visited)-1) #1번을 제외한 감염된 컴퓨터 수