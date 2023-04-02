# 433. Minimum Genetic Mutation

# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

# Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = []
        queue.append((start, 0))
        bankSet = set(bank)
        while queue:
            curr, step = queue.pop(0)
            if curr == end:
                return step
            for i in range(len(curr)):
                for c in "ACGT":
                    mutation = curr[:i] + c + curr[i + 1:]
                    if mutation in bankSet:
                        bankSet.remove(mutation)
                        queue.append((mutation, step + 1))
        return -1

        # Solution 2
        bank, v, q = set(bank), {start}, [(start, 0)]
        for g,k in q:
            for s in (g[:i] + cc + g[i+1:] for i,c in enumerate(g) for cc in 'ACGT'):
                if s in bank and s not in v:
                    if s==end:
                        return k+1
                    q.append((s, k+1))
                    v.add(s)
        return -1