print(f"MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG")

panjang = float(input("Masukan panjang dalam satuan meter : "))
lebar = float(input("Masukan lebar dalam satuan meter   : "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas                               : { luas } m2")
print(f"Keliling                           : { keliling } m")


# Trace table:

# +---------|-------|------|----------+
# | Panjang | Lebar | Luas | Keliling |
# +---------|-------|------|----------+
# | 8       | 5     | -    | -        |
# | 8       | 5     | 40   | -        |
# | 8       | 5     | 40   | 26       |
# +---------|-------|------|----------+