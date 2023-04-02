# 1268. Search Suggestions System

# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = []
        products.sort()
        
        for i, c in enumerate(searchWord):
            tmp = []
            for p in products:
                if i < len(p) and c == p[i]:
                    tmp.append(p)
            output.append(tmp[:3])
            products = tmp
        return output
                    