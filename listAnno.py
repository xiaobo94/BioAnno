from List import List

class Database:
    def __init__(self, database, hasHeader = False, dellimiter = '\t'):
        self.database = database
        self.dbCont = List()
        self.proFile()

    def proFile(self):
        for line in open(self.database):
            self.dbCont.append(line.rstrip().split(self.delimiter))

    def __iter__(self):
        return Iter(self.dbCont)
        
class Anno:
    def __init__(self, annofile, output, *index, newCols = None, database = None, hasHeader = False, delimiter = '\t'):
        self.hasHeader = hasHeader
        self.annofile =annofile
        self.newCols = newCols
        self.container = List()
        self.db = database
        self.delimiter = delimiter
        self.index = index
        self.output = output
        self.proFile()
        
    def proFile(self):
        for line in open(self.annofile):
            self.container.append(line.rstrip().split(self.delimiter))

    def __repr__(self):
        return f"Total items: {len(self.container)}\nIndex: {self.index}"

    def anno(self):
        assert False, "anno must be define"

    def __getitem__(self, index):
        return self.item[index]

    def write(self):
        with open(self.output, 'w') as f:
            for item in self.container:
                if item.isHead and self.hasHeader:
                    f.write('\t'.join(item.value) + '\t' + self.newCols + '\n')
                else:
                    f.write('\t'.join(item.value) + '\t' + '\t'.join(item.attr) + '\n')
    
    def run(self):
        for item in self.container:
            self.item = item
            if item.isHead and self.hasHeader:
                continue
            item.putInfo(self.anno())
        self.write()
    

if __name__ == "__main__":
    class MyAnno(Anno):
        def anno(self):
            if float(self[11]) > 0.1:
                return 'yes'
            else:
                return 'no'
            
    a = MyAnno('needAnno.txt', "myAnno.txt", hasHeader = True, newCols = 'GnomAD_Freq')
    a.run()
