cut=[]

#result=1

white_count=0
blue_count=0

def cut_paper(x,y,n):
    global result
    cut=paper[x][y]

    global white_count
    global blue_count

    if all(paper[i][j] == cut for i in range(x, x+n) for j in range(y, y+n)):
        if cut == 1:
            blue_count += 1  # 파란색 색종이 증가
        else:
            white_count += 1  # 흰색 색종이 증가
        return  # 더 이상 나눌 필요 없음

    
    #위의 for문안에 이걸 넣으면 안됨!...
    #result=result-1+4
    cut_paper(x,y,n//2)
    cut_paper(x,y+n//2,n//2)
    cut_paper(x+n//2,y,n//2)
    cut_paper(x+n//2,y+n//2,n//2)
                

            


n=int(input())
paper=[list(map(int,(input().split()))) for _ in range(n)]

cut_paper(0,0,n)

print(white_count)
print(blue_count)