# jabber = open('D:\\Udemy\Learn Python Programming Masterclass\TextFiles\Jabberwocky.txt', 'r')

# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))

# jabber.close()



# with open('D:\\Udemy\Learn Python Programming Masterclass\TextFiles\Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()

# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end='')

# with open('D:\\Udemy\Learn Python Programming Masterclass\TextFiles\Jabberwocky.txt') as jabber:
#     text = jabber.read()

# print(text)
# for character in reversed(text):
#     print(character, end='')

with open('D:\\Udemy\Learn Python Programming Masterclass\TextFiles\Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('D:\\Udemy\Learn Python Programming Masterclass\TextFiles\Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break