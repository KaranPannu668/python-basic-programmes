print(__file__)

numbers = [1,2,3,4,5,6]

number = int(input("Enter a number and get it's square"))

# squares = {number ** 2 for number in numbers}
squares = [number ** 2 for number in range(1,7)]

index_pos = numbers.index(number)
print(squares[index_pos])