```
import sys
sys.stdin = open('1210.txt')

T = 10
for tc in range(1, 11):
    case = int(input()) #
    arr = [list(map(int, input().split()))for _ in range(100)]

    for n in range(100):
        if arr[99][n] == 2:
            x = n # n이 2인 값을 찾아 x에 저장
            break
    y = 99
    while True:
        if x < 99 and arr[y][x+1] == 1: # 오른쪽으로 가기 위해 조건문 작성
            while x<99 and arr[y][x+1] == 1: # 만약 오른쪽이 1이면 계속 이동 반복
                x += 1
            else:
                y -= 1
        elif x > 0 and arr[y][x-1]: # 왼쪽으로 가기 위해 조건문 작성
            while x > 0 and arr[y][x-1]: #만약 왼쪽이 1이면 계속 이동 반복
                x -= 1
            else:
                y -= 1
        else:
            y -= 1
        if y == 0:
            break

    print(f'#{tc} {x}')




```

