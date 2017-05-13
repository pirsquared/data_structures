from operator import lt, gt

class Heap(object):
    def __init__(self, kind='min'):
        self.heap = []
        self.size = 0
        self.kind = kind
        if kind == 'min':
            self.op = lt
        elif kind == 'max':
            self.op = gt
        else:
            raise ValueError('`kind` needs to be "min" or "max"')

    def insert(self, x):
        heap = self.heap
        heap.append(x)
        self.size += 1
        self.bubble_up(self.size)
        
    def bubble_up(self, i):
        if 1 < i <= self.size:
            heap = self.heap
            j = i // 2
            node = heap[i - 1]
            up = heap[j - 1]
            if self.op(node, up):
                self[i-1, j-1]
                self.bubble_up(j)    
    
    def bubble_down(self, i):
        size, op = self.size, self.op
        if 1 <= i < size:
            heap = self.heap
            nd = self[i-1]
            j = i * 2
            k = j + 1
            if k <= size:
                rt = self[k-1]
                lf = self[j-1]
                if op(rt, nd):
                    if op(rt, lf):
                        self[i-1, k-1]
                        self.bubble_down(k)
                    elif op(lf, nd):
                        self[i-1, j-1]
                        self.bubble_down(j)
                elif op(lf, nd):
                    self[i-1, j-1]
                    self.bubble_down(j)
            elif (j <= size):
                lf = self[j-1]
                if op(lf, nd):
                    self[i-1, j-1]
                    self.bubble_down(j)

    def del_idx(self, idx):
        heap = self.heap
        if 0 <= idx < self.size:
            end = heap.pop()
            self.size -= 1
            if idx < self.size:
                heap[idx] = end
                self.bubble_down(idx + 1)
            
    def del_item(self, item):
        try:
            self.del_idx(self.heap.index(item))
        except ValueError as e:
            raise ValueError('{} is not in the heap'.format(item))
            
    def pop_extreme(self):
        extreme = self.extreme
        self.del_idx(0)
        return extreme

            
    @property
    def extreme(self):
        if self.heap:
            return self.heap[0]

    @property
    def pextreme(self):
        if self.heap:
            print(self.heap[0])

    def __getitem__(self, items):
        heap = self.heap
        try:
            i, j = items
            heap[i], heap[j] = heap[j], heap[i]
        except:
            return heap[items]
        
    def __repr__(self):
        return 'Extreme: {}  Size: {}\nHeap: {}\n'.format(self.extreme, self.size, str(self.heap))
    
    def __bool__(self):
        return bool(self.heap)
    
    def __lt__(self, other):
        return self.extreme < other.extreme
    
    def __le__(self, other):
        return self.extreme <= other.extreme
    
    def __gt__(self, other):
        return self.extreme > other.extreme
    
    def __ge__(self, other):
        return self.extreme >= other.extreme
    
    def __eq__(self, other):
        return self.extreme == other.extreme
    
    def __ne__(self, other):
        return self.extreme != other.extreme
    
    def query(self, kind, arg=None):
        if kind == 1:
            self.insert(arg)
        elif kind == 2:
            self.del_item(arg)
        elif kind == 3:
            self.pextreme
