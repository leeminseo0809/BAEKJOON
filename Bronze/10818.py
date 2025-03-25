# 정수 N개가 주어질 때 최솟값과 최댓값 구하기

N = int(input())
arr = list(map(int, input().split()))

# 최솟값과 최댓값 찾기
min_value = min(arr)
max_value = max(arr)

print(min_value, max_value)


