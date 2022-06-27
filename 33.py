a=float(input("國文:"))
b=float(input("英文:"))
c=float(input("微積分:"))
d=float(input("體育:"))
q=float(input("程式設計:"))
e=[a,b,c,d,q]
avg=(a+b+c+d+q)/5
e.append(avg)

print("平均分數:%.2f"%avg)
print("最高分科目:%.0f"%e.index(max(e)))
print("最低分科目:%.0f"%min(e))

