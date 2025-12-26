class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy = max(candies)  
        for x in candies:
            result.append((x + extraCandies) >= max_candy)
        return result