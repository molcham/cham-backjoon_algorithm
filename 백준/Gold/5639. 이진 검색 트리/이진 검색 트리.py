import sys
input = sys.stdin.readline

# 입력 받기
preorder = [int(line.strip()) for line in sys.stdin if line.strip()]

# 예외 처리
if not preorder:
    exit()

# 1. 이진 탐색 트리 구성 (비재귀 방식)
tree = {'val': preorder[0], 'left': None, 'right': None}

def insert(tree, value):
    current = tree
    while True:
        if value < current['val']:
            if current['left'] is None:
                current['left'] = {'val': value, 'left': None, 'right': None}
                return
            else:
                current = current['left']
        else:
            if current['right'] is None:
                current['right'] = {'val': value, 'left': None, 'right': None}
                return
            else:
                current = current['right']

# 트리에 값들 삽입
for val in preorder[1:]:
    insert(tree, val)

# 2. 후위 순회 (postorder, 스택 사용)
def postorder_iterative(root):
    if root is None:
        return

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node['val'])

        # 왼쪽을 먼저 넣으면 오른쪽이 먼저 처리되기 때문에,
        # 후위 순회를 만들기 위해 오른쪽 먼저 넣기
        if node['left']:
            stack.append(node['left'])
        if node['right']:
            stack.append(node['right'])

    # 후위 순회는 루트가 마지막에 출력되므로 뒤집어서 출력
    for val in reversed(result):
        print(val)

# 후위 순회 결과 출력
postorder_iterative(tree)
