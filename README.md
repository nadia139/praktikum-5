PENJELASAN FLOWCHART: 

Flowchart di atas menggambarkan langkah-langkah untuk menginput dan menghitung nilai akhir mahasiswa
1. Mulai: Program dimulai.
2. Inisialisasi Data = []: Sebuah list kosong dibuat untuk menyimpan data mahasiswa.
3. Input Data Mahasiswa: Program meminta pengguna untuk memasukkan data mahasiswa.
Masukkan Nama: Pengguna memasukkan nama mahasiswa.
Masukkan NIM: Pengguna memasukkan Nomor Induk Mahasiswa (NIM).
Masukkan Nilai Tugas: Pengguna memasukkan nilai tugas mahasiswa.
Masukkan Nilai UTS: Pengguna memasukkan nilai UTS mahasiswa.
Masukkan Nilai UAS: Pengguna memasukkan nilai UAS mahasiswa.
4. Hitung Nilai Akhir: Nilai akhir dihitung berdasarkan formula:
\text{Nilai Akhir} = (\text{Tugas} \times 30\%) + (\text{UTS} \times 35\%) + (\text{UAS} \times 35\%)
5. Tambah Data Lagi? (y/t): Program menanyakan apakah pengguna ingin menambah data mahasiswa lagi.
Jika y (ya), maka kembali ke proses input data mahasiswa.
Jika t (tidak), program akan melanjutkan ke langkah berikutnya.
6. Cetak Garis Pembatas: Program mencetak garis pembatas sepanjang 50 karakter.
7. Cetak Header Tabel: Program mencetak header tabel dengan kolom: No | Nama | NIM | Tugas | UTS | UAS | Akhir.
8. Loop Data dengan enumerate: Program melakukan loop pada list data menggunakan enumerate untuk mencetak setiap data mahasiswa.
Cetak Data: Program mencetak:
Nomor urut
Nama
NIM
Nilai Tugas
Nilai UTS
Nilai UAS
Nilai Akhir (dengan 2 desimal)
9. Cetak Garis Pembatas: Program mencetak garis pembatas sekali lagi.
10. Selesai: Program berakhir.
Flowchart ini membantu mengorganisasi proses input, perhitungan, dan tampilan data mahasiswa dalam bentuk tabel.

PENJELASAN HASIL DARI CODE SATU:

<img width="302" alt="hasil pemrograman 1" src="https://github.com/user-attachments/assets/9453c2f5-f923-45fd-870b-23b4384ec198">



1. Input Data:
Pertama, kamu diminta untuk memasukkan Nama, NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS.

Setelah memasukkan data, program akan menghitung Nilai Akhir, yang kemungkinan diambil dari rata-rata atau perhitungan tertentu berdasarkan Nilai Tugas, UTS, dan UAS.
2. Hasil Tabel:
Setelah kamu selesai memasukkan data dan memilih untuk berhenti (dengan memasukkan 't' saat ditanya "Tambah data(y/t)?"), program akan menampilkan tabel yang berisi data mahasiswa yang sudah dimasukkan.
Kolom-kolom dalam tabel meliputi:

No: Nomor urut data.

Nama: Nama mahasiswa.

NIM: Nomor Induk Mahasiswa.

Tugas, UTS, UAS: Nilai dari masing-masing komponen.

Akhir: Nilai akhir berdasarkan perhitungan dari Tugas, UTS, dan UAS.
3. Contoh Data:
Dalam output terlihat dua mahasiswa dengan data sebagai berikut:
Mahasiswa pertama bernama "nadia" dengan NIM "312410258", Nilai Tugas 90, UTS 78, UAS 85, dan Nilai Akhir 84.05.
Mahasiswa kedua bernama "kevin" dengan NIM "312410347", Nilai Tugas 85, UTS 80, UAS 88, dan Nilai Akhir 84.30.
4. Kesimpulan:
Program ini digunakan untuk memasukkan data nilai mahasiswa dan menampilkannya dalam bentuk tabel dengan nilai akhir yang dihitung otomatis.


PENJELASAN CODE DUA:

<img width="403" alt="pemrograman pertemuan 9 code 2" src="https://github.com/user-attachments/assets/cd05532c-a60c-4cd7-a1c6-61f8da224f6c">


1. Membuat List Awal:
Kamu diminta memasukkan beberapa nilai untuk membentuk list awal. Nilai yang dimasukkan adalah 80, 70, 60, 50, dan 40, sehingga list awal menjadi [80, 70, 60, 50, 40].
2. Operasi pada List:
Program melakukan beberapa operasi pada list awal. Berikut adalah operasinya:
Menampilkan Elemen Tertentu: Elemen ke-2 hingga ke-4 ditampilkan sebagai [70, '60', '50'], dan elemen terakhir ditampilkan sebagai 40.
Mengubah Elemen: Kamu diminta memasukkan nilai baru untuk elemen ke-4 (90) dan ke-5 (100), sehingga list berubah menjadi [80, 70, 60, 90, 100].
Mengubah Elemen ke-4 hingga Terakhir: Elemen ke-4 hingga elemen terakhir diubah menjadi [70, 60, 90, 100, 90].
3. Operasi Tambahan pada List:
Menambah Elemen: Setelah mengubah elemen, program menambah elemen string "Nilai Tambahan" pada akhir list A, sehingga hasilnya adalah [70, 60, 90, 100, "Nilai Tambahan"].
Menambah Elemen pada List B: List B dibuat dengan elemen [70, 60], kemudian program menambahkan elemen 110, 120, dan 130 sehingga list B menjadi [70, 60, 110, 120, 130].
4. Menggabungkan List:
List A dan list B digabungkan, menghasilkan list gabungan [80, 70, 60, 90, 100, 'Nilai Tambahan', 110, 120, 130].
5. Pengulangan:
Setelah operasi-operasi tersebut, tampaknya program mengulang proses pengubahan nilai elemen dan penambahan elemen pada list, serta menggabungkan kembali list A dan B hingga hasilnya sama seperti langkah-langkah sebelumnya.
6. Kesimpulan:
Program ini menunjukkan bagaimana mengakses, mengubah, dan menambahkan elemen pada list, serta bagaimana menggabungkan dua list di Python.


