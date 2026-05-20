# 처음에는 이중 for문으로 접근함
# 하지만 이미 점이 4개로 고정, 가능한 조합도 고정되어 있다.

def solution(dots):
    if parallel(dots[0], dots[1], dots[2], dots[3]):
        return 1

    if parallel(dots[0], dots[2], dots[1], dots[3]):
        return 1

    if parallel(dots[0], dots[3], dots[1], dots[2]):
        return 1

    return 0


def parallel(p1, p2, p3, p4):
    return (p2[1] - p1[1]) * (p4[0] - p3[0]) == \
           (p4[1] - p3[1]) * (p2[0] - p1[0])