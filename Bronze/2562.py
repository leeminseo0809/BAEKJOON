# 첫째 줄에 최댓값, 둘째 줄에 최댓값이 몇 번째 수인지 출력

N = [int(input()) for _ in range(9)]

max_value = max(N) # 최댓값 찾기
max_index = N.index(max_value) + 1 # 최댓값 인덱스 찾기, index() 함수는 0부터 시작하므로 1 더함

print(max_value)
print(max_index)


