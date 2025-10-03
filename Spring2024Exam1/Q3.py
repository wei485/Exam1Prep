#PartA
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)

# Print the result of the map operation as a list
print(list(result))

#PartB
from functools import reduce
# Initializing list
lis = [1, 3, 5, 6, 2]

max_element = reduce(lambda x, y: x if x > y else y, lis)

print(max_element)

#PartC
div7 = [i for i in range(1001) if i % 7 == 0]
print(div7)

#PartD
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]

result = [a, b for a in list_a for b in list_b if a==b]
print(result)