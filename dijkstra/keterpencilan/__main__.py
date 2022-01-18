#Kelompok Eksentrisitas
#- James Patrick Oentoro/10101200241
#- Noel Christevent Mandak/10101200436
#- Stefannus Christian/10101200138
from data.readdata import *
from keterpencilan.graphicuserinterface import *
from keterpencilan.dijkstra import *
if __name__ == '__main__':
   daftar_jalan =  readcsv('data\daftarjalan.csv')
   daftar_kota =  readcsv('data\daftarkota.csv')

   graf = to_graf(daftar_jalan)
   kamus1,kamus2 = makeDict(daftar_kota)
   
   gui(graf,daftar_jalan,daftar_kota,kamus1,kamus2)

#“Di hadapan TUHAN yang hidup, saya menegaskan bahwa saya tidak memberikan maupun
#menerima bantuan apapun—baik lisan, tulisan, maupun elektronik—di dalam ujian ini selain
#daripada apa yang telah diizinkan oleh pengajar, dan tidak akan menyebarkan baik soal
#maupun jawaban ujian kepada pihak lain.”
