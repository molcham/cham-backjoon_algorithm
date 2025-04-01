'''
트리 순회

트리 저장은 딕셔너리에 해야한다 {}에 저장장

'''
import sys

input=sys.stdin.readline

n=int(input()) #노드의 개수
tree={} # 트리구조 딕셔너리에 저장

for i in range (n):
    parent,left,right=input().split() 
    #한줄에 받고 저장하기 int로 하면안됨 없으면 . 이라서
    tree[parent]=(left,right) 
    #각 부모 노드마다 왼쪽 자식, 오른쪽 자식 붙이기

def preorder(node):
    if node =='.':
       return
    print(node,end='') #부모를 출력하는?
    preorder(tree[node][0]) #왼쪽 자식
    preorder(tree[node][1]) #오른쪽 자식

def inorder(node):
    if node =='.':
       return
    inorder(tree[node][0])
    print(node,end='')#부모를 출력하는?
    inorder(tree[node][1])
       
#이 방식은 이진 탐색 트리에서 순회를 하면 오름차순이 된다.
def postorder(node):
    if node == '.':
       return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

