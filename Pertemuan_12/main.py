class SeniRupa:
    def __init__(self, nama, teknik):
        self._nama = nama
        self.__teknik = teknik

    def akses(self, teknik):
        self.__teknik = teknik

    def akses_teknik(self):
        print('Teknik :', self.__teknik)

    def display_info(self):
        print('Karya Seni :', self._nama, '| Teknik :', self.__teknik)

class DuaDimensi(SeniRupa):
    def __init__(self, nama, teknik, pembuat, panjang, lebar, media):
        super().__init__(nama, teknik)
        self.pembuat = pembuat
        self.panjang = panjang
        self.lebar = lebar
        self.media = media
        self.hitung_luas()

    def hitung_luas(self):
        self.luas = self.panjang * self.lebar
    
    def display_info(self):
        super().display_info()
        print('| Pembuat :', self.pembuat, '| Media :', self.media, '| Ukuran :', self.luas , 'cm^2')
    
class TigaDimensi(SeniRupa):
    def __init__(self, nama, teknik, ukuran, bahan):
        super().__init__(nama, teknik)
        self.ukuran = ukuran
        self.bahan = bahan

    def display_info(self):
        super().display_info()
        print('| Ukuran :', self.ukuran, '| Bahan :', self.bahan)

class Terapan(TigaDimensi):
    def __init__(self, nama, teknik, ukuran, bahan, fungsi):
        super().__init__(nama, teknik, ukuran, bahan)
        self.__fungsi = fungsi

    def akses(self, fungsi):
        self.__fungsi = fungsi

    def akses_fungsi(self):
        print('Fungsi :', self.__fungsi)

    def display_info(self):
        super().display_info()
        print('| Fungsi :', self.__fungsi )

# Pembuatan Objek
karya_2D_1 = DuaDimensi('Lukisan Borobudur', 'Ekspresionisme', 'Affandi', 90, 120, 'Cat Minyak')
karya_2D_2 = DuaDimensi('Lukisan Kuda-Kuda Laut', 'Romantisme', 'Raden Saleh', 167, 112, 'Cat Minyak')
karya_2D_3 = DuaDimensi('Lukisan Pertempuran Arjuna melawan Karna', 'Realisme', 'Basuki Abdullah', 150, 200, 'Cat Minyak')

karya_3D_1 = TigaDimensi('Patung Dewi Saraswati', 'Patung Ekletik', 'Sedang', 'Batu Paras Jogja')
karya_3D_2 = TigaDimensi('Patung Garuda Wisnu Kencana', 'Patung Realis', 'Besar', 'Baja dan Perunggu')

Terapan_1 = Terapan('Batik Tradisional Jawa', 'Canting dan Malam', 'Beragam', 'Kain Katun atau Sutera', 'Pakaian')

if __name__ == '__main__':
    while True:
        print('=============================')
        print('       KARYA SENI RUPA       ')
        print('=============================')
        print('1. Karya Seni 2 Dimensi')
        print('2. Karya Seni 3 Dimensi')
        print('3. Karya Seni Terapan')
        print('4. Teknik Karya Seni')
        print('5. Exit')

        choice = input('Pilih Jenis Karya Seni : ')

        if choice == '1':
            print('='*80)
            print('KARYA SENI 2 DIMENSI')
            print('--------------------')
            karya_2D_1.display_info()
            print('')
            karya_2D_2.display_info()
            print('')
            karya_2D_3.display_info()
            print('='*80)

        elif choice == '2':
            print('='*80)
            print('KARYA SENI 3 DIMENSI')
            print('--------------------')
            karya_3D_1.display_info()
            print('')
            karya_3D_2.display_info()
            print('='*80)

        elif choice == '3':
            print('='*80)
            print('KARYA SENI TERAPAN')
            print('------------------')
            Terapan_1.display_info()
            print('='*80)

        elif choice == '4':
            print('='*80)
            print('TEKNIK KARYA SENI')
            print('1. Karya Seni 2 Dimensi')
            print('2. Karya Seni 3 Dimensi')
            print('3. Karya Seni Terapan')

            teknik_choice = input('Pilih Teknik karya seni (1-3): ')
            if teknik_choice == '1':
                print('------------------')
                karya_2D_1.akses_teknik()
                karya_2D_2.akses_teknik()
                karya_2D_3.akses_teknik()
                print('='*80)

            elif teknik_choice == '2':
                print('------------------')
                karya_3D_1.akses_teknik()
                karya_3D_2.akses_teknik()
                print('='*80)

            elif teknik_choice == '3':
                print('------------------')
                Terapan_1.akses_teknik()
                Terapan_1.akses_fungsi()
                print('='*80)

            else:
                print('Pilihan karya seni tidak valid.')
                print('='*80)

        elif choice == '5':
            print('Terima kasih! Program selesai.')
            print('='*80)
            break
        else:
            print('Pilihan tidak valid. Silakan pilih 1-5.')
            print('='*80)