from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep=' ', end='')
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = FixedStack(64)

while True:
    print(f'current number of data: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.Push:
        x = int(input('value: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('stack is full')

    elif menu == Menu.Pop:
        try:
            x = s.pop()
            print(f'popped data: {x}')
        except FixedStack.Empty:
            print("stack is empty")

    elif menu == Menu.Peek:
        try:
            x = s.peek()
            print(f'peeked data: {x}')
        except FixedStack.Empty:
            print("stack is empty")

    elif menu == Menu.Search:
        x = int(input())
        cnt = s.count(x)
        if x in s:
            print(f'number of {x} contained in stack: {s.count(x)}')
            print(f'the first position: {s.find(x)}')
        else:
            print(f'{x} is not in stack')

    elif menu == Menu.Dump:
        s.dump()

    else:
        break
