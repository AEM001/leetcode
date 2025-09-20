class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t=1
        cur=len(digits)-1
        while t!=0 and cur>=0:
            t=(t+digits[cur])//10
            digits[cur]=(t+digits[cur])%10
            
            cur-=1
        if t!=0:
            digits=[t]+digits
        return digits


            

