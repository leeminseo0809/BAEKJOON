N = int(input()) # 숫자의 개수 N개
# .strip() : 문자열의 양쪽 끝에 있는 공백, 개행 문자(\n) 등을 제거
numbers = input().strip() # 공백 없이 숫자 N개

total = sum(map(int, numbers)) # map(int, numbers) : 문자열의 각 문자 -> 정수로 변환
print(total)

