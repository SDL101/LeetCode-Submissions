class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashReg = [0, 0, 0]
                # 5, 10, 20
        
        for bill in bills:
            if bill == 5:
                cashReg[0] += 1
            elif bill == 10:
                cashReg[1] += 1
                while bill > 5:
                    if cashReg[0] > 0:
                        cashReg[0] -= 1
                        bill -= 5
                    else:
                        return False
            elif bill == 20:
                cashReg[2] += 1
                while bill > 5:
                    if cashReg[1] > 0 and bill - 10 >= 5:
                        cashReg[1] -= 1
                        bill -= 10
                    elif cashReg[0] > 0:
                        cashReg[0] -= 1
                        bill -= 5
                    else:
                        return False

        return True

                    