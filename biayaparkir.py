from paketku import*
awalnama = nama_awal("BMW")
akhirnama = nama_akhir("BMW")
if awalnama == akhirnama:
 print ("nama kendaraan:",awalnama)
else :
 print("nama kendaraan tidak sesuia")
    

awaljenis = jenis_awal("mobil")
akhirjenis = jenis_akhir("mobil")
if awaljenis == akhirjenis :
 print ("jenis kendaraan:",awaljenis)
else :
 print ("jenis kendaraan tidak sesuai")
    

mulaijam = jam_awal(7)
akhirjam = jam_akhir(12)
biaya = (akhirjam - mulaijam) * 2000
print ("total biaya parkir:",biaya)
    