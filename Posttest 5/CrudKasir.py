from prettytable import PrettyTable
import datetime

Makanan=[
{"makan":"Soto Ayam", "harga": 15000},
{"makan":"Mie Ayam", "harga": 15000},
{"makan":"Bakso", "harga": 14000},
{"makan":"Ayam Bakar", "harga": 13000},
{"makan":"Batagor", "harga": 5000}] 

Minuman=[
{"minum":"Es Teh", "harga": 4000},
{"minum":"Air Mineral", "harga": 5000},
{"minum":"Es Jeruk", "harga" : 5000},
{"minum":"Jus Buah", "harga" : 8000},
{"minum":"Es Campur", "harga" : 10000}]

def show_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] Tampilkan Menu")
    print("[2] Tambahkan Menu")
    print("[3] Ubah Menu")
    print("[4] Hapus Menu")
    print("[5] Tidak ada pilihan")
    

def jenis():
    print("\n")
    print("----------- JENIS ----------")
    print("[1] MAKANAN")
    print("[2] MINUMAN")
    print("[3] TIDAK ADA PILIHAN")

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
    if len(Makanan)<= 0:
        print("Tidak ada menu makanan")
    else:
        for index in range(len(Makanan)):
            index+=1
            Makanan[index-1].update({"no":index})
        tabelmakan=PrettyTable(["NO","MENU MAKANAN","HARGA"])
        for Makan in Makanan:
            tabelmakan.add_row([Makan["no"],Makan["makan"],Makan["harga"]])
        print(tabelmakan)
    # Menambahkan Menu Makanan
def tambah_makanan():
    try:
        y="y"
        while y=="y":
            Menu_Makanan()
            Makan={}
            Makan["no"]=len(Makanan)+1
            Makan["makan"]=str(input("Masukkan makanan: "))
            Makan["harga"]=int(input("Masukkan harga: "))
            Makanan.append(Makan)
            print("Menu berhasil ditambahkan")
            y=str(input("Ingin menambahkan menu makanan? y/n "))
    except:
        print("Perhatikan ketikkan anda, harga hanya menerima angka")
        #Mengubah Menu Makanan
def ubah_makanan():
    try:
        y="y"
        while y=="y":
            Menu_Makanan()
            urutan=int(input("Tuliskan nomor menu yang ingin diubah: "))
            for Makan in Makanan:
                if Makan["no"]==urutan:
                    makan=str(input("Masukkan makanan baru: "))
                    harga=int(input("Masukkan harg baru: "))
                    Makan["makan"]=makan
                    Makan["harga"]=harga
            print("Menu berhasil diubah")
            y=str(input("Ingin mengubah menu makanan lagi? y/n "))
    except:
        print("Perhatikan ketikkan anda, nomor dan harga hanya menerima angka")
        # Menghapus menu makanan
def hapus_makanan():
    try:
        Menu_Makanan()
        hapus()
        Kondisi=int(input("Masukkan pilihan anda: "))
        if Kondisi==1:
            urutan=int(input("Nomor menu ke berapa yang ingin dihapus? "))
            for Makan in Makanan:
                if Makan["no"]==urutan:
                    print(Makan["no"], Makan["makan"], Makan["harga"])
                    delete=str(input("Apakah ingin menghapus menu y/n "))
                    if delete=="y":
                        for index in range(len(Makanan)):
                            if Makanan[index]["no"]==urutan:
                                del Makanan[index]
                                break
        elif Kondisi==2:
            Menu_Makanan()
            delete=str(input("Apakah ingin menghapus menu y/n "))
            if delete=="y":
                Makanan.clear()
        else:
            print("Pilihan anda tidak ada dalam daftar")
    except:
        print("Perhatikan ketikkan anda, pilihan dan nomor hanya menerima angka")
# Function menu minuman
    # Menampilkan menu minuman
def Menu_Minuman():
    if len(Minuman)<= 0:
        print("Tidak ada menu minuman")
    else:
        for index in range(len(Minuman)):
            index+=1
            Minuman[index-1].update({"no":index})
        tabelminum=PrettyTable(["NO","MENU MAKANAN","HARGA"])
        for Minum in Minuman:
                tabelminum.add_row([Minum["no"],Minum["minum"],Minum["harga"]])
        print(tabelminum)
    # Menambahkan Menu Minuman
def tambah_minuman():
    try:
        y="y"
        while y=="y":
            Menu_Minuman()
            Minum={}
            Minum["no"]=len(Minuman)+1
            Minum["minum"]=str(input("Masukkan minuman: "))
            Minum["harga"]=int(input("Masukkan harga: "))
            Minuman.append(Minum)
            print("Menu berhasil ditambahkan")
            y=str(input("Ingin menambahkan menu minuman? y/n "))
    except:
        print("Perhatikan ketikkan anda, harga hanya menerima angka")
    # Menghapus menu minuman
def ubah_minuman():
    try:
        y="y"
        while y=="y":
            Menu_Minuman()
            urutan=int(input("Tuliskan nomor menu yang ingin diubah: "))
            for Minum in Minuman:
                if Minum["no"]==urutan:
                    minum=str(input("Masukkan minuman baru: "))
                    harga=int(input("Masukkan harga baru: "))
                    Minum["minum"]=minum
                    Minum["harga"]=harga
            print("Menu berhasil diubah")
            y=str(input("Ingin mengubah menu minuman lagi? y/n "))
    except:
        print("Perhatikan ketikkan anda, nomor dan harga hanya menerima angka")
    # Menghapus menu minuman
def hapus_minuman():
    try:
        Menu_Minuman()
        hapus()
        Kondisi=int(input("Masukkan pilihan anda: "))
        if Kondisi==1:
            urutan=int(input("Nomor menu ke berapa yang ingin dihapus? "))
            for Minum in Minuman:
                if Minum["no"]==urutan:
                    print(Minum["no"], Minum["minum"], Minum["harga"])
                    delete=str(input("Apakah ingin menghapus menu y/n "))
                    if delete=="y":
                        for index in range(len(Minuman)):
                            if Minuman[index]["no"]==urutan:
                                del Minuman[index]
                                break
        elif Kondisi==2:
            Menu_Minuman()
            delete=str(input("Apakah ingin menghapus menu y/n "))
            if delete=="y":
                Minuman.clear()
        else:
            print("Pilihan anda tidak ada dalam daftar")
    except:
        print("Perhatikan ketikkan anda, pilihan dan nomor hanya menerima angka")

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
                elif pilih==3:
                    break
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
                elif pilih==3:
                    break
                n=str(input("Apakah ingin mengubah menu makanan atau minuman lagi? y/n "))
        elif menu==4:
            jenis()
            pilih=int(input("PILIH JENIS "))
            if pilih==1:
                hapus_makanan()
            elif pilih==2:
                hapus_minuman()
            elif pilih==3:
                    break
        elif menu==5:
            break
        else:
            print("Kode tidak tersedia")
        i=str(input("Apakah ingin kembali ke menu utama admin? y/n "))

def pelanggan():
    try:
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
                    harga=Makanan[pesanan-1]["harga"]*jumlah
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
                    harga=Minuman[pesanan-1]["harga"]*jumlah
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
    except:
        print("Perhatikan ketikkan anda")   

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
