print('xd')
l = [14, 13, 6, 7, 8, 10, 1, 2]

def find(list, target):
    s = set(l)
    for i in s:
        diff = target - i 
        if diff in s:
            return i, diff
print(find(l, 3))