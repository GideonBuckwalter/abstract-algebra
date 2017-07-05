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

        self.rel_snap_pos = Vector()
        self.rel_phys_pos = Vector()
        
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
    
    def children(self):
        return itertools.chain(self.positive, self.negative)

    def calc_child_rel_snap_positions(self):
        # ASSUME THIS IS A ALOOP

        s = 0
        for child in self.positive:
            s += self.PADDING
            s += child.pix_width() / 2
            child.rel_snap_pos = Vector(s, 0)
            s += child.pix_width() / 2

        s = 0
        for child in self.negative:
            s += self.PADDING
            s += child.pix_width() / 2
            child.rel_snap_pos = Vector(-s, 0)
            s += child.pix_width() / 2

    def draw(self, parent_screen_pos):
        screen_pos = parent_screen_pos + self.rel_snap_pos + self.rel_phys_pos
        self.render_loop(screen_pos)
        for child in self.children():
            child.draw(screen_pos)


class MLoop(AbstractLoop):
    _container = Column
    _primary_dimension = "height"
    _secondary_dimension = "width"

    # METAPROGRAM AWAY IN FUTURE
    def render_loop(self, screen_pos):
        stroke(255, 255, 255)
        noFill()
        rect(screen_pos.x, screen_pos.y, self.pix_width(), self.pix_height())

    def calc_child_rel_snap_positions(self):
        # ASSUME THIS IS A ALOOP

        s = 0
        for child in self.positive:
            s += self.PADDING
            s += child.pix_height() / 2
            child.rel_snap_pos = Vector(0, s)
            s += child.pix_height() / 2

        s = 0
        for child in self.negative:
            s += self.PADDING
            s += child.pix_height() / 2
            child.rel_snap_pos = Vector(0, -s)
            s += child.pix_height() / 2

class ALoop(AbstractLoop):
    _container = Row
    _primary_dimension = "width"
    _secondary_dimension = "height"

    # METAPROGRAM AWAY IN FUTURE
    def render_loop(self, screen_pos):
        stroke(255, 255, 255)
        noFill()
        rect(screen_pos.x, screen_pos.y, self.pix_width(), self.pix_height())

    def calc_child_rel_snap_positions(self):
        # ASSUME THIS IS A ALOOP

        s = 0
        for child in self.positive:
            s += self.PADDING
            s += child.pix_width() / 2
            child.rel_snap_pos = Vector(s, 0)
            s += child.pix_width() / 2

        s = 0
        for child in self.negative:
            s += self.PADDING
            s += child.pix_width() / 2
            child.rel_snap_pos = Vector(-s, 0)
            s += child.pix_width() / 2

