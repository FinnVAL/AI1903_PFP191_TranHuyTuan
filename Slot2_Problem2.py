f = input("Nhập vào 1 dãy số thực: ").split()
sum = 0
if len(f) == 0:
    print("Dãy số trống")
else:
    try:
        n = list(map(float, f))
        m = len(n)
        for i in range(0, len(n)):
            sum = sum + float(n[i])
        avg = sum / m
        print ("Giá trị trung bình của dãy số là: ", avg )
        result = float(n[0])
        for i in n:
            if abs(float(i) - avg) < abs (result - avg):
                result = float(i)
        print("Giá trị gần nhất với giá trị trung bình của dãy số là: ", result)
        Vtri = [vt for vt in range(0, len(n)) if n[vt] == result]
        print("Vị trí của số đó trong dãy số là: ", Vtri)
    except:
        print("Nhập một dãy số thực")
