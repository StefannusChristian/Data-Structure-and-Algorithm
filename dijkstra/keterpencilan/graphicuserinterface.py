from keterpencilan.dijkstra import * 

#Untuk menampilkan graf
import networkx as nx
import matplotlib.pyplot as plt

def find_longname(daftar_kota): #menghitung panjang nama kota dengan nama terpanjang, diperlukan agar pembuatan tabel bisa rapih
    longname = 0
    for kota in daftar_kota: #mengiterasi nama kota dalam daftar kota
        ln = len(kota)
        if ln > longname: #mencari nama kota dengan panjang terbesar
            longname = ln
    return longname


def data_jarak(daftarjalan,daftarkota): #fungsi untuk menampilkan tabel
    long = find_longname(daftarkota) #mencari len dari nama terpanjang untuk menjadi patokan lebar kolom kota asal dan kota tujuan
    no_len = len(str(len(daftarjalan))) #mencari tahu ada berapa banyak sisi dalam graf lalu dihitung berapa banyak digitnya untuk menjadi patokan lebar kolom nomor
    if no_len < 3: #kalo digitnya kurang dari tiga patokannya pakai len judul kolomnya (len('No.'))
        no_len = 3
    if long < 6: #kalo digitnya kurang dari enam patokannya pakai len judul kolomnya (len('Tujuan'))
        long = 6
    i = 1 
    print('Data Jarak')
    print('No.'.center(no_len),'|','Asal'.center(long),'|','Tujuan'.center(long),'|','Jarak','|') #judul kolom
    for st1,st2,duration in daftarjalan:
        print(str(i).rjust(no_len-1),' |',st1.ljust(long),'|',st2.ljust(long),'|',str(int(float(duration))).center(5),'|') #baris dalam tabel
        i+=1

def Pilihan_1(graf,DK,kamus1,kamus2): #Keterpencilan #menampikan nilai keterpencilan dari setiap kota
  list_keterpencilan=[]
  for city in DK: #mengiterasi setiap kota dalam daftar kota
    list_jarak_kota= dijkstra(graf,city,DK,kamus1,kamus2)  #mengambil dijikstra list dari kota tersebut
    jarakmax=max([sublist[0] for sublist in list_jarak_kota]) #Radcc #mencari kota yang memiliki rute tercepat dan jarak terjauh = mencari nilai eksentrisitas
    list_keterpencilan.append([jarakmax,city]) #simpan kedalam list keterpencilan
  sorted_list=sorted(list_keterpencilan) #urutkan berdasarkan durasi secara ascending, data paling atas adalah jari-jari graf
  long = find_longname(DK) #mencari len dari nama terpanjang untuk menjadi patokan lebar kolom kota asal dan kota tujuan
  no_len = len(str(len(DK))) #mencari tahu ada ada berapa banyak kota lalu dihitung berapa banyak digitnya untuk menjadi patokan lebar kolom nomor
  if no_len < 3: #kalo digitnya kurang dari tiga patokannya pakai len judul kolomnya (len('No.'))
      no_len = 3
  if long < 4:  #kalo digitnya kurang dari enam patokannya pakai len judul kolomnya (len('Kota'))
      long = 4
  i = 1
  print('1. Keterpencilan optimal')
  print('No.'.center(no_len),'|','Kota'.center(long),'|','Keterpencilan','|') #judul kolom
  for data in sorted_list:
    print(str(i).rjust(no_len-1),' |',data[1].ljust(long),'|',str(data[0]).center(13),'|')
    i+=1

def Pilihan_2(graf,DK,kamus1,kamus2): #ShortestPath
  kota_awal = input('\nMasukkan kota awal: ')
  if kota_awal not in DK:
    print("Nama kota tidak ditemukan, silahkan masukkan lagi")
    return
  print(f'\n2. Keterpencilan {kota_awal}')
  list_tujuan = dijkstra(graf,kota_awal,DK,kamus1,kamus2) #mangambil dijikstra list dari kota_awal
  # membuat list kota tujuan
  kota_tujuan = []
  # mengisi list kota tujuan dengan kota tujuan
  for jarak,tujuan in list_tujuan:
    kota_tujuan.append([jarak,tujuan[-1]])
  # mengurutkan list kota tujuan berdasarkan jarak dari yang paling kecil ke yang paling besar
  kota_tujuan.sort()
  # membuat tabel
  long = 10
  no_len = 2
  if no_len < 3:
    no_len = 3
  if long < 4:
    long = 4
  i = 1
  print('No.'.center(no_len),'|','Asal'.center(long),'|','Tujuan'.center(long),'|','Jarak','|')
  for kota in kota_tujuan:
    print(str(i).rjust(no_len-1),' |',kota_awal.ljust(long),'|',kota[1].ljust(long),'|',str(kota[0]).center(5),'|')
    i+=1
  jarak_terjauh,kota_terjauh = kota_tujuan[-1]
  # output
  print(f'Skor Keterpencilan kota {kota_awal} adalah {jarak_terjauh}, di mana jarak terjauh dari {kota_awal} adalah saat mengirim ke {kota_terjauh}.')


def show_graf(daftarjalan):  #Bonus :menampilkan graf dengan menggunakna library matplotlib dan networkx
    plt.figure(figsize=(8,8)) #membuat figura
    G = nx.DiGraph() #mengambil objek graf dari library network

    for city1,city2,duration in daftarjalan: #mengiterasi semua sisi dalam daftar jalan
        duration = int(duration)
        G.add_edges_from([(city1,city2)], weight=duration) #menambahkan sisi kedalam objek graf

    edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)]) #menaruh label jarak 
    pos=nx.spring_layout(G) #mengambil titik-titik acak sebanyak banyaknya node dalam graf
    nx.draw(G,pos, node_color = 'tomato', node_size=1000, with_labels=True,arrows=False,font_size=10) #membuat bulatan yang mewakili setiap node dan memiliki keterangan nama kotanya
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=10) #membuat garis pengubung dan menampilkan jarak/durasi antar dua kota
    plt.show() #menampilkan graf

def options(): # fungsi untuk menampilkan opsi yang terdapat pada program dan meminta input user 
  print('Pilih tampilkan: ')
  print('1. Kota dengan nilai keterpencilan optimal')
  print('2. Perhitungan nilai keterpencilan berdasarkan kota asal')
  print('3. Keluar')
  print('4. Tampilkan Graf')
  user_option = input('Pilih: ')
  return user_option

def gui(graf,daftar_jalan,daftar_kota,kamus1,kamus2): #GUI # Main GUI: untuk menampilkan fungsi - fungsi pilihan di atas
    while True:
        data_jarak(daftar_jalan,daftar_kota)
        user_option = options()
        if user_option == '1': 
            Pilihan_1(graf,daftar_kota,kamus1,kamus2)
            input('\nTekan enter untuk melanjutkan \n')
        elif user_option == '2': #
            Pilihan_2(graf,daftar_kota,kamus1,kamus2)
            input('\nTekan enter untuk melanjutkan \n')
        elif user_option == '3':
            print('Terima kasih karena telah menggunakan program ini.')
            print('Anda telah keluar dari program.')
            break
        elif user_option == '4':
            show_graf(daftar_jalan)
        else:
            print('Input anda invalid.')
            input('\nTekan enter untuk melanjutkan \n')


  


