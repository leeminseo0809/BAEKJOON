A, B = map(int, input().split())
C = int(input())

if (B + C) < 60: # 분의 합이 60 미만
    print(A, B + C)
else: # 분의 합이 60 이상 (B + C) >= 60
    add_hour = (B + C) // 60
    B = (B + C) % 60 # 분 계산
    A = A + add_hour # 시간 증가

    if A >= 24:
        A = A % 24

    print(A, B)


