class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1

    def right_child(self, index):
        return (2 * index) + 2

    def insert(self, val):
        # append to the end of the list
        self.heap.append(val)
        # heapify up from the new element's index
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # while not at the root index and the current value is less than its parent ...
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            # swap the current value with its parent
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if len(self.heap) == 0:
            return None # heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()  # Only one element exists.

        min_val = self.heap[0]
        # Replace the root with the last element.
        self.heap[0] = self.heap.pop()
        # Restore the heap property by heapifying down from the root.
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):

        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        # If right child exists and is smaller than current smallest, update smallest.
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current index, swap and continue heapifying down.
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)



