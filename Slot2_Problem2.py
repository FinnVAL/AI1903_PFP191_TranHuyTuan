try:
    x = float(input("Nhập điểm: "))
    if x>10:
        x=float(input("Nhập lại điểm bé hơn 10: "))
    if 8.5<= x <= 10:
        print('Điểm chữ: A')
        print('Điểm hệ 4: 4')
    if 7.0<=x<=8.4:
        print('Điểm chữ: B')
        print('Điểm hệ 4: 3')
    if 5.5<=x<=6.9:
        print('Điểm chữ: C')
        print('Điểm hệ 4: 2')
    if 4.0<=x<=5.4:
        print('Điểm chữ: D')
        print('Điểm hệ 4: 1')
    if x<4.0:
        print('Điểm chữ: F')
        print('Điểm hệ 4: 0')
except:
    print("Nhập một điểm số thực")
