class Animal:
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        self.nama = nama
        self.sifat = sifat
        self.ukuran = ukuran
        self.jumlah_kaki = jumlah_kaki

    def tampil_info(self):
        print('Nama :', self.nama, '| Sifat :', self.sifat, '| Ukuran :', self.ukuran, '| Jumlah Kaki :', self.jumlah_kaki)

class Mamalia(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

    def tampil_info(self):
        super().tampil_info()
        print('Bisa Jalan :', self.bisa_jalan, '| Jenis Mamalia :', self.jenis_mamalia)

class Aves(Animal):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

    def tampil_info(self):
        super().tampil_info()
        print('Bisa Terbang :', self.bisa_terbang, '| Jenis Aves :', self.jenis_aves)

class Ayam(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def tampil_info(self):
        super().tampil_info()
        print('Jenis Ayam :', self.jenis_ayam, '| Keahlian Khusus :', self.bisa_diadu)

class Merpati(Aves):
    def __init__(self, nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves, jenis_merpati, bisa_diadu):
        super().__init__(nama, sifat, ukuran, jumlah_kaki, bisa_terbang, jenis_aves)
        self.jenis_merpati = jenis_merpati
        self.bisa_diadu = bisa_diadu

    def tampil_info(self):
        super().tampil_info()
        print('Jenis Merpati :', self.jenis_merpati, '| Keahlian Khusus :', self.bisa_diadu)

# Objek
singa = Mamalia('Singa', 'Buas', 'Besar', 4, 'Bisa', 'Liar')
kuda = Mamalia('Kuda', 'Jinak', 'Besar', 4, 'Bisa', 'Ternak')
gajah = Mamalia('Gajah', 'Jinak', 'Besar', 4, 'Bisa', 'Liar')

burung_merpati = Aves(' Burung Merpati', 'Jinak', 'Kecil', 2, 'Bisa', 'Peliharaan')
burung_camar = Aves('Burung Camar', 'Jinak', 'Kecil', 2, 'Bisa', 'Liar')

ayam_sailan = Ayam('Ayam Sailan', 'Jinak', 'Kecil', 2, 'Bisa', 'Liar', 'Ayam Hutan', 'Bisa Diadu')
merpati_wulung = Merpati('Merpati Wulung', 'Jinak/Liar', 'Kecil', 2, 'Bisa', 'Merpati', 'Wulung', 'Tidak ada')

singa.tampil_info()
print('\n')
kuda.tampil_info()
print('\n')
gajah.tampil_info()
print('\n')
burung_merpati.tampil_info()
print('\n')
burung_camar.tampil_info()
print('\n')
ayam_sailan.tampil_info()
print('\n')
merpati_wulung.tampil_info()
print('\n')
