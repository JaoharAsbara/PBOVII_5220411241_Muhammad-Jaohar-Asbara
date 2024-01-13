import mysql.connector

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
        print('| Pembuat :', self.pembuat, '| Media :', self.media, '| Ukuran :', self.luas, 'cm^2')

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
        print('| Fungsi :', self.__fungsi)

class KaryaSeniDB:
    def __init__(self):
        self.connection = self.koneksi_database()

    def koneksi_database(self):
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='5220411241'
        )

    def tambah_karya_seni(self, nama, teknik, jenis, pembuat=None, panjang=None, lebar=None, media=None, ukuran=None, bahan=None, fungsi=None):
        cursor = self.connection.cursor()

        if jenis == '2D':
            cursor.execute('INSERT INTO karya_seni_2d (nama, teknik, pembuat, panjang, lebar, media) VALUES (%s, %s, %s, %s, %s, %s)', (nama, teknik, pembuat, panjang, lebar, media))

        elif jenis == '3D':
            cursor.execute('INSERT INTO karya_seni_3d (nama, teknik, ukuran, bahan) VALUES (%s, %s, %s, %s)', (nama, teknik, ukuran, bahan))

        elif jenis == 'terapan':
            cursor.execute('INSERT INTO karya_seni_terapan (nama, teknik, ukuran, bahan, fungsi) VALUES (%s, %s, %s, %s, %s)',(nama, teknik, ukuran, bahan, fungsi))

        else:
            print('Maaf jenis karya seni tidak tersedia.')

        self.connection.commit()
        cursor.close()

    def tampil_karya_seni(self, jenis):
        cursor = self.connection.cursor()

        if jenis == '2D':
            cursor.execute('SELECT * FROM karya_seni_2d')

        elif jenis == '3D':
            cursor.execute('SELECT * FROM karya_seni_3d')

        else:
            cursor.execute('SELECT * FROM karya_seni_terapan')

        result = cursor.fetchall()

        for row in result:
            print(row)

        cursor.close()

    def update_karya_seni(self, id_karya, teknik_baru):
        cursor = self.connection.cursor()

        cursor.execute('UPDATE karya_seni_2d SET teknik = %s WHERE id = %s', (teknik_baru, id_karya))
        cursor.execute('UPDATE karya_seni_3d SET teknik = %s WHERE id = %s', (teknik_baru, id_karya))
        cursor.execute('UPDATE karya_seni_terapan SET teknik = %s WHERE id = %s', (teknik_baru, id_karya))

        self.connection.commit()
        cursor.close()

    def delete_karya_seni(self, id_karya):
        cursor = self.connection.cursor()

        cursor.execute('DELETE FROM karya_seni_2d WHERE id = %s', (id_karya,))
        cursor.execute('DELETE FROM karya_seni_3d WHERE id = %s', (id_karya,))
        cursor.execute('DELETE FROM karya_seni_terapan WHERE id = %s', (id_karya,))

        self.connection.commit()
        cursor.close()

    def __del__(self):
        self.connection.close()

karya_2D_1 = DuaDimensi('Lukisan Borobudur', 'Ekspresionisme', 'Affandi', 90, 120, 'Cat Minyak')
karya_2D_2 = DuaDimensi('Lukisan Kuda-Kuda Laut', 'Romantisme', 'Raden Saleh', 167, 112, 'Cat Minyak')
karya_2D_3 = DuaDimensi('Lukisan Pertempuran Arjuna melawan Karna', 'Realisme', 'Basuki Abdullah', 150, 200, 'Cat Minyak')

karya_3D_1 = TigaDimensi('Patung Dewi Saraswati', 'Patung Ekletik', 'Sedang', 'Batu Paras Jogja')
karya_3D_2 = TigaDimensi('Patung Garuda Wisnu Kencana', 'Patung Realis', 'Besar', 'Baja dan Perunggu')

Terapan_1 = Terapan('Batik Tradisional Jawa', 'Canting dan Malam', 'Beragam', 'Kain Katun atau Sutera', 'Pakaian')

if __name__ == '__main__':
    karya_seni_db = KaryaSeniDB()

    while True:
        print('=============================')
        print('       KARYA SENI RUPA       ')
        print('=============================')
        print('1. Karya Seni 2 Dimensi')
        print('2. Karya Seni 3 Dimensi')
        print('3. Karya Seni Terapan')
        print('4. Update Teknik Karya Seni')
        print('5. Tambah Karya Seni')
        print('6. Hapus Karya Seni')
        print('7. Exit')

        choice = input('Pilih Menu yang Tersedia : ')

        if choice == '1':
            print('=' * 80)
            print('KARYA SENI 2 DIMENSI')
            print('--------------------')
            karya_2D_1.display_info()
            print('')
            karya_2D_2.display_info()
            print('')
            karya_2D_3.display_info()
            print('')
            print('Tambahan Karya Seni 2D:')
            karya_seni_db.tampil_karya_seni('2D')
            print('=' * 80)

        elif choice == '2':
            print('=' * 80)
            print('KARYA SENI 3 DIMENSI')
            print('--------------------')
            karya_3D_1.display_info()
            print('')
            karya_3D_2.display_info()
            print('')
            print('Tambahan Karya Seni 3D:')
            karya_seni_db.tampil_karya_seni('3D')
            print('=' * 80)

        elif choice == '3':
            print('=' * 80)
            print('KARYA SENI TERAPAN')
            print('------------------')
            Terapan_1.display_info()
            print('')
            print('Tambahan Karya Seni 3D Terapan:')
            karya_seni_db.tampil_karya_seni('terapan')
            print('=' * 80)

        elif choice == '4':
            print('=' * 80)
            print('TEKNIK KARYA SENI')
            print('1. Karya Seni 2 Dimensi')
            print('2. Karya Seni 3 Dimensi')
            print('3. Karya Seni Terapan')

            teknik_choice = input('Pilih Teknik karya seni (1-3): ')
            if teknik_choice == '1':
                print('------------------')
                id_karya = input('Masukkan ID karya seni 2D yang akan diperbarui: ')
                teknik_baru = input('Masukkan teknik baru: ')
                karya_seni_db.update_karya_seni(id_karya, teknik_baru)
                print('=' * 80)

            elif teknik_choice == '2':
                print('------------------')
                id_karya = input('Masukkan ID karya seni 3D yang akan diperbarui: ')
                teknik_baru = input('Masukkan teknik baru: ')
                karya_seni_db.update_karya_seni(id_karya, teknik_baru)
                print('=' * 80)

            elif teknik_choice == '3':
                print('------------------')
                id_karya = input('Masukkan ID karya seni terapan yang akan diperbarui: ')
                teknik_baru = input('Masukkan teknik baru: ')
                karya_seni_db.update_karya_seni(id_karya, teknik_baru)
                print('=' * 80)
            else:
                print('Pilihan karya seni tidak valid.')
                print('=' * 80)

        elif choice == '5':
            print('=' * 80)
            print('KARYA SENI TAMBAHAN')
            print('-------------------')

            nama = input('Masukkan nama karya seni: ')
            teknik = input('Masukkan teknik karya seni: ')
            jenis = input('Masukkan jenis karya seni (2D/3D/terapan): ')

            if jenis in ['2D', '3D', 'terapan']:
                if jenis == '2D':
                    pembuat = input('Masukkan nama pembuat: ')
                    panjang = input('Masukkan panjang (cm): ')
                    lebar = input('Masukkan lebar (cm): ')
                    media = input('Masukkan media: ')
                    karya_seni_db.tambah_karya_seni(nama, teknik, jenis, pembuat=pembuat, panjang=panjang, lebar=lebar, media=media)

                elif jenis == '3D':
                    ukuran = input('Masukkan ukuran: ')
                    bahan = input('Masukkan bahan: ')
                    karya_seni_db.tambah_karya_seni(nama, teknik, jenis, ukuran=ukuran, bahan=bahan)

                elif jenis == 'terapan':
                    ukuran = input('Masukkan ukuran: ')
                    bahan = input('Masukkan bahan: ')
                    fungsi = input('Masukkan fungsi: ')
                    karya_seni_db.tambah_karya_seni(nama, teknik, jenis, ukuran=ukuran, bahan=bahan, fungsi=fungsi)

                print('Karya seni berhasil ditambahkan!')
            else:
                print('Jenis karya seni tidak valid.')

            print('=' * 80)

        elif choice == '6':
            print('=' * 80)
            print('HAPUS KARYA SENI')
            print('1. Hapus Karya Seni 2 Dimensi')
            print('2. Hapus Karya Seni 3 Dimensi')
            print('3. Hapus Karya Seni Terapan')

            pil_delete = input('Pilih jenis karya seni yang akan dihapus (1-3): ')

            if pil_delete in ['1', '2', '3']:
                id_karya = input('Masukkan ID karya seni yang akan dihapus: ')
                karya_seni_db.delete_karya_seni(id_karya)
                print('Karya seni berhasil dihapus!')
            else:
                print('Pilihan karya seni tidak valid.')

            print('=' * 80)

        elif choice == '7':
            print('Terima kasih! Program selesai.')
            print('=' * 80)
            break

        else:
            print('Pilihan tidak valid. Silakan pilih 1-6.')
            print('=' * 80)
