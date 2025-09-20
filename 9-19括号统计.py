T =int(input("请输入数字"))

s=''
while(T):
    T-=1
    lcnt,rcnt,acnt=0,0,0
    s=input("请输入一串括号字符串")
    for i in s:
        if i=='(':
            if rcnt:
                acnt+=rcnt
                rcnt-=1
            else:
                lcnt+=1
        else:
            if lcnt:
                lcnt-=1
            else:
                rcnt+=1
    print(acnt)
            
    
