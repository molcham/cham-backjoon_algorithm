import sys

#마지막 호출시 2**n을 넣어줌 

def dc(x,y,n):   # r=7 c=7 
    global cnt
    if x>r or x+n <= r or y>c or y+n <= c:  #n=16
        cnt += n**2
        return     
        '''만약 현재 n*n크기의 격자가 r,c를 포함하지 않는다면
        탐색할 필요가 없기 때문에 바로 cnt +=n**2 만큼 건너뛰기
        
        
        n=16이고 r,c=7 이면 이 식은 만족 ㄴㄴ cnt값 늘리지말고 건너뛰시오
        너무크다 이말이양...더 작은 범위로 줄여라 이거지....
        '''
    if n > 2: # n=16일때 여기 포함 
        n//=2 # 현재 탐색하는 격자의 크기를 절반으로 줄임 
        dc(x,y,n)  # 왼쪽 위 영역 탐색
        dc(x,y+n,n) # 오른쪽 위 영역 탐색
        dc(x+n,y,n) # 왼쪽 아래 영역 탐색
        dc(x+n,y+n,n) # 오른쪽 아래 영역 탐색
    else:     # n<=2 이므로 n==2일때의 조건 인거임 그니까 포함되는 격자
              # n==2 일때 격자 4개 이니까 무조건 4개중에 하나다 이거
        if x==r and y==c:
            print(cnt)
        elif x==r and y+1==c:
            print(cnt+1)
        elif x+1==r and y==c:
            print(cnt+2)
        else:
            print(cnt+3)  
        sys.exit()
        
n,r,c = map(int,input().split())  #if 4 7 7
cnt = 0
dc(0,0,2**n)    #dc(0,0,16)