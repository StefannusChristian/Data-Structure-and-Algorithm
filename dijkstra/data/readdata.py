
class Node():
    def __init__(self):
        self.name = None
        self.index = None
        self.adj = []


def readcsv(filename):  # CSV , fungsi baca file CSV khusus untuk daftar kota dan daftar jalan
    # buka file
    file = open(filename, "r")

    # ambil data
    list_row = file.readlines()

    # tutup file
    file.close()

    result = []
    if len(list_row) == 1:  # Jika hanya ada satu baris, artinya file csvnya daftar kota, buat dibuat list 1 dimensi
        return list_row[0].replace('\n', '').split(',')
    # Jika ada banyak baris, artinya file csvnya daftar jalan, buat jadi list 2 dimensi (list dalam list)
    for row in list_row:
        list_row = row.replace('\n', '')
        result.append(list_row.split(','))

    return result


def to_graf(daftarjalan):  # GraphSturcture #GraphParsing #membangun graf yang disimpan dalam kamus ketetanggaan berdasarkan daftar jalan
    graf = {}  # dictionary untuk simpan graf
    for city1, city2, duration in daftarjalan:  # key: nama kota, value: list yang isinya tetangga dan durasinya
        # karena duration masih dalam string perlu diubah jadi integer
        duration = int(float((duration)))
        if city1 not in graf.keys():
            # jika kota belum ada dalam dictionary, tambahkan kotanya sebagai key, dan list kota tetanggna dan durationnya jadi value
            graf[city1] = [[city2, duration]]
        else:
            # jika kota kota sudah ada dalam dictionary, append list kota tetangga dan durasinya kedalam list dictionary
            graf[city1].append([city2, duration])

        if city2 not in graf.keys():  # lakukan hal yang sama seperti untuk city1
            graf[city2] = [[city1, duration]]
        else:
            graf[city2].append([city1, duration])
    return graf  # Complexity:4E
    # Penjelasan: kompleksitas memori dari kamus ketetanggaan sama dengan list ketetanggaan. kompleksitas memori dari graf yang memakai daftar ketetanggaan adalah 2E, tetapi dalam kasus ini graf yang diberikan adalah graf berbobot sehingga kompleksitasnya menjadi 2*2*E. Hal ini dikarenakan daftar ketetanggan juga menyimpan bobot sisi.
    # GraphMemory = O(E)  (koefisien 4 hilang karena memakai notasi asimtotik)


def makeDict(daftar_kota):  # membuat dictionary untuk konvert kota menjadi index dan sebaliknya
    kamus1 = {}  # keynya nama kota, valuenya index
    kamus2 = {}  # keynya index, valunya nama kota
    i = 0
    for city in daftar_kota:
        kamus1[city] = i
        kamus2[i] = city
        i += 1
    return (kamus1, kamus2)
