# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Hakashi Yumiko Masfat
# NIM     : J0403251023
# Kelas   : TPLA
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}  # dictionary untuk menyimpan data buku
    try:
        with open(nama_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')  # memisahkan berdasarkan koma
                if len(parts) == 3:  # memastikan ada 3 bagian
                    kode_buku, judul, harga = parts
                    database_buku[kode_buku] = {'judul': judul, 'harga': int(harga)}  # menyimpan ke dictionary
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
    return database_buku

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node:
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
         self.head = None  # menginisialisasi head linked list

    def tambah_buku_promosi(self, judul):
        """Menambahkan buku ke daftar promosi (Linked List)"""
        new_node = Node(judul)  # buat node baru
        if self.head is None:
            self.head = new_node  # kalau list kosong, set sebagai head
        else:
            current = self.head
            while current.next:  # mencari node terakhir
                current = current.next
            current.next = new_node  # menambahkan di akhir

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        current = self.head
        if current is None:
            print("Tidak ada buku promosi.")
            return
        print("Daftar Buku Promosi:")
        while current:  # mentraverse linked list
            print(f"- {current.judul}")
            current = current.next

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = []  # list untuk menyimpan antrean pelanggan

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        self.antrean.append(nama_pelanggan)  # menambahkan ke akhir list
        print(f"{nama_pelanggan} ditambahkan ke antrean.")

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        if self.antrean:  # kalau antrean tidak kosong
            pelanggan = self.antrean.pop(0)  # menghapus dari depan
            print(f"{pelanggan} dilayani.")
            return pelanggan
        else:
            print("Antrean kosong.")
            return None

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    # menggunakan insertion sort
    for i in range(1, len(list_harga)):
        key = list_harga[i]  # elemen yang akan disisipkan
        j = i - 1
        # menggeser elemen yang lebih besar dari key ke kanan
        while j >= 0 and key < list_harga[j]:
            list_harga[j + 1] = list_harga[j]
            j -= 1
        list_harga[j + 1] = key  # meyisipkan key di posisi yang benar
    return list_harga

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    """
    Fungsi utama program yang menjalankan menu antarmuka untuk sistem manajemen toko buku.
    Menginisialisasi data dan menjalankan loop menu hingga pengguna memilih keluar.
    """
    # menginisialisasi data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            # menampilkan katalog buku dari dictionary
            print("\nKatalog Buku:", data_buku)
        
        elif pilihan == '2':
            # mengelola daftar promosi menggunakan linked list
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            # Mengelola antrean kasir menggunakan queue
            print("1. Tambah Antrean")
            print("2. Layani Pelanggan")
            sub_pilihan = input("Pilih sub-menu (1-2): ")
            if sub_pilihan == '1':
                nama = input("Nama Pelanggan: ")
                antrean_toko.tambah_antrean(nama)
            elif sub_pilihan == '2':
                antrean_toko.layani_pelanggan()
            else:
                print("Pilihan tidak valid!")

        elif pilihan == '4':
            # menampilkan laporan penjualan terurut menggunakan sorting
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil_sort)

        elif pilihan == '5':
            # keluar dari program
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()