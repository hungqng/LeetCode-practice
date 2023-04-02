# 30. Substring with Concatenation of All Words

# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        if not s or not words:
            return result
        word_map = Counter(words)
        word_size = len(words[0])
        num_word = len(words)
        list_size = word_size * num_word
        for i in range(len(s) - list_size + 1):
            seen = dict(word_map)
            word_used = 0
            for j in range(i, i + list_size, word_size):
                sub_str = s[j: j + word_size]
                if sub_str in seen and seen[sub_str] > 0:
                    seen[sub_str] -= 1
                    word_used += 1
                else:
                    break
            if word_used == num_word:
                result.append(i)
        return result

        # Solution 2
        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        i = 0
        ans = []

        # sliding window(s)
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0
        return ans