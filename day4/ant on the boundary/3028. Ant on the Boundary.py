class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count =0
        boundary=0
        for i in nums:
            boundary+=i
            if boundary==0:
                count+=1
        return count