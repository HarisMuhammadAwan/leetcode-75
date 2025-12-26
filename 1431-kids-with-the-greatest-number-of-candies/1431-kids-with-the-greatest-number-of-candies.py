class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy = max(candies)  
        for x in candies:
            temp = x + extraCandies
            result.append(bool(temp >= max_candy))
        return result