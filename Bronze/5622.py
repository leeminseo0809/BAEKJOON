# 숫자를 누르기 위해서는 기본적으로 1초 + 해당 숫자만큼
# 다이얼을 걸기 위해 필요한 최소 시간을 출력

dial_groups = [
    'ABC', 'DEF', 'GHI', 'JKL',
    'MNO', 'PQRS', 'TUV', 'WXYZ'
]

dial_map = {}

# enumerate() : 리스트를 반복할 때 인덱스와 값을 같이 꺼내주는 함수
for i, group in enumerate(dial_groups): # i: 그룹 번호 (0부터 시작), group: 알파벳 묶음
    for letter in group:
        dial_map[letter] = i + 3 

word = input() # 단어 입력 받기

total_time = 0 # 총 시간 초기화

for ch in word: # word 문자열을 하나씩 반복, ch는 반복문 안에서 매번 꺼내 쓰는 하나의 문자
    total_time += dial_map[ch]

print(total_time)