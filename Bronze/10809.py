# a, b, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력
# 어떤 알파벳이 단어에 포함되어 있지 않는 경우 -1 출력
 
S = input() # 단어 S

for ch in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(ch),end=' ')

# 문자열.find(문자) : 찾는 문자가 문자열에 처음 등장하는 위치의 인덱스를 반환함, 없으면 -1을 반환
