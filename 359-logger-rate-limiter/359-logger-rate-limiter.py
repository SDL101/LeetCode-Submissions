class Logger:

    def __init__(self):
        self._time = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._time:
            self._time[message] = timestamp
            return True
        else:
            if timestamp >= (self._time[message] + 10):
                self._time[message] = timestamp
                return True
            else:
                return False
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)