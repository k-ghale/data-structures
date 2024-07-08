

my_array = [64,34,25,5,22,11,90,12]

n = len(my_array)

#for i in range(1,n):
 #  current_value = my_array[i]
  #  j = i - 1
   # while j>=0 and my_array[j] > current_value:
   #     my_array[j+1] = my_array[j]
    #    j -= 1
    #my_array[j+1] = current_value

for i in range(1,n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1 , -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else :
            break
    my_array[insert_index] = current_value


print("Sorted Array : ", my_array);
