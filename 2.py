a=float(input("輸入電費"))
b=input("輸入是否為夏月")
if b=="是":
    if a<=120:
        s=a*2.1
        print("Summer months:%.2f"%(s))
    if a>=121 and a<=330:
        s=120*2.1+(a-120)*3.02
        print("Summer months:%.2f"%(s))
    if a>=331 and a<=500:
        s=120*2.1+210*3.02+(a-120-210)*4.39
        print("Summer months:%.2f"%(s))
    if a>=501 and a<=700:
        s=120*2.1+210*3.02+170*4.39+(a-120-210-170)*4.97
        print("Summer months:%.2f"%(s))
    if a>=701:
        s=120*2.1+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(a-120-210-170-200)*5.63
        print("Summer months:%.2f"%(s))
else:
    if a<=120:
        s=a*2.1
        print("Non-Summer months:%.2f"%(s))
    if a>=121 and a<=330:
        s=120*2.1+(a-120)*2.68
        print("Non-Summer months:%.2f"%(s))
    if a>=331 and a<=500:
        s=120*2.1+210*2.68+(a-120-210)*3.61
        print("Non-Summer months:%.2f"%(s))
    if a>=501 and a<=700:
        s=120*2.1+210*2.68+170*3.61+(a-120-210-170)*4.01
        print("Non-Summer months:%.2f"%(s))
    if a>=701:
        s=120*2.1+210*2.68+170*3.61+200*4.01+(a-120-210-170-200)*4.5
        print("Non-Summer months:%.2f"%(s))
  