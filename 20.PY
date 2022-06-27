a=int(input("輸入組數為"))
for i  in range(a):
    b=input("第"+str(i+1)+"組:").split(" ")
    d=int(b[0])*250+int(b[1])*175
    print("第"+str(i+1)+"組應收費用:",str(d))
    