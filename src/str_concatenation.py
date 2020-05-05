def string_add(count):
    str = ''
    for i in range(count):
        str += chr(count % 26 + ord('a'))


def list_add(count):
    list = []
    for i in range(count):
        list.append(chr(count % 26 + ord('a')))
    str = ''.join(list)


if __name__ == "__main__":
    # import sys
    # sys.stdout = open('output.txt', 'w')
    import time
    count = 10000000
    while count < 10000000000:
        print("count:", count)
        start = time.time()
        string_add(count)
        end = time.time()
        print("string:", end - start)
        start = time.time()
        list_add(count)
        end = time.time()
        print("list:", end - start)
        print()
        count *= 2
