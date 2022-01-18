How to Run The Program:
python -m avl_list
================================================================================
                    Analisa Waktu search list dan search AVL Tree
================================================================================
Time Complexity untuk search AVL Tree adalah 
O(log n) untuk search sedangkan untuk linear
search pada list time complexity nya adalah O(n)
sehingga search AVL Tree jauh lebih effisien dari
search list. Maka dari itu, aplikasi AVL tree adalah
didalam indexing large records yang terdapat pada databases
selain itu AVL tree juga digunakan dalam large databases.
Misalnya pada avl_tree [5,4,1,7,9] (lihat baris selanjutnya)
Untuk mencari node 1 pada AVL tree, cara yang dilakukan adalah
traverse elements (pada urutan yang berurutan --> 5-4-1). Cara
Algoritma search AVL tree bekerja adalah melewati satu path saja
dari root sampai leaf,sehingga kompleksitas search AVL tree adalah O(log(n)).
Time complexity dari search pada python asumsi saya adalah
O(n) karena saya berasumsi bahwa yang dilakukan python
adalah linear search atau dengan kata lain, python mencari
node yang hendak kita cari satu per satu per index. 
================================================================================
                            Perbandingan Waktu yang dibutuhkan
================================================================================
Angka yang dicari = 1
AVLTree    = 0.0009968234542345 detik
Python     = 0.00516346235835 detik
Output     = True (data ditemukan)

Angka yang dicari = 18253 :
AVLTree    = 0.0 detik
Python     = 0.0009393682359353681 detik
Output     = True (data ditemukan)

Waktu pencarian angka 37383 :
AVLTree    = 0.00199823572357394275 detik
Python     = 0.0048246283752943 detik
Output     = True (data ditemukan)

Waktu pencarian angka 53564 :
AVLTree    = 0.0 detik
Python     = 0.0 detik
Output     = True (data ditemukan)

Waktu pencarian angka 75000 :
AVLTree    = 0.0 detik
Python = 0.001003982385728 detik
Output     = True (data ditemukan)

Waktu pencarian angka -113: 
AVLTree    = 0.0 detik
Python 	   = 0.00410223492893475 detik
Output     = False (data tidak ditemukan karena yang dimasukkan hanya 0 - 750k)

Waktu pencarian angka 75001:
AVLTree    = 0.0 detik
ListPython = 0.0030467308457348957 detik
Output     = False (data tidak ditemukan karena yang dimasukkan hanya 0 - 750k)

# REMARK: Pak maaf, karena saya baru sempat selesaikan tugas ini mepet deadline,
jadi saya tidak sempat meng-insert 750k data ke dalam tree (lama banget), sehingga
saya hanya memasukkan 75000 data saja. Terima Kasih.
================================================================================
                            AVL TREE STRUKTUR DATA DAN ALGORITMA
================================================================================