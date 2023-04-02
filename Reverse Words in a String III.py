# 557. Reverse Words in a String III

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []

        for word in words:
            res.append(word[::-1])
            res.append(" ")
        return "".join(res).strip()

        # Solution 2
        return ' '.join(s.split()[::-1])[::-1]