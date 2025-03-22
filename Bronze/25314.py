N = int(input()) # 주어진 바이트 수

# long의 개수 계산
long_count = N // 4 # 4 바이트 단위로 나누기

for _ in range(long_count): 
    print("long", end=" ")
    
print("int") # 마지막에 int 출력