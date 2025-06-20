class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        topRemoved = self.q.popleft()
        self.q = self.q.popleft()
        return topRemoved

    def top(self) -> int:
        return self.q[0]
        return top

    def empty(self) -> bool:
        return self.q == None
        
# Time Complexity:  O(1) for all 4 stack operations 
# Space Complexity: O(n) since deque scales linearly with input size from user


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()