text = input("Please enter your text: ")

output = []
for x in text.split():
    output.append(len(x))
print(output)

answer = [len(x) for x in text.split()]

print(answer)



output = []
for x in text.split():
    output.append((x, len(x)))
print(output)

answer = {(x, len(x)) for x in text.split()}
print(answer)