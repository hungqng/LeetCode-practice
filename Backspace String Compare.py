# 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S_out, T_out = [], []
        
        for char in s:
            if char == '#':
                if S_out:
                    S_out.pop()
            else:
                S_out.append(char)
        for char in t:
            if char == '#':
                if T_out:
                    T_out.pop()
            else:
                T_out.append(char)
                
        if S_out == T_out:
            return True
        else:
            return False