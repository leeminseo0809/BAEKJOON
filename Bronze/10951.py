import sys
input = sys.stdin.read # sys.stdin.read()를 사용하여 여러 줄을 한꺼번에 입력받음

data = input().strip().split('\n') # 줄바꿈을 기준으로 나눔

for line in data:
    A, B = map(int, line.split())
    print(A + B)
    

