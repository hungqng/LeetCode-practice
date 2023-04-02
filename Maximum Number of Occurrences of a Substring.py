# 1297. Maximum Number of Occurrences of a Substring

# Given a string s, return the maximum number of ocurrences of any substring under the following rules:

# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])

        # Solution 2
        # counts = dict()
        # for j in range(len(s)-minSize+1):
        #     word = s[j:j+minSize]
        #     if word in counts:
        #         counts[word]+=1
        #     else:
        #         if len(collections.Counter(word))<=maxLetters:
        #             counts[word]=1
        # return max(counts.values()) if len(counts)!=0 else 0

        # Solution 3
        # res = 0
        # dic = collections.defaultdict(int)
        # for i in range(len(s)-minSize+1):
        #     tempStr = s[i:i+minSize]
        #     mySet = set(tempStr)
        #     if len(mySet) <= maxLetters:
        #         dic[tempStr] += 1
        #         res = max(res, dic[tempStr])        
        # return res