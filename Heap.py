class Heap(object):
    def __init__(self):
        self.stack = []
        self.size = 0
        
    def insert(self, x):
        self.stack.append(x)
        self.size += 1
        nd_i = self.size - 1
        up_i = self.size // 2 - 1
        while (up_i >= 0) and (self.stack[nd_i] > self.stack[up_i]):
            self.stack[nd_i], self.stack[up_i] = self.stack[up_i], self.stack[nd_i]
            nd_i = up_i
            up_i = (nd_i + 1) // 2 - 1
            
    @property
    def max(self):
        if self.stack:
            return self.stack[0]
    
    def pop(self):
        mx = self.max
        if self.size == 1:
            self.stack = []
            self.size -= 1
        elif self.size > 1:
            self.stack[0] = self.stack.pop()
            self.size -= 1
            self.bubble_down(0)

        return mx
    
    def bubble_down(self, nd_i):
        lf_i = (nd_i + 1) * 2 - 1
        rt_i = lf_i + 1
        if rt_i < self.size:
            rt = self[rt_i]
            nd = self[nd_i]
            lf = self[lf_i]
            if (rt > nd) and (rt > lf):
                self[nd_i, rt_i]
                self.bubble_down(rt_i)
            elif lf > nd:
                self[nd_i, lf_i]
                self.bubble_down(lf_i)
        elif (lf_i < self.size) and (self[lf_i] > self[nd_i]):
            self[nd_i, lf_i]
            self.bubble_down(lf_i)
                
    def __getitem__(self, items):
        try:
            i, j = items
            self.stack[i], self.stack[j] = self[j], self[i]
        except:
            return self.stack[items]
        
    def __repr__(self):
        return 'Max: {}  Size: {}\nStack: {}\n'.format(self.max, self.size, str(self.stack))
