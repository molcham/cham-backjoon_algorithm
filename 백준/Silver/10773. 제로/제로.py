k=int(input())

my_list=[]

for i in range(k):
    money=int(input())
    if money!=0:
        my_list.append(money)
    else:
        my_list.pop()
total=sum(my_list)

print(total)