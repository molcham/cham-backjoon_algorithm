'''
greedy 사용하는 문제

숫자 중간에 괄호를 쓰면 안됨
하나의 숫자를 단위로 괄호 처리 해줘야함

뺄셈 뒤에있는에 모두 묶어버리기

list에 저장하고 원소 검사로 돌린다음
- 가 나오면 빼기!!! 
'''

import sys
input=sys.stdin.readline

sample_list=input().strip() #문자열로 바로 받아서 split
parts=sample_list.split('-')

jun_list=[]


#jun_list=[int(x) if x.isdigit() else x for x in sample_list]

'''
1.for x in sample_list
=> 샘플 리스트 안의 각 요소 x르 하나씩 꺼내서 처리

2.if x.isdigit() else x:
=> x가 숫자로만 이루어진 문자열이면(x.isdigit()이 True면),
=> int(x)로 정수형으로 반환하고,
=> 아니라면 그냥 원래 값인 x를 그대로 사용한다.

3. ...for x in data 
=> 이렇게 조건을 적용한 결과들을 모아서 새로운 리스트 생성

'''
for i,part in enumerate(parts):
    numbers=list(map(int,part.split('+')))
    # + 를 기준으로 int형으로 나눠서 numbers에 넣기
    if i == 0:
        jun_list.append(sum(numbers))
        #첫번째 숫자면 그냥 더해주기
    else:
        jun_list.append(-sum(numbers))
        #나머지 그룹(-기준 나눈거)의 숫자이면 더한다음 앞에 -로
print(sum(jun_list))


