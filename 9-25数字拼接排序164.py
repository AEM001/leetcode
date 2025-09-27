class Solution:
    def crackPassword(self, password: List[int]) -> str:
        strlist=[str(i) for i in password]
        def compare(s1,s2):
            if s1+s2>s2+s1:
                return 1
            elif s1+s2<s2+s1:
                return -1
            else:
                return 0
        sorted_list=sorted(strlist,key=functools.cmp_to_key(compare))
        # for i in range(len(strlist)):
        #     for j in range(0,len(strlist)-1):
        #         if compare(strlist[j],strlist[j+1])>0:
        #             strlist[j],strlist[j+1]=strlist[j+1],strlist[j]
        #         else:
        #             continue
        return ''.join(sorted_list)
        
