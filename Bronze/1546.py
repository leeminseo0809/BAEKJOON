N = int(input()) # 시험 본 과목의 개수
scores = list(map(int, input().split())) # 현재 성적을 리스트로

M = max(scores) # 점수 중 최댓값 : M

new_scores = [(score / M) * 100 for score in scores] # List Comprehension
new_avg = sum(new_scores) / N # 새로운 평균 계산

print(new_avg)


