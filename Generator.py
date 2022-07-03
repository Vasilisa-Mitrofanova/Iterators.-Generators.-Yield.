nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


def flat_generator(nlist, x=0, y=0):
    while x <= len(nlist)-1:
        while y <= len(nlist[x]) - 1:
            yield nlist[x][y]
            y += 1
        x += 1
        y = 0


for item in flat_generator(nested_list):
    print(item)