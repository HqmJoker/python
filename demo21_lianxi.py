def indexOf(arr,num,*args):
    i = 0
    if(len(args) > 0):
        i = args[0]
    while i<len(arr):
        if(arr[i] == num):
            return i
        i += 1
    return -1

print(indexOf([100,200,300],200))
print(indexOf([100,200,300],300,3))
print(indexOf([100,200,300],300,2))
print(indexOf([100,200,300],200,2))
print(indexOf([100,200,300],100))