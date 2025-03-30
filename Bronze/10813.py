# N번 바구니에는 N번 공
# M번 공을 교환, 교환할 때마다 두 바구니 선택하여 공을 교환

N, M = map(int,input().split())

arr = list(range(1, N+1)) # 1부터 N까지의 숫자를 리스트로 초기화

for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

print(*arr) 

