# 792. Number of Matching Subsequences

# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        lookup = defaultdict(list)
        output = 0
        
        for i, c in enumerate(s):
            lookup[c].append(i)
            
        def bs(lst, i):
            l, r = 0, len(lst)
            while l < r:
                mid = (l + r) // 2
                if i < lst[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l
        for w in words:
            prev = -1
            found = True
            for c in w:
                tmp = bs(lookup[c], prev)
                if tmp == len(lookup[c]):
                    found = False
                    break
                else:
                    prev = lookup[c][tmp]
            if found:
                output += 1
        return output

        # Solution 2
        # word_dict = defaultdict(list)
        # count = 0
        
        # for word in words:
        #     word_dict[word[0]].append(word)            
        
        # for char in s:
        #     words_expecting_char = word_dict[char]
        #     word_dict[char] = []
        #     for word in words_expecting_char:
        #         if len(word) == 1:
        #             # Finished subsequence! 
        #             count += 1
        #         else:
        #             word_dict[word[1]].append(word[1:])
        
        # return count