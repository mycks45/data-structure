def linearSearch(arr, item):
    ind =0
    i=0
    while i < len(arr):
        if arr[i] == item:
            ind = i
            break
        else:
            ind = 'no such items'
        i+=1
    return ind


arr = [1,2,4,5,6,7,8]
item = 6


result = linearSearch(arr, item)
print('index fo item in arr:'+ str(result))
