print("------------DATA MAHASISWA--------------\n")

Login=str(input("Hai apakah kamu berkuliah di Universitas Mulawarman? y/n "))
while Login=="y":
    DataMahasiswa={
"Nama Mahasiswa": str(input("MASUKKAN NAMA ANDA: ")),
"NIM Mahasiswa": int(input("MASUKKAN NIM ANDA: ")),
"Universitas Mahasiswa": "Universitas Mulawarman",
"Fakultas Mahasiswa": str(input("MASUKKAN FAKULTAS ANDA: ")),
"Program Studi Mahasiswa": str(input("MASUKKAN PRODI ANDA: ")),
"Semester Mahasiswa": str(input("MASUKKAN SEMESTER ANDA: ")),
"IPK Mahasiswa": float(input("MASUKKAN IPK ANDA: "))
    }
    print("\n-----------------Data",DataMahasiswa["Nama Mahasiswa"],"----------------------")
    print("Nama         :",DataMahasiswa["Nama Mahasiswa"])
    print("NIM          :",DataMahasiswa["NIM Mahasiswa"])
    print("Universitas  :",DataMahasiswa["Universitas Mahasiswa"])
    print("Fakultas     :",DataMahasiswa["Fakultas Mahasiswa"])
    print("Program Studi:",DataMahasiswa["Program Studi Mahasiswa"])
    print("Semester     :",DataMahasiswa["Semester Mahasiswa"])
    print("Nilai IPK    :",DataMahasiswa["IPK Mahasiswa"])
    print("-----------------------------------------------------------------\n")
    Login=str(input("Apakah ingin mengubah biodata anda? y/n "))
print("TERIMA KASIH TELAH MENGISI\n")
