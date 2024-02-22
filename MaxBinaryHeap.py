class MaxBinaryHeap:
    def __init__(self):
        self.heap = []

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def get_parent_index(self, index):
        return (index - 1) // 2

    def add(self, value):
        self.heap.append(value)
        self._percolate_up(len(self.heap) - 1)

    def delete_max(self):
        if len(self.heap) == 0:
            return None

        max_value = self.heap[0]
        self._swap(0, len(self.heap) - 1)
        self.heap.pop()
        self._percolate_down(0)
        return max_value

    def _parent_exists(self, index):
        return index > 0

    def _percolate_up(self, index):
        if index <= 0:
            return

        parent_index = self.get_parent_index(index)
        if self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            self._percolate_up(parent_index)

    def _percolate_down(self, index):
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)

        if (left_child_index >= len(self.heap) and right_child_index >= len(self.heap)):
            return

        largest_child_index = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest_child_index]:
            largest_child_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_child_index]:
            largest_child_index = right_child_index

        if largest_child_index != index:
            self._swap(index, largest_child_index)
            self._percolate_down(largest_child_index)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def heap_sort(lst):
    heap = MaxBinaryHeap()
    for i in lst:
        heap.add(i)
    sorted_list = []
    while heap.heap:
        sorted_list.append(heap.delete_max())
    return sorted_list

def main():
    data = [3, 6, 8, 10, 1, 2, 1]
    print("Original list:", data)
    sorted_data = heap_sort(data)
    print("Sorted list:", sorted_data)

if __name__ == "__main__":
    main()