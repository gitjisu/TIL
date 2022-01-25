```
def duplicated_letter(letters):
    dup = []
    lst = list(map(str,letters))
    for i in lst:
        a = []
        for j in lst:
            if j == i:
                a.append(j)
        if len(a) > 1 :
            if i not in dup:
                dup.append(i)
    return dup




print(duplicated_letter('apple'))
print(duplicated_letter('banana'))
```



```:
def low_and_up(lowup):
	words_list = lowup.split()
	new_list = []
	for word in words_list: # b a n a n a
		new_words = " "
		for i in range(len(word)):
			if i % 2 == 0:
				new_words += word[i].lower()
			else :
				new_words += word[i].upper()
		new_list.append(new_words)
	return " ".join(new_list)
    
print(low_and_up('apple'))
print(low_and_up('banana'))
```



```
def lonely(num):
    result = []
    for i in num: # 1 1 3 3 0 1 1
        if len(result) != 0:
            if i == result[-1]:
                pass
            else:
                result.append(i)
        else:
            result.append(i)
    return result


                    
print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
```

