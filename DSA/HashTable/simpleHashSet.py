
class SimpleHashSet:
    def __init__(self, size = 100):
        self.size = size
        self.bucket = [[] for _ in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        index = self.hash_function(value)
        bucket = self.bucket[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.bucket[index]
        return value in bucket

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.bucket[index]
        if value in bucket:
            bucket.remove(value)

    def print_self(self):
        print(' Hash Set Contents :')
        for index, bucket in enumerate(self.bucket):
            print(f"Bucket {index}: {bucket}")

hash_set = SimpleHashSet()

hash_set.add('Kabin')
hash_set.add('Ghale')
hash_set.add('Usham')
hash_set.add('Enish')
hash_set.add('Ging')
hash_set.add('Gon')
hash_set.add('Gin')
hash_set.add('Baka')
hash_set.add('Luci')
hash_set.add('Monkey D Luffy')

hash_set.print_self()

print("'Kabin' is in the Hash Set : ", hash_set.contains('Kabin'))
print('Removing Kabin')
hash_set.remove('Kabin')
print("'Kabin' is in the Hash Set : ", hash_set.contains('Kabin'))
print("'Ghale' has a hash code : ",hash_set.hash_function('Ghale'))
hash_set.print_self()
