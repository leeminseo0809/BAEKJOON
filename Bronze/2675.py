T = int(input()) # 테스트 케이스의 개수 T

# 문자열 S, R번 반복
for _ in range(T):
    R, S = input().split()
    R = int(R) 
    result ='' # 결과 문자열

    for ch in S: # S에 들어있는 문자들을 하나씩 꺼냄
        result += ch * R

    print(result)
