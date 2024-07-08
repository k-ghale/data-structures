
array = [51,66,45,89,11,54,23,25,56,75,22,33]

n = len(array)

print("Unsorted Array: ", array);

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if(array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1],array[j]
            swapped = True
    if not swapped:
        break

print("Sorted Array: ", array);
