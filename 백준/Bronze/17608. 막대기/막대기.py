import sys
my_list=[]
count=1 # 맨앞에 있는 막대기는 무조건 보임 
n=int(sys.stdin.readline())

for i in range(n): 
    block=int(sys.stdin.readline())
    my_list.append(block)


#가장 큰 막대기를 기준으로 check해야됨
max_block=my_list[n-1]

for j in reversed(my_list):
    if j>max_block:
        max_block=j
        count+=1
print(count)