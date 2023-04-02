# 168. Excel Sheet Column Title

# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            c = chr(ord('A') + (columnNumber - 1) % 26)
            result = c + result
            columnNumber = (columnNumber - 1) // 26
            
        return result