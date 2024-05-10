class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        low, high = max(weights), sum(weights)
        
        while low < high:
            mid = low + (high - low) // 2
            current = 0
            days = 1
            for w in weights:
                if current + w > mid:
                    days += 1
                    current = 0
                current += w
            
            if days >D:
                low = mid +1 
            else:
                high = mid
            
        return low