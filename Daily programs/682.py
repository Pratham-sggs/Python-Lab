class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result_list = []
        for operation in operations :
            if operation == "D" :
                result_list.append(result_list[-1]*2)
            elif operation == "+" :
                sum_temp = result_list[-1] + result_list[-2]
                result_list.append(sum_temp)
            elif operation == "C" :
                result_list.pop()
            else :
                result_list.append(int(operation))
        return sum(result_list)