f = input("Nhập vào 1 dãy số: ")
n = list(map(int,f.split()))
if len(f) == 0:
    print("Dãy số trống")
else:
    try:
        unique = set(n)
        result = list(unique)
        result.sort()
        print (result)
    except:
        print("Nhập một dãy số nguyên.")
