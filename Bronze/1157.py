# 가장 많이 사용된 알파벳 대문자로 출력, 여러 개 존재하는 경우 ? 출력

S = input().strip().lower() # 소문자로

count_dict = {}

for char in S: # 알파벳 개수 세기
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

max_freq = max(count_dict.values()) # count_dict.values() → 딕셔너리의 값들만 뽑아옴

most_common = [k for k, v in count_dict.items() if v == max_freq] # k : 알파벳, v : 등장 횟수

if len(most_common) > 1:
    print('?')
else:
    print(most_common[0].upper())
