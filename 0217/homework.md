```
import sys
sys.stdin = open('1.txt')

for tc in range(1, 11):
    test_num = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    max_palindrome = 0
    for i in range(len(arr)):   # 0~99
        for j in range(len(arr), 0, -1):
            for k in range(len(arr)-j+1):
                if arr[i][k:k+j] == arr[i][k:k+j][::-1]:
                    if max_palindrome < len(arr[k:k+j]):
                        max_palindrome = len(arr[k:k+j])


    column = []
    for i in range(len(arr)):
        cnt = ''
        for j in range(len(arr)):
            cnt += arr[j][i]
        column.append(cnt)
    # column = list(zip(*arr))

    for i in range(len(column)):  # 0~99
        for j in range(len(column), 0, -1):
            for k in range(len(column) - j + 1):
                if column[i][k:k + j] == column[i][k:k + j][::-1]:
                    if max_palindrome < len(column[k:k + j]):
                        max_palindrome = len(column[k:k + j])

    print(max_palindrome)
    
```

