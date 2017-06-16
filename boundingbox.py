# boundingbox.py

class BoundingBox:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def fit_inside(self, enclosing):
        h_pct = self.h / enclosing.h
        w_pct = self.w / enclosing.w

        scalar = h_pct if h_pct > w_pct else w_pct

        self.w /= scalar
        self.h /= scalar
