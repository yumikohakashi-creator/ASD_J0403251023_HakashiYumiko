#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 1: Membuat Fungsi Load Data dari File
#=========================================

# variabel menyimpan data file
nama_file ="stok_barang.txt"

def baca_stok(nama_file):
    stok_dict = {} #inisialisai data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  #ambil data per baris dan hilangkan new line
            kode, nama, jumlah = baris.split(",") #ambil data per item data
            stok_dict[kode] = {"nama": nama, "jumlah": int(jumlah) }  #masukkan dalam dictionary
        return stok_dict
    
buka_stok = baca_stok(nama_file)  #memanggil load 
print ("jumlah stok terbaca", len(buka_stok))  #melihat berapa stok yang di load


#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 2: Membuat Fungsi Menampilkan Data
#=========================================

def tampilkan_stok(stok_dict):
    #membuat header tabel
    print ("\n===== STOK BARANG =====")
    print (f"{'NIM' : <10} | {'Nama': <12} | {'Nilai': >5}")  #untuk mengatur lebar kolom >rata kanan <rata kiri
    '''
    untuk  tampilan yang rapi, atur lebar kolom
    {KODE : <10} artinya nim raya kiri dengan lebar kolom 10 karakter
    {'Nama': <12} artinya nama rata kiri dengan lebar kolom 12 karakter
    {'JUMLAH': >5} artinya nilai rata kanan dengan lebar kolom 5 karakter
    '''
    print ('-'*32) #membuat garis

    #menampilkan 
    for kode in sorted(stok_dict):
        nama= stok_dict[kode]["nama"]
        jumlah = stok_dict[kode]["jumlah"]
        print (f"{kode:<10} | {nama: <12} | {int(jumlah):>5}")

#tampilkan_stok(buka_stok) #memanggil fungsi untuk menampilkan stok

#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 3: Membuat Mencari Data
#=========================================

#membuat fungsi pencarian data
def cari_stok(stok_dict):
    #pencarian stok berdasarkna kode sebagai key dictionary
    #membuat input kode barang yang akan dicari
    kode_cari = input("masukkan kode barang yang ingin dicari: ").strip()

    if kode_cari in stok_dict:
        nama = stok_dict[kode_cari]["nama"]
        jumlah = stok_dict [kode_cari]["jumlah"]

        print("===== stok barang ditemukan =====")
        print(f"KODE: {kode_cari}")
        print(f"NAMA: {nama}")
        print(f"JUMLAH: {jumlah}")
    else:
        print("stok tidak ditemukan. Pastikan kode yang dimasukkan benar")

#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 4: Membuat Update Data
#=========================================

#membuat fungsi update data
def ubah_stok(stok_dict):

    #awali dulu dengan mencari kode barang yang ingin di update
    kode = input ("Masukkan kode barang yang diubah datanya: ").strip()

    if kode not in stok_dict:
        print("kode tidak ditemukan. Update dibatalkan")
        return
    
    try:
        jumlah_baru = int(input("Masukkan jumlah baru 0-100: ").strip())
    except ValueError:
        print("jumlah harus berupa angka. Update Dibatalkan")
    
    if jumlah_baru < 0 or jumlah_baru >100:
        print("jumlah harus antara 0 sampai 100. Update Dibatalkan")

    jumlah_lama = stok_dict[kode]["jumlah"]
    stok_dict[kode]["jumlah"] = jumlah_baru

    print(f"Update Berhasil. jumlah {kode} berubah dari {jumlah_lama} menjadi {jumlah_baru}")

#memanggil fungsi udah data
#ubah_data(buka_data)

#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5: Membuat Fungsi Menyimpan Data pada File
#=========================================

#membuat fungsi menyimpan data ke file
def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            jumlah = stok_dict[kode]["jumlah"]
            file.write(f"{kode}, {nama}, {jumlah}")

#memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)
#print("\nData Berhasil Disimpan ke file:", nama_file)

#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5: Membuat Menu Interaktif
#=========================================

def main():  #fungsi yang dijalankan pertama kali
    #load data otomatis saat program dimulai
    buka_data = baca_stok(nama_file) 

    while True:
        print("\n==== STOK BARANG ====")
        print("1. Tampilkan Stok Barang")
        print("2. Cari Stok berdasarkan kode")
        print("3. Ubah Jumlah stok")
        print("4. Simpan Data ke File")
        print("5. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_stok(buka_stok)
        elif pilihan == "2":
            cari_stok(buka_stok)
        elif pilihan == "3":
            ubah_stok(buka_stok)
        elif pilihan == "4":
            simpan_stok(nama_file, buka_stok)
            print("Stok Berhasil Disimpan")
        elif pilihan == "5":
            print ("Program Selesai")
            break
        else:
            print("Pilihan Tidak Valid. Silahkan coba lagi")

if __name__ == "__main__":
    main() # Main 

