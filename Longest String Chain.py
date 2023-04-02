# 1048. Longest String Chain

# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        s = set(words)
        memo = {}
        
        def rec(word):
            if word not in s:
                return 0
            if word in memo:
                return memo[word]
            else:
                N = len(word)
                mx = 0
                for i in range(N):
                    mx = max(mx, rec(word[:i] +word[i+1:]) +1)
                memo[word] = mx
            return mx
        for w in words:
            rec(w)
        return max(memo.values())

        # Solution 2
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        return max(dp.values())