def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'ID of `greeting` in `greet_pythons` is {id(greeting)}')
    print(f'local namespace in `greet_pythons`(1): {locals()}')

    def make_greeting(item: str) -> str:
        print(f'local namespace in `make_greeting`(1): {locals()}')
        greeting = 'Hi'
        print(f'ID of `greeting` in `make_greeting` is {id(greeting)}')
        print(f'local namespace in `make_greeting`(2): {locals()}')
        return f'{greeting} {item}'
    
    for item in items:
        print(make_greeting(item))
    print(f'ID of `greeting` in `greet_pythons` after execution is {id(greeting)}')


names = ['John']

greet_pythons(names)