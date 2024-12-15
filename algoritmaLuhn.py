def calculate_check_digit(imei):
    imei_base = list(map(int, imei))
    for i in range(len(imei_base) - 1, -1, -2):
        imei_base[i] *= 2
        if imei_base[i] > 9:
            imei_base[i] -= 9
    total = sum(imei_base)
    return (10 - (total % 10)) % 10


imei_partial = "013039003900060"
check_digit = calculate_check_digit(imei_partial)
imei = imei_partial + str(check_digit)
print(f"IMEI lengkap: {imei}")
