# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()

        # Solution 2 hashmap
        hashmap = {}
        for st in strs:
            key = ''.join(sorted(st))
            if key not in hashmap:
                hashmap[key] = [st]
            else:
                hashmap[key] += [st]
        return hashmap.values()

        # Solution 3 defaultdict to collect groups
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return map(sorted, groups.values())