##################################
# Nama: Hakashi Yumiko Masfat
# NIM: J0403251023
# Kelas: TPL A2
##################################


def quickSort(data):
    quickSortHelper(data, 0, len(data) - 1)

def quickSortHelper(data, first, last):
    if first < last:
        splitpoint = partition(data, first, last)
        quickSortHelper(data, first, splitpoint - 1)
        quickSortHelper(data, splitpoint + 1, last)

def partition(data, first, last):
    pivotvalue = data[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1
        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            data[leftmark], data[rightmark] = data[rightmark], data[leftmark]

    data[first], data[rightmark] = data[rightmark], data[first]
    return rightmark

skor_pelamar = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
quickSort(skor_pelamar)

print("hasil pengurutan skor (dari tinggi ke rendah):")
print(skor_pelamar)
lima_tertinggi = skor_pelamar[:5]
print("\n5 kandidat teratas:")
print(lima_tertinggi)