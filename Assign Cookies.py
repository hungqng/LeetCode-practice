# 455. Assign Cookies

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        childi = 0
        cookiei = 0
        
        while cookiei < len(s) and childi < len(g):
            if s[cookiei] >= g[childi]:
                childi += 1
            cookiei += 1
        return childi

        # Solution 2
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                j += 1
            i += 1
        return j

        # Solution 3
        gs,ss = sorted(g),sorted(s)
        c = 0
        while ss and gs:
            if ss[-1] >= gs[-1]:
                ss.pop()
                c += 1
            gs.pop()
        return c