# def sum_list(numbers):
#     total = 0
#     for i in numbers:
#         total += sum(i)
#     return total

# print(sum_list([[1, 4], [10, 5], [20, 30]]))

# def sum_list_index(numbers):
#     total = 0
#     for i in range(len(numbers)):
#         total += sum(numbers[i])
#     return total

# print(sum_list_index([[1, 4], [10, 5], [20, 30]]))    

# def sum_list_while(numbers):
#     total = 0
#     i = 0
#     while i < len(numbers):
#         total += sum(numbers[i])
#         i += 1
#     return total    
    
# print(sum_list_while([[1, 4], [10, 5], [20, 30]]))  




# students = [
#  [100, 80, 100],
#  [90, 90, 60],
#  [80, 80, 80]
# ]


# for i in students:
#     total = 0
#     for j in i:
#         total += j
#     print(total)

# k = 0
# m = 0
# e = 0
# for i in students:
#     k += i[0]
#     m += i[1]
#     e += i[2]
# print(k)
# print(m)
# print(e)


# from re import A


# def my_find(text, alphabet):
#     a =[]
#     if alphabet in text:
#         for i in range(0, len(text)):
#             if alphabet == text[i]:
#                 a.append(i)
#         return a
#     else:
#         return -1
# print(my_find('apple', 'a'))
# print(my_find('a', 'p'))


# def check(n,student):
#     students = []
#     for i in range(1,n+1):
#         students.append(i)
    
#     here = list(map(int,student.split()))
#     for i in here:
#         if i in students:
#             students.remove(i)
#     students = list(map(str,students))
#     return ' '.join(students)
    

    

# print(check(7, '1 3 5')) # 2 4 6 7


# def duplicated_letter(letters):
#     dup = []
#     lst = list(map(str,letters))
#     for i in lst:
#         a = []
#         for j in lst:
#             if j == i:
#                 a.append(j)
#         if len(a) > 1 :
#             if i not in dup:
#                 dup.append(i)
#     return dup




# print(duplicated_letter('apple'))
# print(duplicated_letter('banana'))


# def low_and_up(lowup):
# 	words_list = lowup.split()
# 	new_list = []
# 	for word in words_list: # b a n a n a
# 		new_words = " "
# 		for i in range(len(word)):
# 			if i % 2 == 0:
# 				new_words += word[i].lower()
# 			else :
# 				new_words += word[i].upper()
# 		new_list.append(new_words)
# 	return " ".join(new_list)

# print(low_and_up('apple'))
# print(low_and_up('banana'))







# def lonely(num):
#     result = []
#     for i in num: # 1 1 3 3 0 1 1
#         if len(result) != 0:
#             if i == result[-1]:
#                 pass
#             else:
#                 result.append(i)
#         else:
#             result.append(i)
#     return result


                    
# print(lonely([1, 1, 3, 3, 0, 1, 1]))
# print(lonely([4, 4, 4, 3, 3]))


from re import A


a = [1,2,3,4,5]
b = a 

a[2] = 5

print(a)
print(b)