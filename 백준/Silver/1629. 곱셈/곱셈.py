'''
a를 b번 곱한 수를 구하여라 (함수 안에서 구하기)

그리고 이를 c로 나눈 나머지를 구하여라 (함수 밖에서 구하기) 
=> 이러면 시간초과 !

분할정복을 활용한 거듭 제곱 계산

(a*b) % c 
= [(a%c)*(b%c)]%c
'''

def power(a,b,c):
    if b == 0 :
        return 1
    half=power(a,b//2,c)
    if b%2==0:
        return ((half%c)*(half%c)) # b 가 짝수면 두번 곱하기
    else:
        return ((half%c)*(half%c)*a) #b가 홀수면 a 한번 더 곱해주기

a,b,c=map(int,input().split())

print(power(a,b,c)%c)


