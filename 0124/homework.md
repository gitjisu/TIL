```
def count_vowels(string):
    total = 0
    vowel = ['a','e','i','o','u']
    for i in vowel:
        total += string.count(i)
    return total

print(count_vowels('apple'))
print(count_vowels('banana'))
```

4번

```
def only_square_area(list):
    lst = []
    for i in list[0]:
        if i in list[1]:
            lst.append(i**2)
    return lst

print(only_square_area(([32,55,63],[13,32,40,55])))
```

