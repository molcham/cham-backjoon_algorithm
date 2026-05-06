import math

def solution(signals):
    # 각 신호등의 주기 계산
    cycles = []
    for signal in signals:
        cycles.append(sum(signal))

    # 전체 패턴이 반복되는 최소공배수 계산
    lcm = 1
    for cycle in cycles:
        lcm = lcm * cycle // math.gcd(lcm, cycle)

    # 1초부터 최소공배수 시각까지 확인
    for t in range(1, lcm + 1):
        all_yellow = True

        for i in range(len(signals)):   # 인덱스로 하나씩 접근
            g = signals[i][0]           # 초록 시간
            y = signals[i][1]           # 노랑 시간
            r = signals[i][2]           # 빨강 시간
            cycle = cycles[i]           # 위에서 미리 계산한 주기 가져오기

            pos = (t - 1) % cycle + 1  # 0이 안나오게 하기 위한 계산 방법

            # 현재 시각이 노란불 구간이 아니면 실패
            if not (g + 1 <= pos <= g + y):
                all_yellow = False
                break

        # 모든 신호등이 노란불이면 즉시 반환
        if all_yellow:
            return t

    return -1