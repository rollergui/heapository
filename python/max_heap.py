class MaxHeap(object):
    def __init__(self):
        self.heap = [0]

    def insert(self, element):
        self.heap.append(element)
        self.__float()

    def peek_max(self):
        return self.heap[1]

    def remove(self):
        if len(self.heap) == 2:
            return self.heap[1]
        elif len(self.heap) == 1:
            return "The heap is empty."
        else:
            r = self.heap[1]
            e = self.heap[-1]
            self.heap.pop(-1)
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
        size = len(self.heap) - 1
        while i * 2 <= size:
            if i * 2 + 1 > size:
                if self.heap[i] < self.heap[i * 2]:
                    temp = self.heap[i * 2]
                    self.heap[i * 2] = self.heap[i]
                    self.heap[i] = temp
                return
            else:
                if self.heap[i] < self.heap[i * 2]:
                    if self.heap[i * 2] < self.heap[i * 2 + 1]:
                        temp = self.heap[i * 2 + 1]
                        self.heap[i * 2 + 1] = self.heap[i]
                        self.heap[i] = temp
                        i = i * 2 + 1
                    else:
                        temp = self.heap[i * 2]
                        self.heap[i * 2] = self.heap[i]
                        self.heap[i] = temp
                        i = i * 2
                elif self.heap[i] < self.heap[i * 2 + 1]:
                    temp = self.heap[i * 2 + 1]
                    self.heap[i * 2 + 1] = self.heap[i]
                    self.heap[i] = temp
                    i = i * 2 + 1
                else:
                    return

