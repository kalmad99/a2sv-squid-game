class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        power, result = 0, []
        while columnNumber > 0:
            number = (columnNumber-1) % 26
            result.append(chr(65+number))
            columnNumber = (columnNumber-1)//26
        return "".join(result[::-1])