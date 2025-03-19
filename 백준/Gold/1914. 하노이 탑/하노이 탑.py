def hanoi(n,fr,tmp,to):
    if (n==1):
        print(fr,to)
        return
    hanoi(n-1,fr,to,tmp)
    print(fr,to)  
    hanoi(n-1,tmp,fr,to) 
k=int(input())
print((2**k)-1)

if k<=20:
 hanoi(k,1,2,3)