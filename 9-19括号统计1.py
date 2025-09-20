T =int(input("请输入数字"))

s=''
while(T):
    T-=1
    ba=0
    swap=0
    s=list(input())
    for i in range(len(s)):
        if s[i]=='(':
            ba+=1
        else:
            ba-=1
        if ba<0:
            for j in range(i+1,len(s)):
                if s[j]=='(':
                    swap+=j-i
                    s[i]=s[j]
                    for x in range(j,i):
                        s[x]=s[x-1]
                    ba+=2
    print(swap)
            
    
