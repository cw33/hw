a=input("輸入月租費型式及通話時間為:").split(",")
b=float(a[1])*0.08
if b> float(a[0]):
    c=b*0.7
else:
    c=b*0.8
print("通話費為:{0:.0f}".format(c))