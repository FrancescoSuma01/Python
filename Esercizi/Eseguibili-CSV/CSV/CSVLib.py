class CSV():
    def __init__(self, filename):
        self.file = open(self.filename)
        self.lines = list()

        line = self.file.readline(Row(line))   #legge una riga dal file

class Row():
    pass

class Cell():
    pass