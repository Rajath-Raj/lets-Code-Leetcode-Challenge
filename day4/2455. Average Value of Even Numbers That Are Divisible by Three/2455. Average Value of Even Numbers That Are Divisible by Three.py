class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum=0
        n=0
        for i in nums:
            if i%6==0:
                sum+=i
                n+=1
        if n==0:
            return 0
        avg=int(sum/n)
        return avg