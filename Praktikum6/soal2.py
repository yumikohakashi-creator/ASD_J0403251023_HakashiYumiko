###################################
# Nama: Hakashi Yumiko Masfat
# NIM : J0403251023
# Kelas : TPL A2
###################################

data = [1,3,5,7,9,0,2,4,6,8]
print("data: ", data)
print("-"*30)
try:
    print("hasil data.index(3,0,3): ", data.index(3,0,3))
except ValueError:
    print("hasil data.index(3,0,3): error, tidak ditemukan")

try:
    print("hasil data.index(3,5,6): ", data.index(3,5,6))
except ValueError:
    print("hasil data.index(3,5,6): error, tidak ditemukan")

try:
    print("hasil data.index(3,3,0): ", data.index(3,3,0))
except ValueError:
    print("hasil data.index(3,3,0): error, tidak ditemukan")

try:
    print("hasil data.index(3,0,11): ", data.index(3,0,11))
except ValueError:
    print("hasil data.index(3,0,11): error, tidak ditemukan")
