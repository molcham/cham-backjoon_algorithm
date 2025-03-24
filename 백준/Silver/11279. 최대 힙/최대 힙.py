import sys
import heapq

pq=[]
n=int(sys.stdin.readline())


for i in range(n):
    command=int(sys.stdin.readline()) #입력 받기
    if command>0:
        heapq.heappush(pq,(-command))
    else:
        if len(pq)==0:
            print(0)
        else:
            print(-heapq.heappop(pq))