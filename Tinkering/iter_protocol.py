class MyIter:
    def __init__(self, index=0):
        self.mylist = [1, 2, 3, 4, 5]
        self.index = index

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.mylist):
            raise StopIteration

        result = self.mylist[self.index]
        self.index += 1
        return result


iter = MyIter()

if 6 in iter:
    print("Six!")
else:
    print("Boo")
if 1 in iter:
    print("One!")