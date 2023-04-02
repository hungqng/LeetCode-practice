# 409. Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)

        # Solution 2 hash set
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)

        # Solution 3
        res = 0
        count = Counter(s)
        for c, n in count.items():
            if n % 2 == 0 or res % 2 == 0:
                res += n
            else:
                res += n - 1
        return res

        # Solution 4
        c = Counter(s)
        output = 0
        odd_found = False
        for count in c.values():
            if odd_found:
                if count > 1:
                    if count % 2 == 0:
                        output += count
                    else:
                        output += count - 1
            else:
                if count % 2 == 0:
                    output += count
                else:
                    output += count
                    odd_found = True
        return output

        # Solution 5
        c = Counter(s)
        output = 0
        odd_found = False
        for count in c.values():
            output += int(count / 2) * 2
            if output % 2 == 0 and count % 2 == 1:
                output += 1
        return output