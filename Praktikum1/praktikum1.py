#-------------------------------------------------
#praktikum 1 konsep ADT dan file Handling 
#latihan dasar 1 : Membaca seluruh isi file data
#-------------------------------------------------
print("===Membuka file dalam satu string===")
with open("data_mahasiswa.txt", "r", encoding="utf-8")as file:
    isi_file = file.read()
print (isi_file)

print ("tipe data: ", {type(isi_file)})


print("===Membuka file per baris===")
jumlah_baris = 0 #inisialisasi variabel untuk menghitung jumlah baris
with open ("data_mahasiswa.txt", "r", encoding= "utf-8") as file:
    for baris in file: 
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan baris baru
        print (f"baris ke: {jumlah_baris}")
        print (f"isisnya: {baris}")


#-------------------------------------------------
#praktikum 1 konsep ADT dan file Handling 
#latihan dasar 2 : Parshing data
#-------------------------------------------------
#parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data
with open ("data_mahasiswa.txt", "r", encoding= "utf-8") as file:
    for baris in file: 
        baris = baris.strip() #menghilangkan baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi satuan dan simpan ke variabel
        print ("NIM: ", nim, " Nilai :", nilai)
        

#-------------------------------------------------
#praktikum 1 konsep ADT dan file Handling 
#latihan dasar  3: Membaca data dan menyimpannya 
#-------------------------------------------------

data_list = []#inisasi list untuk menampung data 

with open ("data_mahasiswa.txt", "r", encoding ="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #menyimpan data ke list
print ("=== Menampilkan List===")
print (data_list)
print ("contoh record ke 1", data_list[0])
print ("contoh record ke 2", data_list[1])
print ("jumlah record", len(data_list))


#-------------------------------------------------
#praktikum 1 konsep ADT dan file Handling 
#latihan dasar  4: Membaca data dan menyimpannya ke struktur
#-------------------------------------------------
data_dict ={} #inisialisasi 
with open ("data_mahasiswa.txt", "r", encoding= "utf-8") as file:
    for baris in file: 
        baris = baris.strip() #menghilangkan baris baru
        nim, nama, nilai = baris.split(",") #pecah menjadi satuan dan simpan ke variabel
        #simpan data dalam dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print ("=== Menampilkan Data Dictionary ===")
print (data_dict)


