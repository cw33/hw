k = {}
l = []

def usingKey():
    k["金"] = input("金")
    k["銀"] = input("銀")
    k["銅"] = input("銅")
    k["優"] = input("優")

    print("金牌得到{}".format(k["金"]))
    print("銀牌得到{}".format(k["銀"]))
    print("銅牌得到{}".format(k["銅"]))
    print("優牌得到{}".format(k["優"]))


def usingList():
    l.append(input("金"))
    l.append(input("銀"))
    l.append(input("銅"))
    l.append(input("優"))
    print("金牌得到{}".format(l[0]))
    print("銀牌得到{}".format(l[1]))
    print("銅牌得到{}".format(l[2]))
    print("優牌得到{}".format(l[3]))


if(input("處理方式:(1)字典(2)串列") == "1"):
    usingKey()
else:
    usingList()