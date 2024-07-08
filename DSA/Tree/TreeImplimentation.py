
binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def getData(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None

left_child = left_child_index(0)
right_child_of_left_child= right_child_index(left_child)

data = getData(right_child_of_left_child)

print("root.right.left.data : ",data)
