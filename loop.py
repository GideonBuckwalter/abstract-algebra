from row_column import Row, Column, Symbol
import itertools
import operator

class AbstractLoop:
    PADDING = 5

    _container = None
    _primary_dimension = None
    _secondary_dimension = None

    def __init__(self, positive=None, negative=None):
        self.positive = positive if positive is not None else self._container([])
        self.negative = negative if negative is not None else self._container([])
        self.rel_child_positions = []
        
        self.add_dim_getters(self._primary_dimension, operator.plus, 4)
        self.add_dim_getters(self._secondary_dimension, max, 2)

    def add_dim_getters(self, dim_name, func, pad_times):
        setattr(self, "sym_" + dim_name,
            lambda slf:
                func(getattr(slf.positive, "sym_" + dim_name),
                     getattr(slf.negative, "sym_" + dim_name)))

        setattr(self, "pix_" + dim_name,
            lambda slf:
                self.PADDING * padd_times * \
                func(getattr(slf.positive, "pix_" + dim_name),
                     getattr(slf.negative, "pix_" + dim_name)))

    def draw(self, abs_pos):
        self.render_loop(abs_pos)

        vecs = self.rel_child_positions
        kids = itertools.chain(self.positive, self.negative)
        for vector, child in izip(vecs, kids):
            child.draw(abs_pos + vector)


class MLoop(AbstractLoop):
    _container = Column
    _primary_dimension = "height"
    _secondary_dimension = "width"

    # METAPROGRAM AWAY IN FUTURE
    def render_loop(self, abs_pos):
        stroke(255, 255, 255)
        noFill()
        rect(abs_pos.x, abs_pos.y, self.pix_width(), self.pix_height())

class ALoop(AbstractLoop):
    _container = Row
    _primary_dimension = "width"
    _secondary_dimension = "height"

    # METAPROGRAM AWAY IN FUTURE
    def render_loop(self, abs_pos):
        stroke(255, 255, 255)
        noFill()
        rect(abs_pos.x, abs_pos.y, self.pix_width(), self.pix_height())



