class Node:
    def __init__(self, value):
        self.value = value
        self.attr = []
        self.prev = None
        self.next = None
#    @property
#    def next(self):
#        return self.n
    
#    @property
#    def prev(self):
#        return self.p
    
    @property
    def end(self):
        return not bool(self.next)

    def putInfo(self, val):
        self.attr.append(val)

class List(Node):

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

    def isHead(self):
        return self.__cur == self.__head
    
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

    def setCur(self, cur):
        self.__cur = cur
        
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

    '''
    def insert(self, pos, value):
        if pos <= 0:
            self.add(value)
        elif pos >= len(self):
            self.append(value)
        else:
            node = Node(value)
            count = 0
            cur = self.begin
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next.prev = node
            node.prev = cur
            cur.next = node
    '''

    
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
