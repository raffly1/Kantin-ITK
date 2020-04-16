# from Titipan import Titipan
from Data_Kas import DataKas

# titipan
# t = Titipan('K23', 'Budi', 'Pulpen', 'Rp. 2000', 50, '2020-2-5' )

# t.setHarga(20000)
# print(t.getHarga())

# dataKas
d = DataKas()

d.setPemasukan(200000)
d.setPengeluaran(10000)
d.setLabaBersih()
print(d.getLabaBersih())
