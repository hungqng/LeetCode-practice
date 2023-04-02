# 171. Excel Sheet Column Number

# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        multiplier = 1
        column = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            column += (ord(columnTitle[i]) - 64) * multiplier
            multiplier *= 26
        return column

        # Solution 2
        # ans, pos = 0, 0
        # for letter in reversed(columnTitle):
        #     digit = ord(letter)-64
        #     ans += digit * 26**pos
        #     pos += 1
            
        # return ans