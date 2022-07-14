from cgitb import small


small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99) # Does not raise an error when the item is not present in the set
print(small_ints)

small_ints.remove(99) # Raises an error when the item is not present in the set
print(small_ints)