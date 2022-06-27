a=input("請輸入值為:").split(",")
c=""
d=""
a.sort()
max= sorted(a, reverse = True)
for i in a:
    c+=i
print(c)

for i in max:
    d+=i
print(d)
e=int(d)-int(c)
print("最大值數列與最小值數列差值為:",e)



