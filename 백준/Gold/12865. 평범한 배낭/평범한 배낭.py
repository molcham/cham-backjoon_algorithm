'''
dp 사용하는 문제

0-1 배낭 

물건의 무게 K
해당 물건의 가치 V

'''
import sys

input=sys.stdin.readline
n,k=map(int,input().split())
# n=물품의 수,k=준서가 버틸 수 있는 무게
items=[[0,0]]
'''
여기서 i는 1부터 시작해. 그러면 items[1], items[2]...를 참조하게 돼.

그래서 items[0]은 무시된다는 전제가 있어야 해.
그 말은 → items[0]은 더미(dummy) 값으로 넣어놔야 해!

'''

#무게,가치 입력 받기
for i in range(1,n+1):
    w,v=map(int,input().split()) 
    items.append([w,v])

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1): #물품의 수
    for j in range(1,k+1): #준서가 버틸 수 있는 배낭무게
        weight,value=items[i] 
    #각 인덱스에 있는 요소 할당
        if j<weight:
            dp[i][j]=dp[i-1][j] 
            # 그 i번째 물건은 못담아연
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)
    #j-weight 물건을 넣었기 때문에 최대 넣을 수 있는 무게 줄어든다

print(dp[n][k])


