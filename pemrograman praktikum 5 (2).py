# Membuat list dengan input manual
list_a = []
for i in range(5):
    nilai = input(f"Masukkan nilai untuk elemen ke-{i + 1}: ")
    list_a.append(nilai)

# Akses list (A)
# Tampilkan elemen ke 3
print("Elemen ke-3:", list_a[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4
print("Elemen ke-2 sampai ke-4:", list_a[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", list_a[-1])

# Ubah elemen list (B)
# Ubah elemen ke 4 dengan nilai lainnya
list_a[3] = input("Masukkan nilai baru untuk elemen ke-4: ")
print("List setelah mengubah elemen ke-4:", list_a)

# Ubah elemen ke 4 sampai dengan elemen terakhir
for i in range(3, len(list_a)):
    list_a[i] = input(f"Masukkan nilai baru untuk elemen ke-{i + 1}: ")
print("List setelah mengubah elemen ke-4 sampai terakhir:", list_a)

# Tambah elemen list (C)
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
list_b = list_a[1:3]
print("List B (elemen ke-2 dan ke-3 dari list A):", list_b)

# Tambah list B dengan nilai string
list_b.append("Nilai Tambahan")
print("List B setelah ditambah string:", list_b)

# Tambah list B dengan 3 nilai
for i in range(3):
    nilai = input(f"Masukkan nilai tambahan ke-{i + 1} untuk list B: ")
    list_b.append(nilai)
print("List B setelah ditambah 3 nilai:", list_b)

# Gabungkan list B dengan list A
list_gabungan = list_a + list_b
print("List gabungan A dan B:", list_gabungan)# Membuat list dengan input manual
list_a = []
for i in range(5):
    nilai = input(f"Masukkan nilai untuk elemen ke-{i + 1}: ")
    list_a.append(nilai)

# Akses list (A)
# Tampilkan elemen ke 3
print("Elemen ke-3:", list_a[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4
print("Elemen ke-2 sampai ke-4:", list_a[1:4])

# Ambil elemen terakhir
print("Elemen terakhir:", list_a[-1])

# Ubah elemen list (B)
# Ubah elemen ke 4 dengan nilai lainnya
list_a[3] = input("Masukkan nilai baru untuk elemen ke-4: ")
print("List setelah mengubah elemen ke-4:", list_a)

# Ubah elemen ke 4 sampai dengan elemen terakhir
for i in range(3, len(list_a)):
    list_a[i] = input(f"Masukkan nilai baru untuk elemen ke-{i + 1}: ")
print("List setelah mengubah elemen ke-4 sampai terakhir:", list_a)

# Tambah elemen list (C)
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
list_b = list_a[1:3]
print("List B (elemen ke-2 dan ke-3 dari list A):", list_b)

# Tambah list B dengan nilai string
list_b.append("Nilai Tambahan")
print("List B setelah ditambah string:", list_b)

# Tambah list B dengan 3 nilai
for i in range(3):
    nilai = input(f"Masukkan nilai tambahan ke-{i + 1} untuk list B: ")
    list_b.append(nilai)
print("List B setelah ditambah 3 nilai:", list_b)

# Gabungkan list B dengan list A
list_gabungan = list_a + list_b
print("List gabungan A dan B:",list_gabungan)