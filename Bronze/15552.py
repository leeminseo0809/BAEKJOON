#T = int(input()) 

#for _ in range(T): 
    #A, B = map(int, input().split()) 
    #print(A + B)


import sys
input = sys.stdin.readline  # 빠른 입력

T = int(input())  # 테스트 케이스 개수

output = []  # 결과를 모아서 한 번에 출력하기
for _ in range(T):
    A, B = map(int, input().split())
    output.append(str(A + B))  # 합계를 문자열로 변환하여 리스트에 저장

# 모은 결과를 한 번에 출력
sys.stdout.write("\n".join(output) + "\n")
