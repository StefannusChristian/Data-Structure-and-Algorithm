def dijkstra(graf,kota_awal,daftarkota,kamus1,kamus2): #ShortestPath  #algoritma djikstra, diasumsikan graf adalah graf terhubung, hasilnya adalah djikstra list
  if len(graf) < 2: #harus ada setidaknya 2 node yang terhubung agar algoritma ini bisa berhasil
    return [None]
  start = kota_awal #menyimpan kota awal kedalam variabel start, karena kota_awal akan berubah
  inf = 99999 #karena tidak bisa pakai np.inf pakai angka 99999, dengan mengasumsikan lintasan terpanjang tidak akan lebih dari 99999
  dijkstra_list = [inf]*len(daftarkota) #membuat list yang elemennya akan berisi durasi terpendek dan rutenya dari kota awal ke kota lain berdasarkan indeks, awalnya ditaruh infinity dulu 
  adj = graf[kota_awal] #mengambil tetangga dari kota awal
  durasi_sebelum = 0 #inisiasi dulu durasi sebelum 0, disetiap pengulangan akan bertambah
  path_sebelum = [kota_awal] #akan berisi rute dari kota awal hingga kota akhir, disetiap pengulangan akan bertambah
  cheked = [kota_awal] #akan berisi kota-kota yang sudah pernah dikunjungi, supaya tidak perlu dikunjungi lagi

  while len(cheked) < len(daftarkota): #pengulangan akan berlangsung sampai semua kota dalam daftar kota sudah di kunjungi
    for tetangga,durasi in adj: #cek tetangga sambil update dijkstra list
      if (dijkstra_list[kamus1[tetangga]] == inf) and tetangga not in cheked: #jika baru nemu lintasan baru, tambahkan ke dijikstra list
        dijkstra_list[kamus1[tetangga]] = [durasi+durasi_sebelum,path_sebelum+[tetangga]] #elemen dijikstra_list yang bukan infinity adalah list berisi durasi dan rute dari kota awal ke kota berdasarkan index
      else:
        if tetangga not in cheked: #kalau sudah pernah ada lintasan tapi nemu lintasan baru, bandingkan durasi lintasan baru dengan lintasan yang pernah ada sebelumnya
          if durasi+durasi_sebelum < dijkstra_list[kamus1[tetangga]][0]: #kalo nemu jarak baru yang lebih pendek update dijikstra list
            dijkstra_list[kamus1[tetangga]] = [durasi+durasi_sebelum,path_sebelum+[tetangga]]
    
    min_local = [inf] #inisiasi min_local, min_lokal dibutuhkan untuk menentukan kota yang akan dikunjungi selanjutnya, min_lokal akan menjadi kota awal di pengulangan berikut
    for i in range(len(dijkstra_list)): #cari min_local, minlocal diambil dari elemen dijikstra list yang bukan infinity, dan durasinya paling kecil diantara kota sudah dikunjungi dan sudah punya lintasan
      if dijkstra_list[i] != inf: 
        if kamus2[i] not in cheked:
          if dijkstra_list[i][0] < min_local[0]:
            min_local = [dijkstra_list[i][0],kamus2[i]]

    # update kota awal, path sebelum, durasi sebelum dan cheked
    kota_awal = min_local[1] #kota awal merupakan hasil dari perhitungan min_local
    path_sebelum = dijkstra_list[kamus1[kota_awal]][1] #memperbaharui path sebelum dengan path dari kota awal yang baru
    durasi_sebelum = min_local[0] #memperbaharui durasi sebelum dengan durasi dari kota awal yang baru
    cheked.append(min_local[1]) #menandai kota awal yang baru sebagai kota yang sudah dikunjungi
    adj = graf[kota_awal] #mengambil tetangga dari kota awal untuk diproses di pengulangan selanjutnya

  dijkstra_list[kamus1[start]] = [0,[start,start]] #membuat jarak kota awal ke dirinya sendiri menjadi 0 yang tadinya inf
  return dijkstra_list

#referensi algoritma dijikstra: https://www.youtube.com/watch?v=gPJWbqDEMpM&t=

def calculate_keterpencilan(graf,DK,kamus1,kamus2): #Keterpencilan
  list_keterpencilan=[] #list keterpencilan akan berisi list yang berisi eksentrisitas dan nama kota
  for city in DK: #mengiterasi setiap kota dalam daftar kota
    list_jarak_kota= dijkstra(graf,city,DK,kamus1,kamus2) #mengambil dijiktra list dari suatu kota
    jarakmax=max([sublist[0] for sublist in list_jarak_kota]) #mencari nilai eksentrisitas dari kolom durasi tetpendek
    list_keterpencilan.append([jarakmax,city]) #menambahkan nilai eksentrisitas dan nama kedalam list keterpencilan 
  sorted_list=sorted(list_keterpencilan) #lakukan pengurutan data berdasarkan keterpencilan/eksentrisitas terkecil, fungsi sorted python delalu mengurutkan setiap elemen pertama (nilai eksentrisitas), jika elemen pertamanya sama lalu dibandingkan elemen keduanya
  return sorted_list

def shortest_path(graf,kota_awal,DK,kamus1,kamus2): #Fungsi untuk mencari jarak terpendek dari kota_awal ke semua kota dalam graf
  list_tujuan = dijkstra(graf,kota_awal,DK,kamus1,kamus2) #mengambil dijikstra list dari kota_awal
  if list_tujuan == [None]: #kalau dijikstra list nya [None] artinya graf tersebut memiliki kurang dari 2 kota
    return None
  # membuat list kota tujuan
  kota_tujuan = []
  # mengisi list kota tujuan dengan kota tujuan
  for jarak,tujuan in list_tujuan:
    kota_tujuan.append([jarak,tujuan[-1]])
  # mengurutkan list kota tujuan berdasarkan jarak dari yang paling kecil ke yang paling besar
  sorted_list = sorted(kota_tujuan)
  return sorted_list