class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []  
        for x in candies:
            temp = x + extraCandies
            n = 1
            for y in candies: 
                if(temp < y): 
                    n = 0
            result.append(bool(n))
        return result