from prettytable import PrettyTable
import datetime


Makanan=[
["Makanan","Soto Ayam" , 15000],
["Makanan","Mie Ayam",15000],
["Makanan","Bakso" ,14000],
["Makanan","Ayam Bakar" ,13000],
["Makanan","Batagor" ,5000]]

Minuman=[
["Minuman","Es Teh",4000],
["Minuman","Air Mineral",5000],
["Minuman","Es Jeruk",5000],
["Minuman","Jus Buah",8000],
["Minuman","Es Campur",10000]]

def show_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] Tampilkan Menu")
    print("[2] Tambahkan Menu")
    print("[3] Ubah Menu")
    print("[4] Hapus Menu")

def jenis():
    print("\n")
    print("----------- JENIS ----------")
    print("[1] MAKANAN")
    print("[2] MINUMAN")

def hapus():
    print("\n")
    print("[1] Hapus salah satu menu")
    print("[2] Hapus semua menu")

def Daftar_diskon():
    print("""
    ===============================================================
                        DAFTAR DISKON
    ===============================================================
    Mendapat Diskon setiap Pembelian 3 Minuman sebesar 10%
    Mendapat Diskon setiap Pembelian 2 Makanan sebesar 5%
    Mendapat Diskon setiap pembayaran melalui E-money sebesar 5%
    Mendapat Diskon saat weekend sebesar 5%
    Mendapat Diskon saat weekdays sebesar 10%
    """)

#Function Makanan
    # Tampilan Menu Makanan
def Menu_Makanan():
    try:
        tabelmakan=PrettyTable(["NO","MENU MAKANAN","HARGA"])
        for index in range (len(Makanan)):
            index+=1
            tabelmakan.add_row([index,Makanan[index-1][1],Makanan[index-1][2]])
        print(tabelmakan)
    except:
        print("Tidak ada menu makanan, harap masukkan kembali menu")
    # Menambahkan Menu Makanan
def tambah_makanan():
    y="y"
    while y=="y":
        Menu_Makanan()
        Makan=["Makanan", str(input("Masukkan makanan: ")), int(input("Masukkan harga: "))]
        letak=str(input("Ingin memilih letak nomor menu? y/n "))
        if letak=="y":
            urutan=int(input("Nomor: "))
            Makanan.insert(urutan-1,Makan)
        else:
            Makanan.append(Makan)
        print("Menu berhasil ditambahkan")
        y=str(input("Ingin menambahkan menu makanan? y/n "))
        #Mengubah Menu Makanan
def ubah_makanan():
    y="y"
    while y=="y":
        Menu_Makanan()
        urutan=int(input("Tuliskan nomor menu yang ingin diubah: "))
        Makanan[urutan-1][1]=str(input("Makanan baru: "))
        kondisi=str(input("Ingin mengubah harga? y/n "))
        if kondisi=="y":
            Makanan[urutan-1][2]=str(input("Harga makanan baru: "))
        else:
            print("Menu berhasil diubah")
        y=str(input("Ingin mengubah menu makanan lagi? y/n "))
        # Menghapus menu makanan
def hapus_makanan():
    Menu_Makanan()
    hapus()
    Kondisi=int(input("Masukkan pilihan anda: "))
    if Kondisi==1:
        urutan=int(input("Menu ke berapa yang ingin dihapus? "))
        print((Makanan[urutan-1]))
        delete=str(input("Apakah ingin menghapus menu y/n "))
        if delete=="y":
            del Makanan[urutan-1]
    elif Kondisi==2:
        for Makan in Makanan:
            Makan.clear()
    else:
        print("Pilihan anda tidak ada dalam daftar")
# Function menu minuman
    # Menampilkan menu minuman
def Menu_Minuman():
    try:
        tabelminum=PrettyTable(["NO","MENU MINUMAN","HARGA"])
        for index in range (len(Minuman)):
            index+=1
            tabelminum.add_row([index,Minuman[index-1][1],Minuman[index-1][2]])
        print(tabelminum)
    except:
        print("Tidak ada menu minuman, harap masukkan kembali menu")
    # Menambahkan Menu Minuman
def tambah_minuman():
    y="y"
    while y=="y":
        Menu_Minuman()
        Minum=["Minuman", str(input("Masukkan minuman: ")), int(input("Masukkan harga: "))]
        letak=str(input("Ingin memilih letak nomor menu? y/n "))
        if letak=="y":
            urutan=int(input("Nomor: "))
            Minuman.insert(urutan-1,Minum)
        else:
            Minuman.append(Minum)
        print("Menu berhasil ditambahkan")
        y=str(input("Ingin menambahkan menu minuman lagi? y/n "))
    # Menghapus menu minuman
def ubah_minuman():
    y="y"
    while y=="y":
        Menu_Minuman()
        urutan=int(input("Tuliskan nomor menu yang ingin diubah: "))
        Minuman[urutan-1][1]=str(input("Minuman baru: "))
        kondisi=str(input("Ingin mengubah harga? y/n "))
        if kondisi=="y":
            Minuman[urutan-1][2]=str(input("Harga minuman baru: "))
        else:
            print("Menu berhasil diubah")
        y=str(input("Ingin mengubah menu minuman lagi? y/n "))
    # Menghapus menu minuman
def hapus_minuman():
    Menu_Minuman()
    hapus()
    Kondisi=int(input("Masukkan pilihan anda: "))
    if Kondisi==1:
        urutan=int(input("Menu ke berapa yang ingin dihapus? "))
        print(Minuman[urutan-1])
        del Minuman[urutan-1]
    elif Kondisi==2:
        for Minum in Minuman:
            Minum.clear()
    else:
        print("Pilihan anda tidak ada dalam daftar")

def admin():
    i="y"
    while i=="y":
        show_menu()
        menu = int(input("PILIH MENU "))
        print("\n")
        if menu==1:
            Menu_Makanan()
            Menu_Minuman()
        elif menu==2:
            n="y" 
            while n=="y":
                jenis()
                pilih=int(input("PILIH JENIS "))
                if pilih==1:
                    tambah_makanan()
                elif pilih==2:
                    tambah_minuman()
                n=str(input("Apakah ingin menambah menu makanan atau minuman lagi? y/n "))
        elif menu==3:
            n="y"
            while n=="y":
                jenis()
                pilih=int(input("PILIH JENIS "))
                if pilih==1:
                    ubah_makanan()
                elif pilih==2:
                    ubah_minuman()
                n=str(input("Apakah ingin mengubah menu makanan atau minuman lagi? y/n "))
        elif menu==4:
            jenis()
            pilih=int(input("PILIH JENIS "))
            if pilih==1:
                hapus_makanan()
            elif pilih==2:
                hapus_minuman()
        else:
            print("Kode tidak tersedia")
        i=str(input("Apakah ingin kembali ke menu utama admin? y/n "))

def pelanggan():
    i="y"
    jumlahMinum=0
    TotalHarga_Minum_SebelumDiskon=0
    TotalHarga_Makan_SebelumDiskon=0
    jumlahMakan=0
    while i=="y"or i=="Y":
        Daftar_diskon()
        Kode=str(input("Masukkan kode jenis pesanan: Makanan(1)/Minuman(2) "))
        if Kode=="1":
            Menu_Makanan()
            pesanan=int(input("Masukkan kode Makanan: cont(1,2,3) "))
            if pesanan > len(Makanan):
                print("Mohon maaf menu tidak tersedia")
                continue
            else:  
                jumlah=int(input("Masukkan jumlah pesanan: "))
                harga=Makanan[pesanan-1][2]*jumlah
            jumlahMakan+=jumlah
            TotalHarga_Makan_SebelumDiskon+=harga
        elif Kode=="2":
            Menu_Minuman()
            pesanan=int(input("Masukkan kode Minuman: cont(1,2,3) "))
            if pesanan > len(Minuman):
                print("Mohon maaf menu tidak tersedia")
                continue
            else:
                jumlah=int(input("Masukkan jumlah pesanan: "))
                harga=Minuman[pesanan-1][2]*jumlah
            jumlahMinum+=jumlah
            TotalHarga_Minum_SebelumDiskon+=harga
        else:
            print("Mohon maaf kode jenis pesanan salah")
        print("==============================================")
        i=str(input("Apakah masih ada yang ingin dipesan? y/n "))

        # DISKON MAKANAN JIKA LEBIIH DARI 2 PESANAN
    if jumlahMakan>=2:
        diskonMakan=TotalHarga_Makan_SebelumDiskon*(5/100)
        totalhargamakan=TotalHarga_Makan_SebelumDiskon-diskonMakan
    else:
        diskonMakan=0
        totalhargamakan=TotalHarga_Makan_SebelumDiskon-diskonMakan

        # DISKON MINUMAN JIKA LEBIIH DARI 3 PESANAN
    if jumlahMinum>=3:
        diskonMinum=TotalHarga_Minum_SebelumDiskon*(10/100)
        totalhargamunum=TotalHarga_Minum_SebelumDiskon-diskonMinum
    else:
        diskonMinum=0
        totalhargamunum=TotalHarga_Minum_SebelumDiskon-diskonMinum

    TotalKeseluruhan=totalhargamakan+totalhargamunum

    # DISKON HARI
    if datetime.datetime.today().weekday() < 5:
        diskonhari=TotalKeseluruhan*(10/100)
        totalsemua=TotalKeseluruhan-diskonhari
    else:
        diskonhari=TotalKeseluruhan*(5/100)
        totalsemua=TotalKeseluruhan-diskonhari

    def rincian():
        print("""\n================RINCIAN HARGA=============""" )
        print("Total harga makanan asli   : Rp."+str(int(TotalHarga_Makan_SebelumDiskon)))
        print("Total harga minuman asli   : Rp."+str(int(TotalHarga_Minum_SebelumDiskon)))
        print("Diskon Makanan             : Rp."+str(int(diskonMakan)))
        print("Diskon Minuman             : Rp."+str(int(diskonMinum)))
        print("Diskon Hari                : Rp."+str(int(diskonhari)))

    def penutup():
        print("""\n==========TERIMA KASIH TELAH BELANJA DI KANTIN BESTIE==========""" )
        exit()

    emoney=str(input("Apakah pembayaran menggunakan E-money? y/n "))
    if emoney=="y" or emoney=="Y":
        diskonEmoney=TotalKeseluruhan*(5/100)
        totalAkhir=totalsemua-diskonEmoney
        rincian()
        print("Diskon Pembayaran E-money  : Rp."+str(int(diskonEmoney)))
        print("\nAnda harus membayar tagihan sebesar RP."+str(int(totalAkhir)))
        penutup()
    else:
        rincian()
        print("Diskon Pembayaran E-money  : Rp."+str(0))
        print("\nAnda harus membayar tagihan sebesar RP."+str(int(totalsemua)))
        penutup()
        
x="y"
while x=="y":
    print("""
[1] ADMIN
[2] PELANGGAN
[3] KELUAR
""")
    login=int(input("Login sebagai? "))
    if login==1:
        admin()
    elif login==2:
        pelanggan()
    elif login==3:
        exit()
    else:
        print("Kode salah!")
    x=str(input("Ingin kembali ke menu login? y/n "))
print("Terima Kasih")
