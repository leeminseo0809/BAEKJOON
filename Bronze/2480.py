A, B, C = map(int, input().split())

if A == B == C: # 같은 눈 3개
    print(10000 + A*1000)
elif A == B or A == C: # 같은 눈 2개
    print(1000 + A*100)
elif B == C:
    print(1000 + B*100)
else : # 모두 다른 눈
    print(max(A, B, C) * 100)
