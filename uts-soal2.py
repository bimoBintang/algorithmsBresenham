import cv2
import numpy as np
import matplotlib.pyplot as plt

# Baca gambar
image_path = 'gaun.jpg'  # Path gambar yang diunggah
image = cv2.imread(image_path)  # Baca gambar sebagai array
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konversi ke RGB

# Tampilkan gambar untuk referensi
plt.imshow(image_rgb)
plt.title("Gambar Gaun")
plt.axis("off")
plt.show()

def get_average_color(image, x_start, y_start, width, height):
    h, w, _ = image.shape
    x_end = min(x_start + width, w)
    y_end = min(y_start + height, h)
    
    # Pastikan koordinat awal dan akhir berada dalam batas gambar
    if x_start >= w or y_start >= h:
        raise ValueError("Koordinat awal atau ukuran area berada di luar batas gambar")
    
    area = image[y_start:y_end, x_start:x_end]
    avg_color_per_row = np.average(area, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    return avg_color

# Koordinat area yang diambil (disesuaikan agar berada dalam batas gambar)
samples = [
    get_average_color(image_rgb, 20, 30, 50, 50),
    get_average_color(image_rgb, 60, 70, 50, 50),
    get_average_color(image_rgb, 120, 150, 50, 50),
    get_average_color(image_rgb, 180, 200, 50, 50),
    get_average_color(image_rgb, 20, 30, 100, 100),  # Sesuaikan ukuran agar tidak melebihi batas
    get_average_color(image_rgb, 110, 160, 80, 80),
    get_average_color(image_rgb, 200, 50, 40, 40),
    get_average_color(image_rgb, 80, 200, 60, 60),
    get_average_color(image_rgb, 150, 250, 60, 60),
    get_average_color(image_rgb, 220, 300, 20, 20),
    get_average_color(image_rgb, 90, 110, 80, 80),
    get_average_color(image_rgb, 180, 200, 70, 70),
    get_average_color(image_rgb, 120, 180, 100, 100),
    get_average_color(image_rgb, 70, 120, 50, 50),
    get_average_color(image_rgb, 160, 240, 50, 50),
    get_average_color(image_rgb, 140, 180, 60, 60),
    get_average_color(image_rgb, 180, 240, 40, 40),
    get_average_color(image_rgb, 240, 150, 20, 20),
]

# Hitung rata-rata RGB dari semua area yang diambil
average_color_rgb = np.mean(samples, axis=0)

# Tampilkan hasil
print("Warna rata-rata RGB gaun:", average_color_rgb)

# Konversi rata-rata warna RGB ke HSV
average_color_hsv = cv2.cvtColor(np.uint8([[average_color_rgb]]), cv2.COLOR_RGB2HSV)[0][0]

# Tentukan kategori warna berdasarkan nilai rata-rata HSV
if average_color_hsv[0] < 50 and average_color_hsv[2] > 200:  # Aturan untuk warna putih-emas
    print("Kesimpulan: Gaun terlihat putih dan emas.")
else:  # Aturan untuk warna biru-hitam
    print("Kesimpulan: Gaun terlihat biru dan hitam.")
