#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 1: Membuat Fungsi Load Data dari File
#=========================================

# variabel menyimpan data file
nama_file ="data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisai data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai) }  #masukkan dalam dictionary
        return data_dict
    
buka_data = baca_data(nama_file)  #memanggil load 
print ("jumlah data terbaca", len(buka_data))  #melihat berapa data yang di load


#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 2: Membuat Fungsi Menampilkan Data
#=========================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print ("\n===== DAFTAR MAHASISWA =====")
    print (f"{'NIM' : <10} | {'Nama': <12} | {'Nilai': >5}")  #untuk mengatur lebar kolom >rata kanan <rata kiri
    '''
    untuk  tampilan yang rapi, atur lebar kolom
    {NIM : <10} artinya nim raya kiri dengan lebar kolom 10 karakter
    {'Nama': <12} artinya nama rata kiri dengan lebar kolom 12 karakter
    {'Nilai': >5} artinya nilai rata kanan dengan lebar kolom 5 karakter
    '''
    print ('-'*32) #membuat garis

    #menampilkan 
    for nim in sorted(data_dict):
        nama= data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print (f"{nim:<10} | {nama: <12} | {int(nilai):>5}")

#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 3: Membuat Mencari Data
#=========================================

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkna nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("masukkan nim mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict [nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM: {nim_cari}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

#memanggil fungsi cari data
#cari_data(buka_data)
    
#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 4: Membuat Update Data
#=========================================

#membuat fungsi update data
def ubah_data(data_dict):

    #awali dulu dengan mencari nim/ data mahasiswa yang ingin di update
    nim = input ("Masukkan NIM mahasiswa yang diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update Dibatalkan")
    
    if nilai_baru < 0 or nilai_baru >100:
        print("Nilai harus antara 0 sampai 100. Update Dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi udah data
#ubah_data(buka_data)

#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5: Membuat Fungsi Menyimpan Data pada File
#=========================================

#membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}")

#memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)
#print("\nData Berhasil Disimpan ke file:", nama_file)

#=========================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5: Membuat Menu Interaktif
#=========================================

def main():  #fungsi yang dijalankan pertama kali
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) 

    while True:
        print("\n==== MENU MAHASISWA ====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("5. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            ubah_data(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file, buka_data)
            print("Data Berhasil Disimpan")
        elif pilihan == "5":
            print ("Program Selesai")
            break
        else:
            print("Pilihan Tidak Valid. Silahkan coba lagi")

if __name__ == "__main__":
    main() # Main 

