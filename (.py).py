uku = {
    "judul": "LASKAR PELANGI",
    "penulis": "Andrea Hirata",
    "tahun_terbit": 2005
}

while True:
    print("DATA BUKU")
    print("1. Tampilkan")
    print("2. Tambah penerbit")
    print("3. Ubah penulis")
    print("4. Hapus penerbit")
    print("5. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        for key, value in buku.items():
            print(key, ":", value)

    elif pilihan == "2":
        buku["penerbit"] = input("Penerbit: ")
        print("Penerbit ditambahkan")

    elif pilihan == "3":
        buku["penulis"] = input("Penulis baru: ")
        print("Penulis diubah")

    elif pilihan == "4":
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Penerbit dihapus")

    elif pilihan == "5":
        break

    else:
        print("Pilihan salah")

print("DATA BUKU SETELAH PERUBAHAN")
for key, value in buku.items():
    print(key, ":", value)