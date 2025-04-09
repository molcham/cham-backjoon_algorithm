'''
greedy 사용하기

n개의 회의
회의가 겹치지 않게 하면서 회의실을 사용할 수 있는
회의의 최대 개수

배낭 문제는 '최대 가치'
회의실 문제는 '최대 개수'
-> 짧고 일찍 끝나는 회의를 먼저 담는게 이득

회의는 한번 시작시 중간에 중단 안됨
한 회의가 끝나는 것과 동시에 다음 회의 시작 가능
시작하자마자 끝나는 회의도 가능

사용표가 배낭
회의시간이 가치...

그럼 작은 것 부터 담아야 하지 않을까


1.입력받기
2.정렬시켜주기(end 기준으로 오름차순)
3.가장 작은 원소 선택
4.순차적으로 조건에 맞는 당장의 최적해 선택
5.마지막 조건을 만나면 return 하기
6.return된 값 출력
'''

import sys 

input=sys.stdin.readline
n=int(input())
m=[list(map(int,input().split())) for _ in range (n)]
'''
m = []
for _ in range(n):
    row = list(map(int, input().split()))
    m.append(row)

'''
#map 결과를 리스트로 한 번 감싸주기
#map(...) => 값을 반복해서 넘기는 "게으른"객체
#list(map(...)) => 그 결과를 실제 리스트로 만들기
#m[i][0] 같은 인덱싱이 가능해짐

m.sort(key=lambda x:(x[1],x[0]))

count=0
end_time=0

for start,end in m: #리스트 안에 있는...
    if start>= end_time: # end_time은 처음에는 0
        count +=1
        end_time=end # 선택된 요소에서 갱신해주기

print(count) # 선택된 모든 회의 개수

