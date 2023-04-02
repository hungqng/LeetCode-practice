# 492. Construct the Rectangle

# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

# The area of the rectangular web page you designed must equal to the given target area.
# The width W should not be larger than the length L, which means L >= W.
# The difference between length L and width W should be as small as possible.
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1

        # Solution 2
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        return area//w, w

        # Solution 3
        mid = int(math.sqrt(area))
        while area % mid != 0: mid -= 1
        return [int(area/mid),mid]

        # Solution 4
        for l in range(int(area**0.5), 0, -1):            
        if area % l == 0: 
            return [area // l, l]