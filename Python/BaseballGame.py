class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sumList = []
        for i in range(len(operations)):
            if(operations[i]=="+"):
                sumList.append(sumList[-1]+sumList[-2])
            elif(operations[i]=="D"):
                sumList.append(sumList[-1]*2)
            elif(operations[i]=="C"):
                sumList.pop()
            else:
                sumList.append(int(operations[i]))
        return sum(sumList)
        # Here I traverse through a string and perform the operation corresponding to the letter
        # + is to add previous 2 scores as new score
        # D is to double the previous score as new score
        # C is to remove the previous score (hence I pop)
        # Otherwise, or an x, I record the score cast as integer (since it is a string beforehand)