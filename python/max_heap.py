class MaxHeap(object):
    def __init__(self):
        self.heap = [0]

    def insert(self, element):
        self.heap.append(element)
        self.__float()

    def peek_max(self):
        return self.heap[1]

    def remove(self):
        r = self.heap[1]
        e = self.heap.pop(-1)
        self.heap[1] = e
        self.__sink()
        return r

    def __float(self):
        i = len(self.heap) - 1
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2

    def __sink(self):
        i = 1
        if self.heap[i] > self.heap[i * 2] & self.heap[i] > self.heap[i * 2 + 1]:
            return
        else:
            while True:
                temp = self.heap[i]
                if self.heap[i * 2] > self.heap[i * 2 + 1]:
                    self.heap[i] = self.heap[i * 2]
                    self.heap[i * 2] = temp
                    i = i * 2
                else:
                    self.heap[i] = self.heap[i * 2 + 1]
                    self.heap[i * 2 + 1] = temp
                    i = i * 2 + 1
