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

```
def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

def merge(left, right):
    global cnt

    result = [0]*(len(left)+len(right))
    left_i = right_i = i = 0
    if left[-1] > right[-1]:
        cnt += 1

    while len(left) > left_i or len(right) > right_i:
        if len(left) > left_i and len(right) > right_i:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1

        elif len(left) > left_i:
            result[i] = left[left_i]
            i += 1
            left_i += 1

        elif len(right) > right_i:
            result[i] = right[right_i]
            i += 1
            right_i += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    data = merge_sort(lst)
    print(f'#{tc} {data[N//2]} {cnt}')def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)

def merge(left, right):
    global cnt

    result = [0]*(len(left)+len(right))
    left_i = right_i = i = 0
    if left[-1] > right[-1]:
        cnt += 1

    while len(left) > left_i or len(right) > right_i:
        if len(left) > left_i and len(right) > right_i:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1

        elif len(left) > left_i:
            result[i] = left[left_i]
            i += 1
            left_i += 1

        elif len(right) > right_i:
            result[i] = right[right_i]
            i += 1
            right_i += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    data = merge_sort(lst)
    print(f'#{tc} {data[N//2]} {cnt}'
```

