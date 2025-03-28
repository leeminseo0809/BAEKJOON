# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지 구하기
# 그 다음 서로 다른 값이 몇 개 있는지 출력

N = 10 # 수 10개
arr = [] # 나머지 값을 저장할 리스트

for _ in range(N):
    num = int(input())
    remainder = num % 42
    arr.append(remainder) # append() : 리스트에 새로운 요소 추가할 때 사용하는 메서드

print(len(set(arr))) # set : 집합 자료형, 중복 허용하지 않고 순서 없는 데이터 구조

