from sys import stdout, stdin

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

    @property
    def isEnd(self):
        return self.__cur == self.__end
    
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

    @property
    def isEnd(self):
        return self.__cur == self.__end 

class Database:
    def __init__(self, database, hasHeader = False, delimiter = '\t'):
        self.database = database
        self.hasHeader = hasHeader
        self.delimiter = delimiter
        self.dbCont = List()
        self.proFile()

    def proFile(self):
        for line in open(self.database):
            self.dbCont.append(line.rstrip().split(self.delimiter))

    def __iter__(self):
        return iter(self.dbCont)

    def __next__(self):
        yield next(self.dbCont)

    def __getitem__(self, index):
        print(self.dbCont.cur)
        if self.dbCont.isHead and self.hasHeader:
            next(self)
        return self.dbCont.cur[index]
        
class Anno:
    def __init__(self, *index, reader = stdin, writer = stdout, newCols = None, database = None, hasHeader = False, delimiter = '\t'):
        self.hasHeader = hasHeader
        self.reader = reader
        self.writer = writer
        self.newCols = newCols
        self.needAnno = List()
        self.db = database
        self.delimiter = delimiter
        self.index = index
        self.proFile()
        
    def proFile(self):
        for line in self.reader:
            self.needAnno.append(line.rstrip().split(self.delimiter))

    def __repr__(self):
        return f"Total items: {len(self.needAnno)}\nIndex: {self.index}"

    def anno(self):
        assert False, "anno must be define"

    def __getitem__(self, index):
        return self.needAnno.cur[index]

    def write(self):
        for item in self.needAnno:
            if self.needAnno.isHead and self.hasHeader:
                self.writer.write('\t'.join(item.value) + '\t' + self.newCols + '\n')
            else:
                self.writer.write('\t'.join(item.value) + '\t' + '\t'.join(item.attr) + '\n')

    def addAnno(self, val):
        self.needAnno.cur.putInfo(val)
    
    def run(self):
        self.anno()
        self.write()
    

if __name__ == "__main__":
    
    class MyAnno(Anno):
        def anno(self):
            t = ('chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrMT')
            needAnno = iter(self.needAnno)
            database = iter(self.db)
            next(needAnno)
            naItem = next(needAnno)
            next(database)
            dbItem = next(database)
            while True:
                try:
                    chrom = naItem[0]
                    pos = int(naItem[1]) + 1
                    ref = naItem[3]
                    alt = naItem[4]

                    db_chrom = dbItem[0]
                    db_pos = int(dbItem[1])
                    db_ref = dbItem[3]
                    db_alt = dbItem[4]

                    if t.index(db_chrom) > t.index(chrom):
                        self.addAnno("*")
                        naItem = next(needAnno)
                    elif t.index(db_chrom) < t.index(chrom):
                        dbItem = next(database)
                    else:
                        if db_pos > pos:
                            self.addAnno("*")
                            naItem = next(needAnno)
                        elif db_pos < pos:
                            dbItem = next(database)
                        else:
                            if ref == db_ref and alt == db_alt:
                                self.addAnno(dbItem[5])
                                naItem = next(needAnno)
                            else:
                                self.addAnno("*")
                                naItem = next(needAnno)
                except StopIteration:
                    try:
                        while not self.needAnno.isEnd:
                            self.addAnno("*")
                            next(needAnno)
                    except StopIteration:
                        pass
                    break
                    
    db = Database('database.txt', hasHeader = True)

    '''
    class MyAnno(Anno):
        def anno(self):
            for item in self.needAnno:
                if len(item[3]) == len(item[4]):
                    self.addAnno('SNP')
                else:
                    self.addAnno('not_a_SNP')
    
    reader = open('needAnno.txt')
    writer = open('myAnno.txt', 'w')
    a = MyAnno(reader = reader, writer = writer, hasHeader = True, newCols = 'GnomAD_Freq')
    '''
    a = MyAnno(database = db, hasHeader = True, newCols = "CLNREVSTAT")
    a.run()
