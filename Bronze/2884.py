H, M = map(int, input().split())

M -= 45 # 45분 일찍 일어나기

if M < 0:
    H -=1
    M += 60

if H < 0:
    H = 23

print(H,M)
