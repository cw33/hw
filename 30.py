ans=input("輸入數字")
que=input("輸入數字")
a=0
b=0
for i in que:
    for j in ans:
        if  i==j:
            if que.index(i)==ans.index(j):
                a=a+1
            else:
                b=b+1
if a==4:
    print(str(a)+"A"+str(b)+"B"+"全對") 
else:
    print(str(a)+"A"+str(b)+"B"+"加油") 