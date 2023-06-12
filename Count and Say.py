# 38. Count and Say

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = ""
        count = 1
        i = 0

        while i < len(prev):
            # Count the number of consecutive digits
            while i < len(prev) - 1 and prev[i] == prev[i + 1]:
                count += 1
                i += 1

            # Append the count and digit to the result
            result += str(count) + prev[i]
            
            # Reset count for the next digit
            count = 1
            i += 1

        return result