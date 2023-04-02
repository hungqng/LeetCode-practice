class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minDegree = (minutes/60.0)*360
        hourDegree = ((hour + minutes/60)/12.0)*360 % 360
        answer = abs(minDegree - hourDegree);
        if (answer > 180):
            return 360 - answer
        else:
            return answer