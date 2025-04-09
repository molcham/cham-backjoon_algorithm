'''
dp를 사용해서 푸는 문제

상향식으로 풀기-테이블 생성하기

'''
import sys

a=input().strip()
b=input().strip()

n,m=len(a),len(b) #문자열의 길이

dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]: #맨 뒷자리 수가 same
            dp[i][j]=dp[i-1][j-1]+1
            #하나씩 줄인다음 공통 수열 길이 +1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])
#마지막칸이 최종 정답이다. 
#작은 문제부터 차근차근 테이블을 채워간다.
