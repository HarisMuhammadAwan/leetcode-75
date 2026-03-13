class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        length = len(flowerbed)
        
        while i < length:
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == length-1) or (flowerbed[i+1] == 0)
                
                if left_empty and right_empty:
                    count += 1
                    flowerbed[i] = 1
                    i += 1
            i += 1
        
        return count >= n