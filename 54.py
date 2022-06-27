a=float(input("請輸入路程公里數(km)"))
if a<=1.5:
    print("所需車資為:75")
else:
    s=(a-1.5)*1000
    if s<=250:
            b=75+5
            print("所需車資為:",b)
    elif s>250:
            n=s//250
            b=75+5*(n+1)
            print("所需車資為:",b)
