akundefault=[{"Username":"Herni Suhartati", "katasandi":"hehe"}]
def Menu_utama():
    print("""
    ====================================
        SELAMAT DATANG DI MENU UTAMA
    ====================================
    1. BUAT AKUN
    2. LOGIN
    3. KELUAR
    """)

i="y"
while i=="y" or i=="Y":
    Menu_utama()
    Kode=str(input("Masukkan kode yang ingin kamu lakukan: (1 s/d 3) "))
    if Kode=="1":
        userbaru={}
        userbaru["Username"]=str(input("Masukkan username baru: "))
        userbaru["katasandi"]=str(input("Masukkan kata sandi baru: "))
        akundefault.append(userbaru)
        print("Anda telah berhasil buat akun!")
    elif Kode=="2":
        login=0
        while login<3:
            Username=str(input("Masukkan username anda: "))
            katasandi=str(input("Masukkan kata sandi anda: "))
            pengguna= next((userbaru for userbaru in akundefault if Username==userbaru["Username"] and katasandi==userbaru["katasandi"]),False)
            if pengguna:
                print("Selamat Datang", Username)
                break
            else:
                print("Batas percobaan login: 3 dan percobaan anda sudah yang ke",login+1)
            login+=1
            print("==============================================================")
    elif Kode=="3":
        print("Terima kasih")
        exit()
    else:
        print("Kode tidak terbaca")
    i=input("\nApakah anda ingin kembali memilih menu? y/n " )
print("Terima kasih")