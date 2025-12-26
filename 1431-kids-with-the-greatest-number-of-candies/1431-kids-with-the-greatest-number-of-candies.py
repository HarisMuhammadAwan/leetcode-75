class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        i = 0  
        for x in candies:
            temp = candies[i] + extraCandies 
            j = 0
            n = 1
            for y in candies: 
                if(temp < candies[j]): 
                    n = 0
                j += 1 
            result.append(bool(n))
            i += 1
        return result