def only_square_area(list):
    lst = []
    for i in list[0]:
        if i in list[1]:
            lst.append(i**2)
    return lst

print(only_square_area(([32,55,63],[13,32,40,55])))