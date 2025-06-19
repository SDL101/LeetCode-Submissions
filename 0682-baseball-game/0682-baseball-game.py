class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreArr = []
        total = 0
        for op in operations:
            if op == "C":
                total = total - scoreArr[-1]
                scoreArr.pop()
            elif op == "D":
                temp = scoreArr[-1]
                scoreArr.append(temp * 2)
                total = total + (temp * 2)
            elif op == "+":
                tempOne, tempTwo = scoreArr[-1], scoreArr[-2]
                scoreArr.append(tempOne + tempTwo)
                total = total + (tempOne + tempTwo)
            else:
                op = int(op)
                scoreArr.append(op)
                total += op
        return total