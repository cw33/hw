a=str(["紅豆生南國春來發幾枝願君多采擷此物最相思"])
b=str(["春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少"])
c=[x for x in a for y in b if x==y]
print(c)
# print(set(a)&set(b))