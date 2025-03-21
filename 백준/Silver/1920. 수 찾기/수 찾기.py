'''

첫번째 줄 :몇개 숫자 입력할지 N
두번째 줄 : 첫번째 줄에서 입력받은 숫자갯수 만큼 수 배열 입력 N개 
세번째 줄 : 몇개 숫자 입력해서 검사받을지 M
네번째 줄 : 검사받을 숫자 배열 M개 

이분 탐색 : 반으로 계속해서 쪼개나가면서 찾는 수가 있는지 check하는 방법 
찾는 과정에서 ?....

그냥 리스트에서 비교하는게 나을 것 같기도..?

각 인덱스가 일치하는지 비교하는게 아니라..각 인덱스에 있는 숫자가 n_list에 존재하는지 아닌지 check


4 1 5 2 3

1 3 7 9 5

for문으로 풀면 시간초과 나옴 이런...

이분탐색으로 구현해야한다.


'''
# 숫자 차례대로 정렬을 해준 상태임 그렇기 때문에 의미가 있음

def binary_search(arr,target):

    left,right=0,len(arr)-1 #인덱스 설정
    
    while left<=right:  
    #부호 설정해주는 것도 매우 중요함 마지막 한개의 요소도 검사할 수 있도록 하기위함
        mid=(left+right) // 2
        
        if arr[mid]==target:
            return True
        elif arr[mid]<=target:
            left=mid+1
        else:
            right=mid-1
    return False
            


n=int(input())
n_list=sorted(map(int,(input().split())))

m=int(input())
m_list=list(map(int,(input().split())))

for target in m_list:
    if binary_search(n_list,target):
        print(1)
    else:
        print(0)





'''
for i in range (n):
    if m_list[i] in n_list:
        print(1)
    else:
        print(0)

'''











    



