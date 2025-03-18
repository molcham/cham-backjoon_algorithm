x,y,w,h=(input().split()) #input() 은 항상 문자열로 입력받음


x=int(x)
y=int(y)
w=int(w)
h=int(h)

if (x<=(w/2)) and (y>(h/2)):
    print(int(min(x,h-y)))
elif (x>(w/2)) and (y>(h/2)):
    print(int(min(w-x,h-y)))
elif (x<=(w/2)) and (y<(h/2)):
    print(int(min(x,y)))
elif (x>(w/2)) and (y<(h/2)):
    print(int(min(w-x,y)))
else:
    print(int(min(w/2,h/2)))




