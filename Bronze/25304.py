X = int(input()) # 영수증에 적힌 총 금액 
N = int(input()) # 영수증에 적힌 구매한 물건의 종류의 수 

total = 0  # 계산된 총 금액

for _ in range(N): 
    a, b = map(int, input().split()) # N개의 줄에 각 물건의 가격 a와 개수 b개
    total += a * b  # 가격 * 개수의 곱을 총합에 더하기
    
if total == X:
    print('Yes')
else :
    print('No')