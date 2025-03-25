# 정수 N개로 이루어진 수열 A와 정수 X가 주어질 때 X 보다 작은 수를 모두 출력

N, X = map(int, input().split())
A = list(map(int, input().split())) # 수열 A를 이루는 정수 N개

# X보다 작은 수를 필터링하여 공백으로 구분하여 출력
result = [str(num) for num in A if num < X] # X보다 작은 수를 필터링
print(" ".join(result)) # join() 함수를 사용하여 공백으로 구분하여 출력
