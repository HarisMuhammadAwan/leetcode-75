class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 1. Find max (O(N) time, O(1) space)
        max_candy = max(candies)
        
        # 2. Overwrite the input list directly
        for i in range(len(candies)):
            # Replace the integer at index 'i' with a boolean
            candies[i] = (candies[i] + extraCandies >= max_candy)
            
        # 3. Return the modified input list
        return candies