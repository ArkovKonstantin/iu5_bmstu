st = "abcd"
def rev2(str):
    s= ""
    for n in range(len(str)):
        s = s + str[(len(str)-n-1)]
    return s

print (rev2(st))