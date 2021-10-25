
print("-------------KONVERSI SUHU KE DALAM CELCIUS----------------\n")
mencoba=input("Apakah ingin mencoba? (y/n) ")
while mencoba =="y":
    print("""
    Kode Fahrenheit= 'F'/'f'
    Kode Kelvin= 'K'/'k'
    Kode Reamur= 'R'/ 'r'
    """)
    Suhu=str(input("Masukkan kode skala suhu yang ingin di konversikan: "))
    if Suhu=="F" or Suhu=="f":
        Fahrenheit=int(input("Masukkan derajat suhunya: "))
        Celcius=int(Fahrenheit-32)*5/9
        print("Konversi suhu F ke C yaitu F=", str(round(Celcius,2)),"C")
    elif Suhu=="K" or Suhu=="k":
        Kelvin=int(input("Masukkan derajat suhunya: "))
        Celcius=Kelvin-273
        print("Konversi suhu K ke C yaitu K=", str(round(Celcius,2)),"C")
    elif Suhu=="R" or Suhu=="r":
        Reamur=int(input("Masukkan derajat suhunya: "))
        Celcius=Reamur*5/4
        print("Konversi suhu R ke C yaitu R=", str(round(Celcius,2)),"C")
    else:
        print("Mohon maaf kode yang anda masukkan salah")
    print("-------------------------------------------------------------------\n")
    mencoba=input("Apakah anda ingin menghitung konversi lagi? (y/n) ")
print("\nTerima kasih, jaga kesehatannya yaaa!\n")