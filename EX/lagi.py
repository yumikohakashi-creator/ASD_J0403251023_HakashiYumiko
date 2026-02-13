# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Hakashi Yumiko Masfat
# NIM   : J0403251023
# Kelas : A2
# ==========================================================

# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 

# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 
def baca_stok(nama_file):
    """ 
    Membaca data stok dari file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 

    Output: - stok_dict (dictionary) 
    key   = kode_barang 
    value = {"nama": nama_barang, "stok": stok_int}     
    """
    stock_dict = {}

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # ilangin newline dan spasi
            kode_barang, nama_barang, stok = baris.split(",")
            stock_dict[kode_barang] = {"nama": nama_barang, "stok": int(stok)}

        return stock_dict


# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 
def simpan_stok(nama_file, stok_dict): 
    """ 
    Menyimpan seluruh data stok ke file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    """ 
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode_barang in stok_dict:
            nama_barang = stok_dict[kode_barang]["nama"]
            stok = stok_dict[kode_barang]["stok"] 
            baris = f"{kode_barang},{nama_barang},{stok}\n" 
            file.write(baris)
    pass


# ------------------------------- 
# Fungsi: Menampilkan semua data 
# ------------------------------- 
def tampilkan_semua(stok_dict): 
    """ 
    Menampilkan semua barang di stok_dict. 
    """ 
    for kode_barang in stok_dict:
        nama_barang = stok_dict[kode_barang]["nama"]
        stok = stok_dict[kode_barang]["stok"]
        print(f"Kode: {kode_barang} | Nama: {nama_barang} | Stok: {stok}")

    if not stok_dict:
        print("Stok barang kosong.")
    pass


# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 
def cari_barang(stok_dict): 
    """ 
    Mencari barang berdasarkan kode barang. 
    """ 
    kode = input("Masukkan kode barang: ").strip() 

    if kode in stok_dict:
        nama_barang = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"Kode: {kode} | Nama: {nama_barang} | Stok: {stok}")
    else:
        print("Barang tidak ditemukan.")
    pass


# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict): 
    """ 
    Menambah barang baru ke stok_dict. 
    """ 
    kode = input("Masukkan kode barang baru: ").strip() 
    nama = input("Masukkan nama barang: ").strip()

    if kode in stok_dict:
        print("'Kode sudah digunakan.")
        return
    try:
        stok_awal = int(input("Masukkan stok awal (angka): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Proses penambahan dibatalkan.")
        return
    pass


# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 
def update_stok(stok_dict): 
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """ 
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip() 
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan. Proses update dibatalkan.")
        return
    
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 
 
    pilihan = input("Masukkan pilihan (1/2): ").strip() 

    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah: "))
        stok_dict[kode]["stok"] += jumlah
        return
    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah: "))
        stok_dict[kode]["stok"] -= jumlah
        return
    elif pilihan not in ["1", "2"]:
        print("Pilihan tidak valid. Proses update dibatalkan.")
    else:
        print("Pilihan tidak valid. Proses update dibatalkan.")
        return
    pass


# ------------------------------- 
# Program Utama 
# ------------------------------- 
def main(): 
    # Membaca data dari file saat program mulai 
    stok_barang = baca_stok(NAMA_FILE) 
 
    while True: 
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok_barang) 
            print("Data berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 

# Menjalankan program utama 
if __name__ == "__main__": 
    main()