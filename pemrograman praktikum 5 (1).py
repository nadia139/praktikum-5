# Program untuk menambahkan data ke dalam sebuah list

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    # Meminta input dari user
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai_tugas = float(input("Nilai Tugas: "))
    nilai_uts = float(input("Nilai UTS: "))
    nilai_uas = float(input("Nilai UAS: "))
    
    # Menghitung nilai akhir
    nilai_akhir = (0.3 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)
    
    # Menambahkan data ke list data_mahasiswa
    data_mahasiswa.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": nilai_tugas,
        "UTS": nilai_uts,
        "UAS": nilai_uas,
        "Akhir": nilai_akhir
    })
    
    # Menanyakan apakah user ingin menambah data lagi
    tambah_data = input("Tambah data(y/t)? ")
    if tambah_data.lower() != 'y':
        break

# Menampilkan daftar data mahasiswa
print("\n| No | Nama      | NIM   | Tugas | UTS | UAS | Akhir |")
print("=======================================================")
for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"| {i:<2} | {mhs['Nama']:<9} | {mhs['NIM']:<5} | {mhs['Tugas']:<5} | {mhs['UTS']:<3} | {mhs['UAS']:<3} | {mhs['Akhir']:.2f} |")