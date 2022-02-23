#Cho phép nhân ab x 4 = b4 tìm a b ?
for a in range(10):
    for b in range(10):
        if ((a*10+b)*4)==(b*10+4):
            print(a,b)
            print(f"a={a}")
            print(f"b={b}")
