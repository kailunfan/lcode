def findThirdLargest(numbers):
    base = [float('-inf')]*3
    for n in numbers:
        if n <= base[0]:
            continue
        if base[0]<n<=base[1]:
            base[0] = n
        elif base[1]<n<=base[2]:
            base[0],base[1] = base[1], n
        elif n>base[2]:
            base[0], base[1], base[2] = base[1],base[2], n
    return base[0]

assert findThirdLargest([10,7,8,9]) == 8
assert findThirdLargest([1,2,3,4,5,6]) == 4
assert findThirdLargest([6,5,4,3,2,1]) == 4

