N = int(input())
arr = list(map(int, input().split())) # 공백으로 구분된 정수 목록 입력
v = int(input()) # 찾으려는 정수 입력

# 리스트에서 v 개수 세기
count = arr.count(v)

print(count)
