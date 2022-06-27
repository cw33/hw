ans=input("輸入第一組數字")
que=input("輸入第二組數字")
a=0
b=0
for i in range(len(que)):
    for j in range(len(ans)):
        if  i==j:
            if que.index(i)==ans.index(j):
                a=a+1
            else:
                b=b+1
print(a,"A",b,"B") 