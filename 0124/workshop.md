```

def get_dict_avg(test):
    count = 0
    result = []
    for i in test.values():
        result.append(i)
        count += 1
    return sum(result)/count

	
    
print(get_dict_avg({'python' : 80, 'algorithm': 90, 'django' : 89, 'web' : 83}))
```

```
def count_blood(data):
    temp = set(data)
    result = {}
    for i in temp:
        if i in data:
            result[i] = data.count(i)
    return result

	
    
print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']))

```

