import numpy as np


class Heap(object):
    def __init__(self, a):

        self.heap = np.asarray(a)
        self._build()

    def _children(self, i, filt=True):

        k = 2 * i + 1
        if filt:
            return np.array([j for j in [i, k, k + 1] if self._is_node(j)])
        else:
            return np.array([i, k, k + 1])

    @staticmethod
    def _parent(i):
        return (i + 1) // 2 - 1

    def _is_node(self, i):
        return 0 <= i < self.size

    def _build(self):

        i = self.start
        while i >= 0:
            self._swap(i)
            i -= 1

    def _swap(self, i):

        c = self._children(i)
        m = self.heap[c].argmax()
        if m > 0:
            self.heap[c[[0, m]]] = self.heap[c[[m, 0]]]
            self._swap(c[m])

    def _up(self, i):

        p = self._parent(i)
        if self._is_node(p) and self.heap[i] > self.heap[p]:
            self.heap[[i, p]] = self.heap[[p, i]]
            self._up(p)

    def insert(self, n):

        self.heap = np.append(self.heap, n)
        self._up(self.size - 1)

    def max(self):

        return self.heap[0]

    def pop(self):

        m = self.max()
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]

        self._swap(0)

        return m

    @property
    def size(self):

        return len(self.heap)

    @property
    def start(self):

        return (self.size + 1) // 2 - 1

    @property
    def _levels(self):

        return int(np.log2(self.size + 1))

    def _is_level(self, i):

        return int(np.log2(i + 1)) <= self._levels

    def __repr__(self):

        return self.heap.__repr__()

    def _show_node(self, i, horizontal=True):

        i, l, r = self._children(i, filt=False)

        base = Str2d(
            str(self.heap[i]) if self._is_node(i) else ' ',
            height=2, width=5
        )

        if self._is_level(l):
            if horizontal:
                base = base / (
                        self._show_node(l, horizontal) + self._show_node(r, horizontal)
                )
            else:
                base = base + (
                        self._show_node(l, horizontal) / self._show_node(r, horizontal)
                )

        return base
