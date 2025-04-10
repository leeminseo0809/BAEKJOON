# 그룹 단어(단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우) 개수 출력

N = int(input()) # 단어 개수 N개
group_word = N 

for i in range(N):
    S = input() # 단어 입력 받기
    for j in range(len(S)-1): 
        if S[j] == S[j+1]: # 알파벳이 연속적이면 통과
            continue
        elif S[j] in S[j+1:]:
            group_word -= 1
            break

print(group_word)

# continue : 현재 반복을 건너뛰고 다음 반복으로
# break : 반복문을 즉시 종료      
