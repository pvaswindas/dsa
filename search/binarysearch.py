class NewList:
    def __init__(self):
        self.arr = []

    def addToList(self, element):
        self.arr.append(element)
        self.arr.sort()
        return self.arr

    def printList(self):
        print(self.arr)
        return

    def FindIndexBinary(self, data):
        left = 0
        right = len(self.arr)-1
        while left <= right:
            mid = int((left + right)//2)
            if self.arr[mid] == data:
                print(f"Element found at index {mid}")
                return
            elif self.arr[mid] < data:
                left = mid+1
            else:
                right = mid-1
        print("Element not found")
        return None


arr = NewList()

arr.addToList(1)
arr.addToList(2)
arr.addToList(3)
arr.addToList(4)
arr.addToList(5)
arr.printList()
arr.FindIndexBinary(1)
