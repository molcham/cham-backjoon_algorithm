'''
스택

menu =select_menu()
        if menu == Menu.push:
            x=int

몇번 입력받을지는 함수 밖에서 받기

import sys 써주기
input() 은 한 줄을 입력받을 때 sys.stdin을 내부적으로 호출하지만,
sys.stdin.readline() 은 여러줄 입력받을 때 유리하다.

'''

#from enum import Enum
#from collections import deque

import sys
my_stack= []
n=int(input())

for i in range(n):
    command=sys.stdin.readline().split() # 여기서 입력받기 command

    if command[0]=='push':
        my_stack.append(command[1])
    elif command[0]=='pop':
        if len(my_stack)==0: #list에는 empty 속성이 존재하지 않음
            print(-1)
        else :
            print(my_stack.pop())
            #print(x)
    elif command[0]=='top':
        if len(my_stack)==0:
            print(-1)
        else:
            print(my_stack[-1])
    elif command[0]=='empty':
        if len(my_stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] =='size':
        print(len(my_stack))
    








        
        




            





    

    
    