my_hash_table = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]


#my_hash_table = [None,None,None,None,None,None,None,None,None,None]

def hash_funtion(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    return sum_of_char % 10

def add(value):
    index = hash_funtion(value)
    bucket = my_hash_table[index]
    if value not in bucket:
        bucket.append(value)

def contains(value):
    index = hash_funtion(value)
    bucket = my_hash_table[index]
    return value in bucket


add('Kabin')
print('\n')
print(my_hash_table)
print('\n')
print("'Kabin' is in the Hash Set :", contains('Kabin'))
