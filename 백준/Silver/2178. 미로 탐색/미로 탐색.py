'''
bfs사용하기
최소의 칸 구하기 = 최단거리 탐색 ?
2차원 배열에 저장해서 푸는 문제인듯

n개의 줄 m개의 정수 
n행 m열

strip() 양쪽 끝의 공백 제거
lstrip() 왼쪽(앞쪽) 공백 제거
rstrip() 오른쪽(뒤쪽) 공백 제거

(1,1) 에서 출발해서 (n,m)까지 가기

bfs또는 dfs를 배열 위에서 사용하는 경우
거의 대부분 방향 배열을 써서 이동한다.
만약 방향 배열 안쓰면 if문으로 다 따져줘야해서 복잡



'''
from collections import deque
import sys

input=sys.stdin.readline

n,m=map(int,(input().split()))
matrix=[]

#2차원 배열에 저장하기
for i in range (n):
    row=list(map(int,input().strip())) 
    #한 줄 입력받고 리스트로 변환
    #map(int,...)으로 문자 하나하나 숫자로 바꿔 리스트로
    matrix.append(row)
    #배열로 저장해줌

dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque()
queue.append((0,0))

#BFS 시작

while queue:
    y,x=queue.popleft()
    for i in range(4): #상하좌우
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<m:
            #1인 곳만 갈 수 있고, 아직 방문하지 않은 곳
            if matrix[ny][nx]==1:
                matrix[ny][nx]=matrix[y][x]+1
                #1이면 지나가면서 +1해주기
                queue.append((ny,nx))

# 결과
if matrix[n-1][m-1] == 1:
    print(-1)  # 도착 못함
else:
    print(matrix[n-1][m-1])
    #계속 값을 갱신 1,1부터 시작했다고 했으니께...
    #근데 나는 0,0부터로 계산함












