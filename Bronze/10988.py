# 단어가 주어졌을 때, 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 지 확인

S = input()

if S == S[::-1]: # S[start:stop:step]
    print(1)
else:
    print(0)