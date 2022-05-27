class Node:
    def __init__(self, value):
        self.value = value
        self.attr = []
        self.prev = None
        self.next = None
    
    @property
    def end(self):
        return not bool(self.next)

    def putInfo(self, val):
        self.attr.append(val)

    @property
    def isHead(self):
        return self.prev == None

    def __getitem__(self, index):
        return self.value[index]

class Iter:
    def __init__(self, headNode):
        self.curNode = headNode
    def __next__(self):
        if not self.curNode:
            raise StopIteration
        else:
            _ = self.curNode
            self.curNode = self.curNode.next
            return _

class List:

    def __init__(self):
        self.__head = None
        self.__end = None
        self.__cur = self.__head
        self.__items = 0

    def isEmpty(self):
        return self.__items == 0

    def end(self):
        return self.__cur.end

    def __len__(self):
        return self.__items

    def __iter__(self):
        return Iter(self.head)

    def add(self, value):
        node = Node(value)
        if self.isEmpty():
            self.__head = node
            self.__end = node
            self.__items += 1
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
            self.__items += 1

    #def isHead(self):
    #    return self.__cur == self.__head
    
    def append(self, value):
        node = Node(value)
        if self.isEmpty():
            self.__head = node
            self.__end = node
            self.__items += 1
        else:
            self.__end.next = node
            node.prev = self.__end
            self.__end = node
            self.__items += 1

    @property
    def head(self):
        self.__cur = self.__head
        return self.__cur

    @property
    def cur(self):
        return self.__cur
    
    @property
    def headItem(self):
        return self.head.value
    
    @property
    def nextItem(self):
        if self.end():
            return "None items"
        self.__cur = self.__cur.next
        return self.__cur.value

if __name__ == "__main__":
    l = List()
    l.append('xiao')
    l.append('bo')
    l.add('shi')
    print(l.isEmpty())
    print(len(l))
    print(l.head)
    print(l.nextItem)
    print(l.nextItem)
    print(l.nextItem)
    print(l.nextItem)
