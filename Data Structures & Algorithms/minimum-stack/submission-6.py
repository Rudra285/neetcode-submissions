class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)
        # if not self.stack:
        #     self.stack.append(val)
        # else:
        #     queue = []
        #     while self.stack and val > self.stack[-1]:
        #         compare = self.stack.pop()
        #         queue.append(compare)
        #     self.stack.append(val)
        #     while queue:
        #         self.stack.append(queue.pop())

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            min_val = self.stack[-1]
            queue = []
            while self.stack:
                compare = self.stack.pop()
                queue.append(compare)
                if min_val >= compare:
                    min_val = compare
            while queue:
                self.stack.append(queue.pop())
            return min_val
        else:
            return None
