```

get_dict_avg = {'python' : 80, 'algorithm': 90, 'django' : 89, 'web' : 83}

def avg(get_dict_avg):
    sub = get_dict_avg.keys()
    score = sum(get_dict_avg.values())
    return score/len(sub)

print(avg(get_dict_avg))

```

```
blood = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']


def count_blood(blood):
    dict = {}
    cnt_a = cnt_b = cnt_o = cnt_ab = 0
    for i in blood:
        if i == 'A':
            cnt_a += 1
        elif i == 'B':
            cnt_b += 1
        elif i == 'O':
            cnt_o += 1
        else:
            cnt_ab += 1
    dict = {'A': cnt_a, 'B':cnt_b, 'O':cnt_o, 'AB':cnt_ab}        
    return dict

print(count_blood(blood))

```

