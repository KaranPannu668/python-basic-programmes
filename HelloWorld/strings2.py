parrot = "Norwegian Blue"

#  Slice - Start, Stop and Step
# print(parrot[0:6:2])
# print(parrot[0:6:3])

number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
  if not char.isnumeric():
    separators = separators + char

print(separators)

values = "".join( char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
