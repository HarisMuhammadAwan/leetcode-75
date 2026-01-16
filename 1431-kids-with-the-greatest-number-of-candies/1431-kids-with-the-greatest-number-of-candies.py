class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        largest = max(candies)
        for i in candies:
            result.append ((i + extraCandies) >= largest)
        return result