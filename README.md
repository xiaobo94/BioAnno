1. 该包主要应用于多列的纯文本文件依据某一列以及多列的自身条件，或者依据另外的数据库来对文件进行注释。
2. 使用说明：
   使用时需要导入Anno类，然后自己定义一个类作为子类继承Anno，并重新定义子类的方法函数anno。在anno方法中，如果没有使用到数据库注释，则可以使用self.needAnno作为可迭代对象进行迭代，也可以使用iter和next进行手动迭代，但是需要处理迭代到最后产生的StopIteration异常。迭代过程中产生的内容即为输入文件的每一行，可以使用中括号来取每一行中的每一项，然后依据每一项的关系来输出不同的注释结果，注释结果需要使用self.addAnno('someting')来将其添加，最后会输出到该行最后。同理，如果根据数据库注释的话，则可以在anno方法中使用self.db，使用方法同self.needAnno，但需要创建Database类的实例，并作为参数传给Anno的子类。
3. 参数：
   Database类参数：
       database为数据库文件，delimiter为数据库分隔符，默认为制表符，hasHeader为数据库是否包含表头，默认为False。
   Anno类参数：
       reader为需要注释文件的文件描述符，默认为从标准输入读取，writer为需要输出文件描述符，默认输出到屏幕，newCols为新的注释列，database为Database类实例，默认为False，hasHeader为文件是否含有表头，默认False，delimiter为注释文件的分隔符，默认为制表符。
       