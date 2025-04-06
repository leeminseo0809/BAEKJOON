# 체스:총 16개의 피스(킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개)

chess_groups = ['킹', '퀸', '룩', '비숍', '나이트', '폰']
default_counts = [1, 1, 2, 2, 2, 8] # 정상 체스 세트 기준 개수

input_counts = list(map(int, input().split())) # 실제로 발견한 피스 개수

result = [] # 결과 계산

for default, actual in zip(default_counts, input_counts): # zip(default_counts, input_counts):두 개의 리스트를 하나로 묶어줌
    result.append(default-actual) # append() : 리스트의 맨 뒤에 새로운 값 추가

print(' '.join(map(str, result))) # ' '.join(...) : 문자열 리스트를 공백으로 이어붙여 하나의 문자열로 만듦





