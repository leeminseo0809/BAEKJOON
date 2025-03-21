T = int(input()) # 테스트 케이스 개수 입력

for _ in range(T): # 테스트 케이스의 개수 T개, range(1, T) : 1부터 T-1까지 반복
    A, B = map(int, input().split()) # A, B 입력 받음
    print(A+B)