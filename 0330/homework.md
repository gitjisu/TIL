```
import sys
sys.stdin = open('1.txt')


def pos(k):
    for i in range(k):
        if arr[k] == arr[i] or abs(arr[k] - arr[i]) == k - i:
            return False
    return True



def queen(k):
    global result
    if k == n:
        result += 1
        return
    else:
        for i in range(n):
            arr[k] = i
            if pos(k):
                queen(k + 1)


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    result = 0

    arr = [0] * n
    queen(0)
    print(f'#{tc} {result}')
```

