class MinStack:

    def __init__(self):
      self._stack = []

    def push(self, val: int) -> None:
      if self._stack:
        if val < self._stack[-1][1]:
          currMin = val
        else:
          currMin = self._stack[-1][1]
      else:
        currMin = val
      self._stack.append([val, currMin])
      

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
      return self._stack[-1][1]