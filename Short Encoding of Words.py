# 820. Short Encoding of Words

# A valid encoding of an array of words is any reference string s and array of indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)

        # Solution 2
        N = len(words)
        W = set(words)
        for w in words:
            M = len(w)
            for j in range(1, M):
                if w[-j:] in W:
                    W.remove(w[-j:])
        return len("#".join([w for w in W]) + "#")