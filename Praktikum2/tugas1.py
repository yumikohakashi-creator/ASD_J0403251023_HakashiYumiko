# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Hakashi Yumiko Masfat
# NIM : J0403251023
# Kelas : TPL A2
# ==========================================================
# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    """
    stok = {} #inisialisai data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  #ambil data per baris dan hilangkan new line
            kode, nama, jumlah = baris.split(",") #ambil data per item data
            stok[kode] = {"nama": nama, "stok": int(jumlah) }  #masukkan dalam dictionary
        return stok
    
buka_data = baca_stok(nama_file)  #memanggil load 
print ("jumlah stok terbaca", len(buka_data))  #melihat berapa data yang di load

# -------------------------------a
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    # Tulis ulang seluruh isi file berdasarkan stok_dict
    # Hint: with open(nama_file, "w", encoding="utf-8") as f:
    pass
# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """
    if not stok_dict:
        print("\n stok barang masih kosong")
        return
    print("\n" + "=" *40)
    print(f"{'KODE': <10} | {'NAMA BARANG': <15} | {'STOK': >5}")
    print("-"*40)
    for kode in sorted(stok_dict):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<10} | {nama: <15} | {stok: >5}")
    print("="*40)
# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode = input("Masukkan kode barang: ").strip()
    if kode in stok_dict: #Cek apakah kode ada di dictionary
        barang = stok_dict[kode]
        print("\n--- Detail Barang ---")
        print(f"Nama : {barang['nama']}")
        print(f"Stok : {barang['stok']}")
    else:
        print("\n[!] barang tidak ditemukan.")
    # Jika ada: tampilkan detail barang
    # Jika tidak ada: tampilkan 'Barang tidak ditemukan'

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """
    kode = input("Masukkan kode barang baru: ").strip()
    if kode in stok_dict: #Validasi kode tidak boleh duplikat
        print("Kode sudah digunakan. Tambah barang gagal") # Jika sudah ada: tampilkan 'Kode sudah digunakan' dan return
        return
    nama = input("Masukkan nama barang: ").strip()
    try: 
        stok_awal = int(input("masukkan stok awal (angka): ")) #Input stok awal (integer)
        stok_dict[kode] = {"nama": nama, "stok": stok_awal} # Simpan ke dictionary
        print(f"barang {nama} berhasil ditambahkan")
    except ValueError:
        print("stok harus berupa angka!")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    if kode not in stok_dict: #Cek apakah kode ada di dictionary
        print("barang tidak ditemukan")
        return # Jika tidak ada: tampilkan pesan dan return
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    try: #Input jumlah perubahan stok
        jumlah = int(input("masukkan jumlah: "))
        if pilihan =="1":  # - Jika pilihan 1: stok = stok + jumlah
            stok_dict[kode]['stok'] += jumlah
            print("update berhasil")
        elif pilihan == "2":  # - Jika pilihan 2: stok = stok - jumlah
            if stok_dict[kode]['stok'] - jumlah <0:
                print("stok tidak mencukupi")
            else:
                stok_dict[kode]['stok']-= jumlah
                print("update berhasil")
        else: # - Jika hasil < 0: batalkan dan tampilkan error
            print("pilihan tidak valid")
    except ValueError: 
        print("masukkan angka yan valid")
    pass

# -------------------------------
# Program Utama
# -------------------------------
def main():
    # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)

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
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()