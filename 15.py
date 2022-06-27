a=input("輸入一組四位數字為:")
for i in a:
    b=(int(a[0])+7)%10
    c=(int(a[1])+7)%10
    d=(int(a[2])+7)%10
    e=(int(a[3])+7)%10
x=b
y=c
b=d
c=e
d=x
e=y

print("輸出加密後的數字為",b,c,d,e)