class SegmentTree:
    arr = []
    tree = []

    def __init__(self, arr):
        arr.sort()
        self.arr = arr
        self.tree = [None] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = 1
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if start > right or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, left, right)
        right_sum = self.query(2 * node + 1, mid + 1, end, left, right)
        return left_sum + right_sum

    def find_prefix_with_sum(self, target_sum):
        return self._find_prefix_with_sum(1, 0, len(self.arr) - 1, target_sum)

    def _find_prefix_with_sum(self, node, start, end, target_sum):
        if start == end:
            if self.tree[node] == target_sum:
                self.update(1, 0, len(self.arr) - 1, start, 0)
                return start
            else:
                return None
        mid = (start + end) // 2
        left_sum = self.tree[2 * node]
        if left_sum >= target_sum:
            return self._find_prefix_with_sum(2 * node, start, mid, target_sum)
        else:
            return self._find_prefix_with_sum(2 * node + 1, mid + 1, end, target_sum - left_sum)

    def update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = 0
            return
        mid = (start + end) // 2
        if index <= mid:
            self.update(2 * node, start, mid, index, value)
        else:
            self.update(2 * node + 1, mid + 1, end, index, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]