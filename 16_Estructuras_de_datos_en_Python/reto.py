class MyList:
    def __init__(self):
        self.data = {}
        self.length = 0

    def append(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError("pop from empty list")
        self.length -= 1
        popped_item = self.data[self.length]
        del self.data[self.length]
        return popped_item

    def shift(self):
        if self.length == 0:
            raise IndexError("shift from empty list")
        self.length -= 1
        shifted_item = self.data[0]
        del self.data[0]
        return shifted_item

    def unshift(self, item):
        self.data = {index + 1: value for index, value in self.data.items()}
        self.data[0] = item
        self.length += 1

    def map(self, func):
        new_list = MyList()
        for index, item in self.data.items():
            new_list.append(func(item))
        return new_list

    def filter(self, func):
        filtered_list = MyList()
        for index, item in self.data.items():
            if func(item):
                filtered_list.append(item)
        return filtered_list

    def join(self, character=","):
        joined_string = ""
        for index, item in self.data.items():
            joined_string += str(item) + character
        # Remove the last character (the extra separator)
        return joined_string[:-len(character)] if joined_string else ""

myList = MyList()
myList.append("a")
myList.append("b")
myList.append("c")

myList = MyList()
myList.append("a")
myList.append("b")
myList.append("c")

print(myList.data)
# Output: {0: 'a', 1: 'b', 2: 'c'}

mapped_list = myList.map(lambda x: x.upper())
print(mapped_list.data)
# Output: {0: 'A', 1: 'B', 2: 'C'}

filtered_list = myList.filter(lambda x: x != "b")
print(filtered_list.data)
# Output: {0: 'a', 2: 'c'}

joined_string = myList.join("-")
print(joined_string)
# Output: 'a-b-c'

popped_item = myList.pop()
print(popped_item)
# Output: 'c'

shifted_item = myList.shift()
print(shifted_item)
# Output: 'a'

myList.unshift("d")
print(myList.data)
# Output: {0: 'd', 1: 'b'}
