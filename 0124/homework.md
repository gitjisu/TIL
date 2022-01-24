```
a = 'apple'
print(a.count('a') + a.count('e'))

b = 'banana'
print(b.count('a'))
```

4번

```
list = ([32,55,63],[13,32,40,55])

def only_square_area(list):
    lst = []
    for i in list[0]:
        for j in list[1]:
            if i == j:
                lst.append(i**2)
    return lst

print(only_square_area(list))
```

