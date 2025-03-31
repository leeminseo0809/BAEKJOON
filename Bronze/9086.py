# 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자 연속하여 출력

T = int(input()) # 테스트의 개수 T

for _ in range(T):
    s = input() # 문자열 입력 받기
    print(s[0] + s[-1])