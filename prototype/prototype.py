import copy

class prototype:
    def copy(self, **attr):
        new = copy.deepcopy(self)
        new.__dict__.update(attr)
        return new
        