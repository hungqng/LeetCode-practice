# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)

        # Solution 2
        # vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
        # return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)

        # Solution 3 two pointers
        # s = list(s)
        # vows = set('aeiouAEIOU')
        # l, r = 0, len(s) - 1
        # while l <= r:
        #     while l <= r and s[l] not in vows: l += 1
        #     while l <= r and s[r] not in vows: r -= 1
        #     if l > r: break
        #     s[l], s[r] = s[r], s[l]
        #     l, r = l + 1, r - 1
        # return ''.join(s)

        # Solution 4 Two pointers using stack
        # vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # L = list(s)
        # i = 0
        # j = len(L) - 1
        # while i < j:
        #     while i < j and L[i] not in vowels:
        #         i += 1
        #     while j > i and L[j] not in vowels:
        #         j -= 1
        #     L[i], L[j] = L[j], L[i] 
        #     i += 1
        #     j -= 1
        # return ''.join(L)