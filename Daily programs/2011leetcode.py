class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dictonary = {"X++" : 1 , "--X" : -1 , "++X" : 1 , "X--" : -1}
        result = 0
        for key in operations :
            result += dictonary[key]
        return result
        