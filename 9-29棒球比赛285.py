from typing import List
class Solution:
    def calPoints(self, operations:List[str]) -> int:
        get=[]
        for i in operations:
            if i =="+":
                get.append(get[-1]+get[-2])
            elif i=="D":
                get.append(get[-1]*2)
            elif i=="C":
                get.pop()
            else:
                if int(i)>=-3E4 and int(i)<=3E4:
                    get.append(int(i))
        return sum(get)
         