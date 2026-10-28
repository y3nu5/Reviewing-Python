print (
'''
=============================
APLIKASI KEUANGAN SEDERHANA
=============================
'''
)

nama_pengeluaran =[]
nominal_pengeluaran = []

def tambah_pengeluaran(nama, nominal):
    nama_pengeluaran.append(nama)
    nominal_pengeluaran.append(nominal)

def lihat_total_pengeluaran():
    total_pengeluaran = 0

    for nominal in nominal_pengeluaran:
        total_pengeluaran += nominal

    print("Total Pengeluaran: ", total_pengeluaran)

run_app = True

while run_app:
    print("1. Tambah Pengeluaran")
    print("2. Lihat Total Pengeluaran")
    print("3. Keluar")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 3:
        run_app = False
    elif pilihan == 1:
        nama = input("Masukkan nama pengeluaran: ")
        nominal = int(input("Masukkan nominal pengeluaran: "))
        tambah_pengeluaran(nama, nominal)
    else:
        lihat_total_pengeluaran()

        # total_pengeluaran = sum(nominal_pengeluaran)
        # print("Total Pengeluaran: ", total_pengeluaran)
        