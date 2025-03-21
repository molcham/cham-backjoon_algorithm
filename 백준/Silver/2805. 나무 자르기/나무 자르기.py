def geun_searh(arr,target):
    left,right=0,max(arr) #초기 인덱스 설정
    #아예 max값을 리스트의 최댓값으로 설정

    while left<=right:
        mid=(left+right) // 2
        total=sum((x - mid) for x in arr if (x-mid) > 0 )

        if total >= target:
            result = mid
            left=mid+1
        else:
            right=mid-1
    return result


n,m=map(int,input().split())
tree_list=list(map(int,input().split()))

print(geun_searh(tree_list,m))