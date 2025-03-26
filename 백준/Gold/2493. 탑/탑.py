import sys
input = sys.stdin.readline

n=int(input())

towers=list(map(int,input().split())) #list로 생성해주기

stack=[]
result=[0]*n

for i in range(n): # 1번 부터 n번 탑까지 탐색
    while stack:
        if towers[i]>towers[stack[-1]]:
            #만약 내가검사하는 타워가 stack에 있는 타워보다 크다면
            stack.pop()
        else:
            #만약 내가검사하는 타워가 stack에 있는 타워보다 작거나..
            #스택이 비어서 더 이상 확인할 탑이 없다?
            #result에 나보다 큰 탑의 towers에 있는 인덱스 넣어주기
            result[i]=stack[-1]+1 
            #stack은 인덱스 값이니까 +1해서 몇번째 탑인지 저장 
            break
    stack.append(i)

print(*result) 