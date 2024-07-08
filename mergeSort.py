 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2;
    left = arr[:mid]
    right = arr[mid:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


my_array = [64,34,25,5,22,11,90,12]
sortedArr = mergeSort(my_array)

print("Sorted Array :", sortedArr)
