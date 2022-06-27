s=5
ans=0
c=[]
for i in range(s):
    c.append(input())
    if c[i]=="a" or c[i]=="A":
        ans+=1
    elif c[i]=="2":
        ans+=2
    elif c[i]=="3":
        ans+=3
    elif c[i]=="4":
        ans+=4
    elif c[i]=="5":
        ans+=5
    elif c[i]=="6":
        ans+=6
    elif c[i]=="7":
        ans+=7
    elif c[i]=="8":
        ans+=8
    elif c[i]=="9":
        ans+=9
    elif c[i]=="10":
        ans+=10
    elif c[i]=="j" or c[i]=="J":
        ans=ans+11
    elif c[i]=="q" or c[i]=="Q":
        ans=ans+12
    elif c[i]=="k" or c[i]=="K":
        ans+=ans+13
print(ans)