class Solution:
    def maxDepth(self, s: str) -> int:
        string=list(s)
        count=0
        max=0
        temp=0
        for i in string:
                if i=='(':
                    count+=1
                elif i==')' and count>0:
                    if max<count:
                        max=count
                    count-=1
        return max

                
