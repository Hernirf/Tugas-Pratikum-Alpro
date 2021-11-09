import datetime

def Daftar_menu():
    print("""
                        SELAMAT DATANG DI KANTIN BESTIE
    =========================================================================
                                    DAFTAR MENU
    =========================================================================
    1. MAKANAN:                             2. MINUMAN:
        a. Soto Ayam    = Rp.15.000,00          a. Es Teh       = Rp.4.000,00
        b. Mie Ayam     = Rp.15.000,00          b. Air Mineral  = Rp.5.000,00 
        c. Bakso        = Rp.14.000,00          c. Es Jeruk     = Rp.5.000,00 
        d. Ayam Bakar   = Rp.13.000,00          d. Jus Buah     = Rp.8.000,00 
        e. Batagor      = Rp.5.000,00           e. Es Campur    = Rp.10.000,00 
    """)
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

Menu=[
["Makanan","Soto Ayam" , 15000],
["Makanan","Mie Ayam",15000],
["Makanan","Bakso" ,14000],
["Makanan","Ayam Bakar" ,13000],
["Makanan","Batagor" ,5000],
["Minuman","Es Teh",4000],
["Minuman","Air Mineral",5000],
["Minuman","Es Jeruk",5000],
["Minuman","Jus Buah",8000],
["Minuman","Es Campur",10000]]

i="y"
jumlahMinum=0
TotalHarga_Minum_SebelumDiskon=0
TotalHarga_Makan_SebelumDiskon=0
jumlahMakan=0
while i=="y"or i=="Y":
    Daftar_menu()
    Daftar_diskon()
    Kode=str(input("Masukkan kode jenis pesanan: Makanan(1)/Minuman(2) "))
    if Kode=="1":
        pesanan=str(input("Masukkan kode Makanan: (a s/d e) "))
        if pesanan=="a" or pesanan=="A":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[0][2]*jumlah
        elif pesanan=="b" or pesanan=="B":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[1][2]*jumlah
        elif pesanan=="c" or pesanan=="C":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[2][2]*jumlah
        elif pesanan=="d" or pesanan=="D":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[3][2]*jumlah
        elif pesanan=="e" or pesanan=="E":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[4][2]*jumlah
        else:
            print("Mohon maaf menu tidak tersedia")  
        jumlahMakan+=jumlah
        TotalHarga_Makan_SebelumDiskon+=harga
    elif Kode=="2":
        pesanan=str(input("Masukkan kode Minuman: (a s/d e) "))
        if pesanan=="a" or pesanan=="A":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[5][2]*jumlah
        elif pesanan=="b" or pesanan=="B":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[6][2]*jumlah
        elif pesanan=="c" or pesanan=="C":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[7][2]*jumlah
        elif pesanan=="d" or pesanan=="D":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga= Menu[8][2]*jumlah
        elif pesanan=="e" or pesanan=="E":
            jumlah=int(input("Masukkan jumlah pesanan: "))
            harga=Menu[9][2]*jumlah
        else:
            print("Mohon maaf menu tidak tersedia")
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