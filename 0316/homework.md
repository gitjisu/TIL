```python
import sys
sys.stdin = open('중위순회.txt')

def in_order(t):
    if t:
        in_order(ch1[t])
        print(tree[t], end='')
        in_order(ch2[t])

for idx in range(1, 11):
    N = int(input())

    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    for i in range(1, N+1):
        data = input().split()
        tree[i] = data[1]

        try:
            ch1[i] = int(data[2])
            ch2[i] = int(data[3])
        except IndexError:
            continue

    print(f'#{idx} ', end='')
    in_order(1)
    print()
```

