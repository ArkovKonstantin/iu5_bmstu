
mas = [0, 4, 10, 6, 657, 35, 3456, 2]


def minimum(mas):
    min = mas[0]
    for n in mas:
        if n < min:
            min = n
    return min

def sa(mas):
    sum = 0
    for n in mas:
        sum = sum + n
    return sum/len(mas)


print (minimum(mas))
print (sa(mas))


