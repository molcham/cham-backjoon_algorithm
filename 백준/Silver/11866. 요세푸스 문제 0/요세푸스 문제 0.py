from collections import deque
import sys



#print(*queue)

def circle(arr,k):
    arr=list(arr)
    result=[] #선택된 k번째 저장할 리스트
    now=0
    while len(arr)>0:
        now=(now+(k-1))%len(arr)
        p=arr.pop(now)
        result.append(p)
    return result

n,k=map(int,(sys.stdin.readline().split()))

queue=deque(range(1,n+1)) # 1부터 n까지 채운 deque 생성


print("<" + ", ".join(map(str, circle(queue, k))) + ">")