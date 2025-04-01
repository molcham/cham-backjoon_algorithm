'''
BFS를 사용하는 문제 큐를 사용해야함

만약 1인 토마토를 발견한다면 
위 아래 왼 오 앞 뒤를 탐색하면서 0인 토마토가 있으면 1로 바꿔주기

-1이면 건너뛰기 

아마도...에 3차원배열 행렬에 저장해야 하지 않을까?
7576(그냥 토마토)
i,j,k

0부터 시작해서 1,2,3,4....

'''

from collections import deque
import sys

input=sys.stdin.readline

m,n,h=map(int,input().split())
#전체 구조는 h*n*m의 3차원 배열
#열,행,층

matrix=[]
for _ in range(h):
    layer=[list(map(int,input().split())) for _ in range(n)]
    matrix.append(layer)

#각 층에 대해 n줄씩 입력을 받아서 2차원배열로 만들고
#matrix라는 3차원 배열에 추가
#즉, `matrix[z][y][x]`로 접근할 수 있는 
# **3차원 공간**이 생성됨!

#6방향 :좌우상하위아래
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

#먼저 배열에서 1인 위치들을 큐에 넣기
queue=deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if matrix[z][y][x]==1:
                queue.append((z,y,x))

#BFS 시작
#맨 처음에는 1인 위치에 있는append해놓은 것부터
while queue:
    z,y,x=queue.popleft()
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        #내가 처음에 입력받은 범위 안에 있는지 
        if 0<=nz<h and 0<=ny<n and 0<=nx<m:
            #만약 범위안에 있는 한 위치가 0이라면면
            if matrix[nz][ny][nx] == 0:
                matrix[nz][ny][nx] =matrix[z][y][x] + 1
                #1로 갱신해주기,bfs도는중이니까
                queue.append((nz,ny,nx))
                #1로 변한건 큐에 넣어두고 
                #while문으로 계속 탐색
'''
마지막 몇일 걸렸는지 결과 분석
bfs를 돌면서 0에서부터 시작해서 다 돌때까지 
계속해서 갱신해감
matrix[nz][ny][nx] =matrix[z][y][x] + 1
위와같이 해줘야함 
그냥 1로 갱신해주면 몇일 걸렸는지 확인 불가능 

'''
days =0 
for z in range(h):
    for y in range(n):
        for x in range(m):
            if matrix[z][y][x]==0:
                print(-1)
                #안익은 토마토가 있는거임
                exit()
            days = max(days,matrix[z][y][x])

print(days-1) #1부터 시작했으니까 -1 해줘야됨

                







