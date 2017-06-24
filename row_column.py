
class ExprList(list):
    
    SPACING = 5

    _primary_dimension = None
    _secondary_dimension = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_dim_getter(self._primary_dimension, sum)
        self.add_dim_getter(self._secondary_dimension, max)


    def add_dim_getter(self, dim_name, func):
        func_name = "sym_{}".format(dim_name)

        setattr(self, func_name,
            lambda slf:
                func(getattr(ele, func_name)() for ele in slf))

    def pix_height(self):
        #      Symbol.PIX_HGT * self.sym_height() + self.SPACING * (self.sym_height() - 1)
        return Symbol.PIX_HGT * (self.sym_height() + self.SPACING) - self.SPACING

    def pix_width(self):
        return Symbol.PIX_WTH * (self.sym_width() + self.SPACING) - self.SPACING




class Row(ExprList):
    _primary_dimension = "width"
    _secondary_dimension = "height"

class Column(ExprList):
    _primary_dimension = "height"
    _secondary_dimension = "width"



class Symbol:

    PIX_HGT = 50
    PIX_WTH = 50

    def sym_width(self):
        return 1

    def sym_height(self):
        return 1

    def pix_width(self):
        return PIX_WTH

    def pix_height(self):
        return PIX_HGT

    def draw(self, abs_pos):
        fill(0,0,255)
        noStroke()
        ellipseMode(CENTER)
        ellipse(abs_pos.x, abs_pos.y, self.pix_width(), self.pix_height())