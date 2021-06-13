
def bubbleSort(arr):
    lenght = len(arr)

    i = 0
    while i < lenght-1:
        j = 0
        # swapped flag is used to check if the arr is already sorted or not
        swapped = False
        while j < (lenght-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped =True
            if not swapped:
                break
            j += 1
        i += 1

    return arr

arr = [12,43,12,34,23,56,32,41,45,24,64,57,97,35]

result = bubbleSort(arr)
print(result)
