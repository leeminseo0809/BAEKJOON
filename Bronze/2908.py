A, B = input().split()

result_A = int(A[::-1])
result_B = int(B[::-1])

if result_A > result_B:
    print(result_A)
else:
    print(result_B)

# [start:stop:step] -> stop:시작인덱스, stop:끝인덱스, step:증감값
# [::-1] : 처음부터 끝까지 거꾸로 읽음
