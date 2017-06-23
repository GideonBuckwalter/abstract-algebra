class Row(list):
    def sym_width(self):
        return sum(ele.sym_width() for ele in self)

    def sym_height(self):
        return max(ele.sym_height() for ele in self)

class Column(list):
    def sym_width(self):
        return max(ele.sym_width() for ele in self)

    def sym_height(self):
        return sum(ele.sym_height() for ele in self)

class Symbol:
    def sym_width(self):
        return 1

    def sym_height(self):
        return 1