# 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것
# 2번째 줄에선 그 다음 출석번호를 출력

N = 30 # 전체 학생 30명
arr = [0] * N # 모든 학생 번호 0으로 초기화

for _ in range(28): # 28명의 출석번호 입력받기
    num = int(input()) # 출석한 학생 번호 입력
    arr[num-1] = 1 # 파이썬 리스트의 인덱스는 0부터 시작 but 학생 번호는 1부터

# 제출하지 않은 학생 번호 찾기
not_submit = []
for i in range(N):
    if arr[i] == 0:
        not_submit.append(i+1)

print(not_submit[0])
print(not_submit[1])
    