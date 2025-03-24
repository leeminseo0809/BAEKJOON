# 오른쪽 정렬로 별 찍기

# print문으로 출력 : 왼쪽 정렬
# 오른쪽 정렬 : rjust(전체자리수)

N = int(input()) # 별의 줄 수 입력

for i in range(1, N+1):
    print(str("*" * i).rjust(N))
