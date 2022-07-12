from xmlrpc.client import boolean


def multiply(x: float, y: float) -> float:
  """
  Multiply 2 numbers.

  Although this function is intended to multiply 2 numbers,
  you can also use it to multiply a sequence.  If you pass
  a string, for example, as the first argument, you'll get
  the string repeated `y` times as the returned value.

  :param x: The first number to multiply.
  :param y: The number to multiply `x` by.
  :return: The product of `x` and `y`.
  """
  result = x * y
  return result


def is_palindrome(string: str) -> bool:
  """Check if a string is a palindrome.
     A palindrome is a string that reads the same forwards and backwards

  Args:
      string (string): The string to check

  Returns:
      bool: True if `string` is a palindrome, False otherwise
  """


  # backwards = string[::-1]
  # return backwards == string
  return string[::-1].casefold() == string


def palindrome_sentence(sentence: str) -> bool:
  string = ""
  for char in sentence:
    if char.isalnum():
      string += char

  # return string[::-1].casefold() == string
  return is_palindrome(string)


answer = multiply(10.5, 4)
print(answer)

print()

for val in range(1,5):
  two_times = multiply(2,val)
  print(two_times)

# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#   print("'{}' is a palindrome".format(word))
# else:
#   print("'{}' is not a palindrome".format(word))

def fibonacci(n: int) -> int:
  """Return the `n`th Fibonacci number, for positive `n`.

  Args:
      n (int): `n`th Fibonacci number to be found.

  Returns:
      F (int): The `n`th Fibonacci number.
  """
  if 0 <= n <= 1:
    return n
  n_minus1, n_minus2 = 1, 0

  result = None
  for f in range(n-1):
    result = n_minus2 + n_minus1
    n_minus2 = n_minus1
    n_minus1 = result
  return result


for i in range(36):
  print(i, fibonacci(i))

p = palindrome_sentence(54645)