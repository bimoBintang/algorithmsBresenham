import matplotlib.pyplot as plt
plt.title("Bresenham Algortima")
plt.xlabel("X Aksi")
plt.ylabel("Y Aksi")
plt.grid(True)

def bres(x1,y1,x2,y2):

    # titik untuk menghitung awal dx, dy
    x,y = x1,y1
    dx= abs(x2- x1)
    dy= abs(y2 -y1)
    gradient =  dy/float(dx)

    # mentukar x dengan y agar algortima lebih akurat 
    if gradient > 1:
        dx, dy = dy, dx
        x,y = y,x
        x1,y1 = y1, x1
        x2,y2 = y2, x2

    # parameter keputusan
    p = 2 * dy - dx
    print(f"x= {x}, y= {y}")

    # menyimpan kordinat yang disesuikan
    xCordinates = [x]
    yCordinates = [y]
    # Looping mengambil gambar garis
    for k in range(2, dx +2):
        if p > 0:
            y = y + 1 if y < y2 else y -1
            p = p + 2 * (dy -dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x -1

        print(f"x= {x}, y= {y}")
        xCordinates.append(x)
        yCordinates.append(y)

    plt.plot(xCordinates, yCordinates, marker='o')
    plt.show()

def main():
    x1 = int(input("Enter starting of X: "))
    y1 = int(input("Enter starting of y: "))
    x2 = int(input("Enter starting of x: "))
    y2 = int(input("Enter starting of y: "))

    bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()