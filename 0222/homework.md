```
for tc in range(1, 11):
    l, p = input().split()
    stack = [] # 1 2 3 4
    for i in p: # 1 2 3 
        if not stack or i != stack[-1]:
            stack.append(i)
        else:
            stack.pop()
    print(f'#{tc} {"".join(stack)}')
```

