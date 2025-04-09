'''
greedy 쓰는 문제 

다른 모든 지원자와 비교했을 때 성적,면접시험 중
적어도 하나가 다른 지원자보다 떨어지지 않을 때 선발

어떤 지원자 B도 A보다 서류와 면접 둘 다 더 좋은 사람은
없어야 한다.

시험 성적으로 정렬
greedy하게 서류 순서대로 한번만 보고 판단

'''
import sys

input=sys.stdin.readline

t=int(input()) #테스트 케이스
t_count=0
result=[]

while t_count<t:
    count=0
    n=int(input()) #지원자의 숫자
    emp=[]
    #사원정보 list 생성 해주기
    for i in range (n):
        doc,itv=map(int,input().split())
        emp.append([doc,itv])
    emp.sort(key=lambda x:(x[0],x[1]))
    min_itv=emp[0][1]
    for i in range(1,n):
        if emp[i][1]>min_itv:
            continue 
    #만약 앞의 사람(서류 성적이 더 높은)보다
    #면접 성적이 더 낮으면 둘다 낮은거라 탈락
        else:
            count+=1
            min_itv=emp[i][1]
    result.append(count)
    t_count+=1

for i in result:
    print(i+1)
    

#오름 차순으로 정렬하기 서류 성적 기준으로

'''


#사원정보 list 생성 해주기
for i in range (n):
    doc,itv=map(int,input().split())
    emp.append([doc,itv])

emp.sort(key=lambda x:(x[0],x[1]))
#오름 차순으로 정렬하기 서류 성적 기준으로

'''
'''
[[doc,itv]]
doc=0번째 인덱스 원소
itv=1번째 인덱스 원소

emp[i][0] : i번째 지원자의 서류 성적 
emp[i][1] : i번째 지원자의 면접 성적
'''
