hashmap = {}
arr = [1, 2, 3, 4, 5]

for i in range(0, len(arr)):
    hashmap[i] = arr[i]

print(hashmap)
print(1 in hashmap)
print(5 in hashmap)
print(hashmap[1])