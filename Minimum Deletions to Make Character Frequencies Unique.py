# 1647. Minimum Deletions to Make Character Frequencies Unique

# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt, res, used = collections.Counter(s), 0, set()
        for ch, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res

        # Solution 2
        prev, keep = inf, 0
        for freq in sorted(Counter(s).values(), reverse=True):
            freq = min(prev - 1, freq)
            if freq == 0:
                break
            keep += freq
            prev = freq
        return len(s) - keep