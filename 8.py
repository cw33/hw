a=int(input("輸入第一行正整數為:")) 
b=input("第二行中數列中的數字為:").split(" ")
c=""
for i in range(1,a+1):
    for i in b:  
        c+=i
        if c.count>=1:
            print("每個數字都剛好出現一次")