import os

class Kasir():
    def __init__(self):
        self.main_title = """===============================
SELAMAT DATANG DI TOKO BUKU ABC"""
        self.main_action = """Pilih menu yang ingin diakses :
1. Pembelian
2. Pembayaran
3. Keluar"""
        # Key = index, value = [nama_buku, kategori, jumlah halaman, harga]
        self.data_buku = {
                        0 : ["BukuA", 'Komik', 150, 30000],
                        1 : ["BukuB", 'Komputer', 240, 98000],
                        2 : ["BukuC",'Novel', 350, 150000]
                    }
        self.keranjang = []
        self.notif_buku_added = False
    def menu_utama(self):
        print(self.main_title)
        print(self.main_action)
        main_choice = input("Menu yang dipilih: ")
        if main_choice == "1":
            os.system("cls")
            self.menu_pembelian()
        elif main_choice == "2":
            os.system("cls")
            self.menu_pembayaran()
        elif main_choice == "3":
            print("Terima Kasih Atas Kunjungan Anda Ke Toko Buku ABC.")
            input()
            os.system("cls")
        else:
            print("Pilihan menu tidak ada. Klik 'Enter' untuk memilih kembali.")
            input()
            os.system("cls")
            self.menu_utama()
    def menu_pembelian(self):
        jumlah_buku_tersedia = len(self.data_buku.keys())
        print(self.main_title)
        print("\nDaftar Buku Yang Tersedia")
        for x in range(jumlah_buku_tersedia):
            print("{}. {} (Kategori: {}, Jumlah Halaman: {}, Harga: Rp.{})".format(str(x+1),\
                self.data_buku[x][0], self.data_buku[x][1], self.data_buku[x][2],\
                self.data_buku[x][3]))
        print("{}. Kembali Ke Menu Utama\n".format(str(jumlah_buku_tersedia + 2)))
        # Notif setiap add buku ke keranjang
        if self.notif_buku_added:
            print("Buku Telah Dimasukkan Ke Keranjang")
            self.notif_buku_added = False
        # Hanya muncul ketika isi keranjang tidak kosong
        if len(self.keranjang) != 0:
            print("Total Jumlah Barang di Keranjang: {} buku.".format(len(self.keranjang)))
        try:
            add_buku = int(input("Pilih buku: "))
        except:
            print("Pilihan buku tidak ada. Klik 'Enter' untuk memilih kembali.")
            input()
            os.system("cls")
            self.menu_pembelian()
        else:
            # Opsi untuk kembali ke menu utama
            if add_buku == jumlah_buku_tersedia + 2: #Misal daftar buku ada 3, kalo input 5 bakal masuk kesini
                os.system("cls")
                self.menu_utama()
            # Opsi untuk pilihan lainnya
            else:
                if add_buku - 1 in self.data_buku.keys():
                    self.keranjang.append(add_buku - 1)
                    tambah_lagi = input("Ingin Menambah Buku Lagi (Ya/Tidak)? ")
                    if tambah_lagi == "Ya":
                        self.notif_buku_added = True
                        os.system("cls")
                        self.menu_pembelian()
                    elif tambah_lagi == "Tidak":
                        os.system("cls")
                        self.menu_utama()
                    else:
                        print("Pilihan tidak ada. Tekan 'Enter' untuk kembali ke Menu Pembelian. ")
                        input()
                        os.system("cls")
                        self.menu_pembelian()
                else:
                    print("Pilihan tidak ada. Tekan 'Enter' untuk kembali ke Menu Pembelian. ")
                    input()
                    os.system("cls")
                    self.menu_pembelian()
    def menu_pembayaran(self):
        print(self.main_title)
        if len(self.keranjang) == 0:
            print("Keranjang masih kosong. Tekan 'Enter' untuk kembali ke Menu Utama.")
            input()
            os.system("cls")
            self.menu_utama()
        else:
            total_harga = 0
            print("Daftar Buku di Keranjang")
            for nomer, isi in enumerate(self.keranjang):
                print("{}. {} ({})\t: Rp.{}".format(nomer+1, self.data_buku[isi][0],\
                    self.data_buku[isi][1], str(self.data_buku[isi][3])))
                total_harga += self.data_buku[isi][3]
            print("Total Harga\t\t: Rp.{}".format(str(total_harga)))
            # Cek apakah uang yang dibayar itu cukup
            try:
                total_uang = int(input("Masukkan jumlah uang pembayaran: Rp."))
            except:
                print("Tolong masukkan nilai angka, bukan huruf.")
                input()
                os.system("cls")
                self.menu_pembayaran()
            else:
                if  total_uang > total_harga:
                    print("Uang kembalian: Rp.{}".format(total_uang - total_harga))
                    input()
                    self.exit()
                else:
                    print("Uang yang anda berikan tidak mencukupi")
                    input()
                    os.system('cls')
                    self.menu_pembayaran()
    def run(self):
        self.menu_utama()
    def exit(self):
        print("Terima Kasih Atas Kunjungan Anda Ke Toko Buku ABC.")
        input()
        os.system("cls")
        
Orang1 = Kasir()
Orang1.run()