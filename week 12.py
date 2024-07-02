library = [
    {"Judul": "Kembara Rindu", "Penulis": "Habiburrahman El Shirazy", "Tahun": 2019, "Stok": 5},
    {"Judul": "Bumi Cinta", "Penulis": "Habiburrahman El Shirazy", "Tahun": 2010, "Stok": 3},
    {"Judul": "Suluh Rindu", "Penulis": "Habiburrahman El Shirazy", "Tahun": 2022, "Stok": 4},
    {"Judul": "Hujan", "Penulis": "Tere Liye", "Tahun": 2016, "Stok": 6},
    {"Judul": "Bumi", "Penulis": "Tere Liye", "Tahun": 2014, "Stok": 2},
    {"Judul": "Tentang Kamu", "Penulis": "Tere Liye", "Tahun": 2016, "Stok": 1},
    {"Judul": "Assalamualaikum Beijing", "Penulis": "Asma Nadia", "Tahun": 2013, "Stok": 3},
    {"Judul": "Rumah Tanpa Jendela", "Penulis": "Asma Nadia", "Tahun": 2011, "Stok": 5},
    {"Judul": "Cinta Diujung Sajadah", "Penulis": "Asma Nadia", "Tahun": 2008, "Stok": 2},
    {"Judul": "Geez and Ann", "Penulis": "Nadhifa Allya Tsana", "Tahun": 2020, "Stok": 4},
    {"Judul": "Kata", "Penulis": "Nadhifa Allya Tsana", "Tahun": 2018, "Stok": 3},
    {"Judul": "Masih Ingatkah Jalan Pulang", "Penulis": "Nadhifa Allya Tsana", "Tahun": 2020, "Stok": 2}
]

def tambah_buku():
    Judul = input("Masukkan Judul Buku: ")
    Penulis = input("Masukkan Penulis Buku: ")
    try:
        Tahun = int(input("Masukkan Tahun Buku: "))
        Stok = int(input("Masukkan Jumlah Stok Buku: "))
    except ValueError:
        print("Tahun dan Stok harus berupa angka!")
        return

    book = {"Judul": Judul, "Penulis": Penulis, "Tahun": Tahun, "Stok": Stok}
    library.append(book)
    print(f"Buku '{Judul}' berhasil ditambahkan ke Gudang Ilmu!")

def pencarian_buku(keyword):
    result = []
    for book in library:
        if keyword.lower() in book["Judul"].lower() or \
           keyword.lower() in book["Penulis"].lower() or \
           str(keyword) == str(book["Tahun"]):
            result.append(book)
    return result

def menampilkan_buku(books):
    if not books:
        print("Tidak ada buku yang ditemukan.")
    else:
        print("Buku yang ditemukan:")
        for book in books:
            print(f"Judul: {book['Judul']}, Penulis: {book['Penulis']}, Tahun: {book['Tahun']}, Stok: {book['Stok']}")

def main():
    while True:
        print("\nSelamat Datang di Gudang Ilmu!")
        print("Menu Gudang Ilmu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            print("\nPencarian Buku:")
            keyword = input("Masukkan kata kunci (Judul, Penulis, atau Tahun): ")
            result = pencarian_buku(keyword)
            menampilkan_buku(result)
        elif pilihan == "3":
            print("Terima kasih telah Mengunjungi Gudang Ilmu!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()