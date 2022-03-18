```
def post_order(t):
    if 0 < t <= N:
        post_order(ch1[t])
        post_order(ch2[t])
        cal.append(tree[t])
 
def calculator(num1,num2,x):
    if x == '+':
        return num1 + num2
    elif x == '-':
        return num1 - num2
    elif x == '*':
        return num1 * num2
    elif x == '/':
        return num1 / num2
 
for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    cal = []
    for i in range(N):
        lst = list(input().split())
        if lst[1].isdigit():
            tree[int(lst[0])] = int(lst[1])
        else:
            tree[int(lst[0])] = lst[1]
            ch1[int(lst[0])] = int(lst[2])
            ch2[int(lst[0])] = int(lst[3])
    post_order(1)
 
    stack = []
    for num in cal:
        if type(num) != int:
            b = stack.pop()
            a = stack.pop()
            c = calculator(a, b, num)
            stack.append(c)
        else:
            stack.append(num)
    answer = int(stack.pop())
 
    print(f'#{tc} {answer}')
```

