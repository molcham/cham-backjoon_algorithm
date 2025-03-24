from collections import deque
import sys


n=int(input())

queue=deque()

for i in range(n,0,-1):
    queue.append(i)  #아래부터 n(front) 맨 위에 1(rear)

while len(queue)>1:  # queue안에 카드가 1개 남을때 까지
    queue.pop() #맨위의 원소 버리기
    queue.appendleft(queue.pop()) #appendleft 새로운 요소를 왼쪽(큐의 앞부분)에 추가하기 (그다음 출력)
    #queue.pop()은 제일 위에 있는 원소를 뽑아서!! =>appendleft하기
print(queue[0])