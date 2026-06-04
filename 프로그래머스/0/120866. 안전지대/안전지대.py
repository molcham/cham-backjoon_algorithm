def solution(board):
    
    #board 는 n*n 배열 0과 1로 이루어진 2차원 배열 
    
    n = len(board)
    danger = [[0] * n for _ in range(n)]
    
    # 방향 배열 생성 
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 1. board 전체를 돌면서 지뢰 찾기
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger[i][j] = 1
                
    # 2. 지뢰를 찾으면 danger에 지뢰 칸 + 주변 8칸 표시하기
                
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n:
                        danger[nx][ny] = 1

    # 3. danger에서 0인 칸 개수 세기
    
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                answer += 1
                
    return answer