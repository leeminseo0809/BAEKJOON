# N : 바구니 개수
# M : 순서를 바꾸는 명령 횟수
# i부처 j까지의 바구니 순서를 역순으로 뒤집
# 순서 바꾼 뒤, 왼쪽에 있는 바구니부터 출력

N, M = map(int,input().split())
arr = list(range(1, N + 1))  # 1부터 N까지의 숫자로 초기화


for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = reversed(arr[i-1:j])

print(*arr)

