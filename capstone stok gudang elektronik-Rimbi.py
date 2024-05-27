from datetime import datetime, date

#Kelas Elektronik untuk mendefinisikan atribut produk elektronik
class Elektronik:
    def __init__(self, kode, nama, jenis, stok, harga, tanggal_masuk, garansi_tahun):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.stok = stok
        self.harga = harga
        self.tanggal_masuk = tanggal_masuk
        self.garansi_tahun = garansi_tahun  

#Inisialisasi data elektronik dengan beberapa produk
dataelektronik = [
    Elektronik('E101', 'Laptop Asus ROG Zephyrus G14', 'Laptop', 15, 25000000, '1-11-2024', '2 Tahun'),
    Elektronik('E102', 'Smartphone Samsung Galaxy S23 Ultra', 'Smartphone', 25, 18000000, '1-11-2024', '1 Tahun'),
    Elektronik('E103', 'Headphone Sony WH-1000XM5', 'Headphone', 30, 5500000, '1-11-2024', '1 Tahun'),
    Elektronik('E104', 'Smartwatch Apple Watch Series 8', 'Smartwatch', 20, 7000000, '1-11-2024', '1 Tahun'),
    Elektronik('E105', 'Kamera Mirrorless Canon EOS R6', 'Kamera', 10, 32000000, '1-11-2024', '1 Tahun')
]

# Fungsi template tabel daftar Elektronik
def ShowList(data_elektronik):
    header = ["Kode", "Nama", "Jenis", "Stok", "Harga", "Tanggal_Masuk", "Garansi_Tahun"]

    # Menentukan lebar minimum untuk kolom harga, tanggal, dan garansi
    lebar_kolom_min = {
        "Harga": 15,  # Minimal 15 karakter untuk harga
        "Tanggal_Masuk": 15,  # Minimal 15 karakter untuk tanggal
        "Garansi": 10  # Minimal 10 karakter untuk garansi
    }

    # Menghitung lebar maksimum untuk setiap kolom, dengan mempertimbangkan lebar minimum
    lebar_kolom = [max(
        lebar_kolom_min.get(kolom, 0),  
        max(len(str(getattr(item, kolom.lower()))) for item in data_elektronik)
    ) for kolom in header]

    # Menampilkan header tabel
    for i, kolom in enumerate(header):
        print(f"{kolom:<{lebar_kolom[i]}}  ", end="")
    print()

    # Menampilkan pemisah
    for lebar in lebar_kolom:
        print("=" * lebar, end="  ") 
    print()

# Menampilkan isi tabel
    for item in data_elektronik:
        for kolom in header:
            nilai = getattr(item, kolom.lower())
            if kolom == "Harga":
                nilai = f"Rp{nilai:,}"
            elif kolom == "Tanggal_Masuk":
                if isinstance(nilai, date):  
                    nilai = nilai.strftime("%d-%m-%Y") 
                else:
                    nilai = datetime.strptime(nilai, "%d-%m-%Y").date().strftime("%d-%m-%Y") 
            print(f"{nilai:<{lebar_kolom[header.index(kolom)]}}  ", end="")
        print()

# Fungsi update barang sesuai kolom
def UpdateBarang(Data, Kolom, NewData2):
    InputUpdateBarang = (input("\tApakah data yang diupdate sudah benar? (Ya/Tidak): ")).lower()
    if InputUpdateBarang == "ya":
        Data[0][Kolom] = NewData2
        print("\n\tData sudah diperbarui!, Silahkan cek data terupdate pada menu 2")
    else:
        print("\t Data tidak terupdate!")

# Fungsi filter dictionary dalam list (Modifikasi dengan Lambda)
# Fungsi untuk mencari produk elektronik berdasarkan kode
def SearchList(Input):
    return list(filter(lambda data: data.kode == str(Input), dataelektronik))

def tampilkan_data_elektronik():
    if not dataelektronik:  
        print("\tTidak ada data elektronik.")
        return  

    ShowList(dataelektronik)

#Tampilan menu awal 
def MenuAwal():
    print('''
    = = = = = = =Selamat Datang Di Toko Elektronik Sova = = = = = = = 

        = = = = = = = = = Daftar Pilihan : = = = = = = = =
            
            1. Report Stok Elektronik
            2. Menambahkan Data Stok Elektronik
            3. Mengupdate Data Stok Elektronik
            4. Menghapus Data
            5. Exit ''')

    while True:

        PilihanMenu = (input('\nMasukkan nomor yang dipilih[1-5]: '))
        if PilihanMenu == '1':
            MenuDataElektronik()
        elif PilihanMenu == '2':
            MenambahData()
        elif PilihanMenu == '3':
            UpdateData()
        elif PilihanMenu == '4':
            DeleteData()
        elif PilihanMenu == '5':
            print('\n=== Terima kasih dan Sampai Jumpa lagi :) === \n')
            exit()
        else:
            print('Anda memasukkan pilihan yang salah \nsilahkan pilih menu yang benar antara [1-5] ')   

# Pilihan untuk menampilkan seluruh Stok Elektronik dalam databases
def MenuDataElektronik():
    while True:
        print('''
        ==== Menu Menampilkan Stok Elektronik ====
        
        1. Menampilkan semua Stok Elektronik
        2. Menampilkan data tertentu
        3. Kembali ke menu utama\n ''')
        
        SubMenu = input('Silahkan pilih daftar diatas [1-3]: ')

        if SubMenu == '1' and dataelektronik:
            ShowList(dataelektronik)
        elif SubMenu == '2' and dataelektronik:
            CodeStok = input("\tMasukkan Kode Elektronik yang ingin anda cari: ")
            hasil_pencarian = SearchList(CodeStok)
            if hasil_pencarian:
                ShowList(hasil_pencarian)
            else:
                print("\n\t Data Tidak Ditemukan")
        elif SubMenu == '3':
            MenuAwal()
        else:
            print('\nSilahkan masukkan pilihan yang sesuai [1-3]:')

# Fungsi untuk menambah produk elektronik baru
def tambah_produk():
    while True:
        tampilkan_data_elektronik()

        while True:
            kode_elektronik = input('\nMasukkan Kode Elektronik baru (minimal 4 karakter, kombinasi huruf dan angka): ')
            if len(kode_elektronik) >= 4 and kode_elektronik.isalnum():  
                if any(elektronik.kode == kode_elektronik for elektronik in dataelektronik):
                    print('Kode sudah ada di database, silahkan masukkan kode baru.')
                else:
                    break
            else:
                print('Kode tidak valid. Minimal 4 karakter, kombinasi huruf dan angka.')

        nama = input('Nama Elektronik: ').capitalize()
        jenis = input('Jenis Elektronik: ').capitalize()

        while True:
            try:
                stok = int(input('Stok Elektronik: '))
                if stok < 0:
                    raise ValueError("Stok harus berupa bilangan positif.")
                break
            except ValueError as e:
                print('Stok harus angka.')

        while True:
            try:
                harga = int(input('Harga: '))
                if harga < 0:
                    raise ValueError("Harga harus berupa bilangan positif.")
                break
            except ValueError as e:
                print('harga harus angka.')

        while True:
            tanggal_str = input('Tanggal Masuk (format DD-MM-YYYY): ')
            try:
                tanggal_masuk = datetime.strptime(tanggal_str, "%d-%m-%Y").date()  
                break
            except ValueError:
                print('Format tanggal tidak valid. Gunakan DD-MM-YYYY.')

        while True:
            try:
                durasi_garansi = int(input('Durasi Garansi (dalam tahun): '))
                if durasi_garansi <= 0:
                    raise ValueError("Durasi garansi harus berupa bilangan positif.")
                garansi_tahun = f"{durasi_garansi} Tahun" 
                break
            except ValueError as e:
               print('garansi harus berupa bilangan positif ')

        konfirmasi = input('''Apakah anda yakin data ini akan ditambahkan (Y/T)? : ''').capitalize()
        if konfirmasi == 'Y':
            dataelektronik.append(Elektronik(kode_elektronik, nama, jenis, stok, harga, tanggal_masuk, garansi_tahun))
            tampilkan_data_elektronik()
            print('\n Stok Elektronik Berhasil ditambahkan')
            return 

        elif konfirmasi == 'T':
            print('\nData Elektronik Tidak Jadi ditambahkan')
            return  #

        else:
            print('''\nPilihan yang anda masukkan salah, Silahkan Masukkan pilihan range [Y/T]''')

# Pilihan untuk Menambah Stok Elektronik
def MenambahData():
    while True:
        create_data = input('''
        **********Menu Menambah Stok Elektronik***********
        
                1. Menambah Stok Elektronik ke database
                2. Kembali ke menu utama
        Silahkan pilih menu diatas : ''')

        if create_data == '1':
            tambah_produk()
        elif create_data == '2':
            MenuAwal()
            break 
        else:
            print('''\nPilihan yang anda masukkan salah, Silahkan Masukkan pilihan range [1-2]''')


# Menu Untuk Update/Mengubah stok Elektronik
from datetime import datetime

def UpdateData():
    while True:
        Updatedatacust = input('''
        ======= Menu ubah data customer ======
                        
        1. Update Stok Elektronik
        2. Cek data terupdate
        3. Kembali ke main menu

        Silahkan pilih menu diatas ''')

        if Updatedatacust == '1':
            tampilkan_data_elektronik()
            code_elektronik = input('\n===Masukkan Kode Stok Elektronik:')
            produk_ditemukan = SearchList(code_elektronik)
            if produk_ditemukan:
                while True:
                    print('''
                    === Data Elektronik ditemukan === ''')
                    ShowList(produk_ditemukan)
                    konfirmasi = input('''
                    === Apakah data ingin di ubah (Y/T)? : ''').capitalize()
                    if konfirmasi == 'Y':
                        while True:
                            kolom = int(input('''\tKategori Database Stok Elektronik
                            1. Kode Elektronik
                            2. Tanggal Masuk
                            3. Nama Elektronik
                            4. Jenis Elektronik
                            5. Stok Elektronik
                            6. Harga
                            7. Garansi
                            Masukkan kolom data yang ingin diubah:  '''))

                            kolom_nama = ['kode', 'tanggal_masuk', 'nama', 'jenis', 'stok', 'harga', 'garansi_tahun'][kolom - 1]
                            masukan_data = input(f"\tMasukkan {kolom_nama} baru: ")

                            if kolom == 1:  # Kode Elektronik
                                if len(masukan_data) >= 4 and masukan_data.isalnum():
                                    if any(elektronik.kode == masukan_data for elektronik in dataelektronik if elektronik != produk_ditemukan[0]):
                                        print('Kode sudah ada di database, silahkan masukkan kode baru.')
                                    else:
                                        break
                                else:
                                    print('Kode tidak valid. Minimal 4 karakter, kombinasi huruf dan angka.')
                            elif kolom == 2:  # Tanggal Masuk
                                try:
                                    masukan_data = datetime.strptime(masukan_data, "%d-%m-%Y").date()
                                    break
                                except ValueError:
                                    print('Format tanggal tidak valid. Gunakan DD-MM-YYYY.')
                            elif kolom in [5, 6]:  # Stok dan Harga
                                try:
                                    masukan_data = int(masukan_data)
                                    if masukan_data < 0:
                                        raise ValueError("Input harus berupa bilangan positif.")
                                    break
                                except ValueError as e:
                                    print('Input harus berupa bilangan positif.')
                            elif kolom == 7:  # Garansi
                                try:
                                    durasi_garansi = int(masukan_data)
                                    if durasi_garansi <= 0:
                                        raise ValueError("Durasi garansi harus berupa bilangan positif.")
                                    masukan_data = f"{durasi_garansi} Tahun"
                                    break
                                except ValueError as e:
                                    print('Durasi garansi harus berupa bilangan positif.')
                            else:  
                                break

                        # Update atribut objek Elektronik
                        setattr(produk_ditemukan[0], kolom_nama, masukan_data)
                        print("\n\tData sudah diperbarui!, Silahkan cek data terupdate pada menu 2")
                        break
                    elif konfirmasi == 'T':
                        print("\n\tData tidak jadi diubah")
                        break
                    else:
                        print("\n\tInput yang Anda masukkan salah!")
            else:
                print("\n\tData tidak ditemukan")
        elif Updatedatacust == '2':
            tampilkan_data_elektronik()
        elif Updatedatacust == '3':
            MenuAwal() 
            break  # Keluar dari loop ketika kembali ke menu utama
        else:
            print('\n\nMasukkan yang anda input salah, silahkan input nomor dari range 1 - 3')

# Fungsi menghapus daftar Elektronik dari databases
def DeleteData():
    inputDel = (int(input('''
        Menu Menghapus Daftar Elektronik:
            1. Menghapus Daftar Elektronik dari stok data
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputDel == 1:
        tampilkan_data_elektronik()
        DelKodeID = (input("\n\tMasukkan Kode Elektronik yang ingin dihapus:"))
        ListValue2 = [value2 for dataku in dataelektronik for value2 in dataku.__dict__.values()]
        if DelKodeID not in ListValue2:
            print("\n\tData yang ingin anda hapus tidak ada!")
        else:
            produk_ditemukan = SearchList(DelKodeID)
            ShowList(produk_ditemukan)
            hapus = (input("\n\t Hapus Data (Ya/Tidak)?")).lower()
            if hapus == "ya":                    
                dataelektronik.remove(produk_ditemukan[0])  # Menghapus objek dari daftar dataelektronik
                print("\n\t Data berhasil terhapus!")
                ShowList(dataelektronik)
            else: 
                print("\n\t Data tidak berhasil terhapus!")
    elif inputDel == 2:
        MenuAwal() 
    DeleteData()


# Menu Utama

MenuAwal()