class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        k=max(piles)
        while low<=high:
            mid=(low+high)//2
            hours=0
            for p in piles:
                hours+=math.ceil(p/mid)
            if hours<=h:
                k=min(k,mid)
                high=mid-1
            else:
                low=mid+1
        return k
                
