# 크로아티아 알파벳 개수 새기

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input() # 사용자가 입력한 문자열 받음

for i in alphabet:
# alphabet 리스트를 순회하면서 S 문자열 안에 있는 각 크로아티아 알파벳 조합(i)을 찾아서 '*' 하나로 바꿈
    S = S.replace(i, '*')
print(len(S))
