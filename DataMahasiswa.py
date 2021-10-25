print("------------DATA MAHASISWA--------------\n")

Login=str(input("Hai apakah kamu mahasiswa Universitas Mulawarman? y/n "))
while Login=="y":
    DataMahasiswa={
"Nama Mahasiswa": str(input("Sebutkan nama lengkap anda! ")),
"NIM Mahasiswa": int(input("Berapa NIM anda? ")),
"Universitas Mahasiswa": "Universitas Mulawarman",
"Fakultas Mahasiswa": str(input("Apa fakultas anda? ")),
"Program Studi Mahasiswa": str(input("Apa prodi anda? ")),
"Semester Mahasiswa": str(input("Anda merupakan mahasiswa semester berapa? ")),
"IPK Mahasiswa": float(input("Berapa nilai IPK anda? "))
    }
    print("\n-----------------DATA",DataMahasiswa["Nama Mahasiswa"],"----------------------")
    print("Nama         :",DataMahasiswa["Nama Mahasiswa"])
    print("NIM          :",DataMahasiswa["NIM Mahasiswa"])
    print("Universitas  :",DataMahasiswa["Universitas Mahasiswa"])
    print("Fakultas     :",DataMahasiswa["Fakultas Mahasiswa"])
    print("Program Studi:",DataMahasiswa["Program Studi Mahasiswa"])
    print("Semester     :",DataMahasiswa["Semester Mahasiswa"])
    print("Nilai IPK    :",DataMahasiswa["IPK Mahasiswa"])
    print("-----------------------------------------------------------------\n")
    Login=str(input("Apakah ingin mengubah data mahasiswa mu? y/n "))
print("Terima kasih telah mengisi\n")