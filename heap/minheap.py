class MinHeap:
    def __init__(self):
        self.heap = []
        self.parent = lambda i: (i - 1) // 2
        self.leftchild = lambda i: (2 * i + 1)
        self.rightchild = lambda i: (2 * i + 2)

    def insert(self, val):
        self.heap.append(val)
        self.heapUp(len(self.heap)-1)

    def insert_from_list(self, arr):
        for i in arr:
            self.insert(i)

    def delete(self, val):
        if val in self.heap:
            if len(self.heap) == 1:
                self.heap.pop(0)
                return
            idx = self.heap.index(val)
            print(idx)
            self.heap[idx] = self.heap.pop(-1)
            if idx < len(self.heap):
                if idx > 0 and self.heap[idx] > self.heap[self.parent(idx)]:
                    self.heapUp(idx)
                else:
                    self.heapDown(idx)
        else:
            return -1

    def extractMax(self):
        if len(self.heap) == 0:
            return -1
        if len(self.heap) == 1:
            return self.heap.pop(0)
        root = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self.heapDown(0)
        return root

    def heapUp(self, idx):
        while idx != 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            self.swap(idx, self.parent(idx))
            idx = self.parent(idx)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapDown(self, i):
        mx = i
        lc = self.leftchild(i)
        rc = self.rightchild(i)
        if lc < len(self.heap) and self.heap[lc] < self.heap[mx]:
            mx = lc
        if rc < len(self.heap) and self.heap[rc] < self.heap[mx]:
            mx = rc
        if mx != i:
            self.swap(i, mx)
            self.heapDown(mx)

    def heapify(self, nums, n, i):
        mn = i
        lc = 2 * i + 1
        rc = 2 * i + 2
        if lc < n and nums[lc] < nums[mn]:
            mn = lc
        if rc < n and nums[rc] < nums[mn]:
            mn = rc
        if mn != i:
            nums[i], nums[mn] = nums[mn], nums[i]
            self.heapify(nums, n, mn)

    def heapSort(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        return nums[::-1]


heap = MinHeap()
res = [10, 5, 7, 1, 4, 17, 99, 88]
heap.insert_from_list(res)
print(heap.heapSort(res))
