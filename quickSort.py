
def quicksort(array, low , high):
    if high is None:
        high = len(array) -1

    if low < high:
        pivot = partition(array,low,high)
        quicksort(array,low,pivot-1)
        quicksort(array,pivot+1,high)


def partition(array,low,high):
    p = array[low]
    i = low +1 
    j = high
    while True:
        while i <= j and array[i] <= p:
            i+=1
        while i <= j and array[j] >= p:
            j-=1
        if i < j:
            array[i], array[j] = array[j] , array[i]
        else:
            break
    array[low],array[j] = array[j], array[low] 
    return j

my_array = [64,34,25,5,22,11,90,12]
quicksort(my_array,0, None)
print("sorted :",my_array)
