def oddEven():
    for num in range (1, 2001):
        if num % 2 != 0:
            print "Number is {}. This is an odd number".format(num)
        elif num % 2 == 0:
            print "Number is {}. This is an even number".format(num)
oddEven()

a = [2,4,10,16]

def multiply(arr, mult):
    newArr = []
    for val in arr:
        newArr.append(val * mult)
    print newArr
    return newArr
multiply(a, 5)


def layeredMultiply(arr):
    layeredArr = []
    for val in arr:
        newArr = []
        for count in range (0, val):
            newArr.append(1)
        layeredArr.append(newArr)
    print layeredArr
layeredMultiply(multiply([2,4,5],3))