def count_cycle(n):
    original = n  # 처음 입력받은 숫자 저장
    count = 0  # 사이클 횟수

    while True:
        if n < 10:  
            n = int("0" + str(n))  # 1의 자리 수일 경우 앞에 0 추가
        
        digit_sum = sum(map(int, str(n)))  # 각 자리 숫자 합 구하기
        new_number = int(str(n % 10) + str(digit_sum % 10))  # 새로운 숫자 생성
        
        count += 1  # 횟수 증가
        if new_number == original:  # 원래 숫자로 돌아오면 종료
            return count
        
        n = new_number  # n 갱신 후 다시 반복

# 입력 및 실행
n = int(input())  
print(count_cycle(n))  