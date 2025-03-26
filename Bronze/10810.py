N, M = map(int,input().split())
arr = [0] * N # 바구니를 0으로 초기화

for _ in range(M):
    i, j, k = map(int, input().split())
    # i번 바구니부터 j번 바구니까지 k 번호의 공 넣기
    for idx in range(i - 1, j):  # 인덱스를 맞추기 위해 -1 (리스트 인덱스는 0부터 시작하는데 바구니 번호는 1부터 시작하므로)
        arr[idx] = k


print(*arr) # 리스트의 요소를 하나씩 꺼내서 print() 함수의 인자로 넘겨 줌

