# 500. Keyboard Row

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                res.append(word)
        return res

        # Solution 2
        return filter(lambda word:
                        set(word.lower()) - set("qwertyuiop") == set() or
                        set(word.lower()) - set("asdfghjkl") == set() or
                        set(word.lower()) - set("zxcvbnm") == set(),
                    words)