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

    def __getitem__(self, index):
        return self.value[index]

class List:

    def __init__(self):
        self.__head = Node(None)
        self.__end = Node(None)
        self.__cur = self.__head
        self.__items = 0
        self.__head.next = self.__end
        self.__end.prev = self.__head

    def isEmpty(self):
        return self.__items == 0

    def end(self):
        return self.__cur.end

    def __len__(self):
        return self.__items

    def __iter__(self):
        self.__cur = self.__head
        return self

    def __next__(self):
        if self.__cur.next == self.__end:
            raise StopIteration
        else:
            self.__cur = self.__cur.next
            return self.__cur

    def add(self, value):
        node = Node(value)
        self.__head.next.prev = node
        node.next = self.__head.next
        self.__head.next = node
        node.prev = self.__head
        self.__items += 1

    @property
    def isHead(self):
        return self.__cur == self.__head.next
    
    def append(self, value):
        node = Node(value)
        self.__end.prev.next = node
        node.prev = self.__end.prev
        self.__end.prev = node
        node.next = self.__end
        self.__items += 1

    @property
    def cur(self):
        return self.__cur
