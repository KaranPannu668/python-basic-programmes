panagram = """The quick brown
 fox jumps\tover
  the lazy fox"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# replace the values in place 
values_list = ['9' , '33' , '343', '4343']


for index in range(len(values_list)):
  values_list[index] = int(values_list[index])

print(values_list)

# create a new list

integer_values = []
for value in values_list:
  integer_values.append(int(value))

print(integer_values)