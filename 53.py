a=int(input("輸入n值"))
b=[]
c=[]
for i  in range(a):
    b.append(input("請輸入姓名:"))
    c.append(input("請輸入電子郵件:"))
  
d=input("請輸入要查詢電子郵件的姓名:")
for  j in range(a):
    if d==b[j]:
        print(b[j],"電子郵件帳號為",c[j])
    
    