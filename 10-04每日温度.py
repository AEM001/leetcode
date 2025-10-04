class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[]
        search=dict()
        for ind,i in emumarate(temperatures):
            
            while stack and i>stack[-1]:
                search[stack[-1]]=count
                count+=1
                stack.pop()
            stack.append(i)
        for i in temperatures:
            res.append(search.get(i, -1))
        return res

