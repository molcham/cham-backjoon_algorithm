import bisect
import sys

n=int(sys.stdin.readline())
liquid_list=list(map(int,sys.stdin.readline().split()))

def find_liquid(arr):
    arr.sort()
    closet_sum=float('inf')  # 최소합을 무한대로 초기화 
    #만약 초기값을 0으로 하면 어떤값도 작을 수가 없다!
    reult=(0,0)

    for i in range(len(arr)):
        target =-arr[i]  #합이 0인게 제일 최적의 용액 서로 부호만 반대
        #들어갈 수 있는 가장 왼쪽 인덱스 반환
        idx=bisect.bisect_left(arr,target,i+1) # i를 기준으로 그 이후부터!
        #이진 탐색으로 위치 찾기

        for j in [idx-1,idx]: #현재 위치와 왼쪽 값 비교 (더 작을수도)
            if i<j<len(arr):
                mix=arr[i]+arr[j] #j 안에서 찾은 용액값
                if abs(mix)<abs(closet_sum): #절댓값으로 비교
                    closet_sum=mix
                    result=(arr[i],arr[j])
    return sorted(result)

print(*find_liquid(liquid_list))