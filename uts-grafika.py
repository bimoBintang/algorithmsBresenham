import matplotlib.pyplot as plt

def calculate_file_size(width, height, color_depth):
    total_pixels = width * height
    bytes_per_pixel = color_depth / 8
    file_size_bytes = total_pixels * bytes_per_pixel 
    file_size_kb = file_size_bytes / 1024
    file_size_mb = file_size_kb / 1024
    
    return file_size_bytes, file_size_kb, file_size_mb

def show_file_size_plot(file_size_bytes, file_size_kb, file_size_mb):
    units = ['Bytes', 'Kilobytes', 'Megabytes']
    sizes = [file_size_bytes, file_size_kb, file_size_mb]

    plt.title("Ukuran File Gambar")
    plt.xlabel("Satuan Ukuran")
    plt.ylabel("Ukuran File")
    plt.grid(True)
    
    plt.bar(units, sizes, color=['blue', 'orange', 'green'])
    plt.text(0, file_size_bytes, f"{file_size_bytes:.2f} Bytes", ha='center', va='bottom')
    plt.text(1, file_size_kb, f"{file_size_kb:.2f} KB", ha='center', va='bottom')
    plt.text(2, file_size_mb, f"{file_size_mb:.2f} MB", ha='center', va='bottom')
    
    plt.show()

def main():
    width = int(input("Masukkan lebar gambar (dalam piksel): "))
    height = int(input("Masukkan tinggi gambar (dalam piksel): "))
    color_depth = int(input("Masukkan kedalaman warna (dalam bit, contoh: 24 untuk RGB): "))
    
    file_size_bytes, file_size_kb, file_size_mb = calculate_file_size(width, height, color_depth)

    print(f"=============================")
    print(f"Ukuran file dalam bytes: {file_size_bytes:.2f} Bytes")
    print(f"Ukuran file dalam kilobytes: {file_size_kb:.2f} KB")
    print(f"Ukuran file dalam megabytes: {file_size_mb:.2f} MB")
    
    show_file_size_plot(file_size_bytes, file_size_kb, file_size_mb)

if __name__ == "__main__":
    main()
