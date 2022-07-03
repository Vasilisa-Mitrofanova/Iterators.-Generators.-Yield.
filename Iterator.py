nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class MyClass:
    def __init__(self, nlist, x: int = 0, y: int = -1):
        self.nlist = nlist
        self.x = x
        self.y = y

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.y < len(self.nlist[self.x])-1:
                self.y += 1
                result = self.nlist[self.x][self.y]
                return result
            else:
                self.x += 1
                self.y = 0
                result = self.nlist[self.x][self.y]
                return result
        except:
            raise StopIteration


for item in MyClass(nested_list):
    print(item)