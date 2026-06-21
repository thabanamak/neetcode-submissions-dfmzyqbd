class Solution:
    def calPoints(self, operations: List[str]) -> int:
        array = []
        special = ["+","C","D"]
        for i in range(len(operations)):
            
            if operations[i] in special and array:
                if operations[i] == "+":
                    total = int(array[-1]) + int(array[-2])
                    array.append(total)
                elif operations[i] == "C":
                    array.pop()

                elif operations[i] == "D":
                    total = int(array[-1])*2
                    array.append(total)

            if operations[i] not in special:
                array.append(int(operations[i]))

        return sum(array)

        