# 입력 받은 그대로 출력

while True: # 무한 반복으로 계속 입력을 받음
    try:
        line = input() # 한 줄씩 입력을 받음
        print(line) # 입력된 줄을 그대로 출력
    except EOFError:
        break


