f = input("Nhập vào 1 dãy số: ")
if len(f) == 0:
    print("Dãy số trống")
else:
    try:
        n = list(map(int,f.split()))
        unique = set(n)
        result = list(unique)
        result.sort()
        print (result)
    except:
        print("Nhập một dãy số nguyên.")
