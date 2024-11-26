import math

# Fungsi untuk menampilkan menu operasi
def menu():
    print("===== Scientific Calculator =====")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (^)")
    print("6. Akar kuadrat (√)")
    print("7. Sinus (sin)")
    print("8. Cosinus (cos)")
    print("9. Tangen (tan)")
    print("10. Logaritma (log)")
    print("11. Eksponensial (exp)")
    print("12. Keluar")

# Fungsi untuk menjalankan kalkulator scientific
def kalkulator():
    while True:
        menu()
        pilihan = input("Masukkan pilihan (1-12): ")
        
        if pilihan == '12':
            print("Kalkulator ditutup.")
            break
        
        if pilihan in ['1', '2', '3', '4', '5']:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                print(f"Hasil: {num1} + {num2} = {num1 + num2}")
            elif pilihan == '2':
                print(f"Hasil: {num1} - {num2} = {num1 - num2}")
            elif pilihan == '3':
                print(f"Hasil: {num1} * {num2} = {num1 * num2}")
            elif pilihan == '4':
                if num2 != 0:
                    print(f"Hasil: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Pembagian dengan nol!")
            elif pilihan == '5':
                print(f"Hasil: {num1} ^ {num2} = {math.pow(num1, num2)}")
        
        elif pilihan == '6':
            num = float(input("Masukkan angka: "))
            if num >= 0:
                print(f"Hasil: √{num} = {math.sqrt(num)}")
            else:
                print("Error: Akar kuadrat dari angka negatif!")
        
        elif pilihan == '7':
            degree = float(input("Masukkan derajat: "))
            print(f"Hasil: sin({degree}) = {math.sin(math.radians(degree))}")
        
        elif pilihan == '8':
            degree = float(input("Masukkan derajat: "))
            print(f"Hasil: cos({degree}) = {math.cos(math.radians(degree))}")
        
        elif pilihan == '9':
            degree = float(input("Masukkan derajat: "))
            print(f"Hasil: tan({degree}) = {math.tan(math.radians(degree))}")
        
        elif pilihan == '10':
            num = float(input("Masukkan angka: "))
            if num > 0:
                print(f"Hasil: log({num}) = {math.log10(num)}")
            else:
                print("Error: Logaritma hanya untuk angka positif!")
        
        elif pilihan == '11':
            num = float(input("Masukkan angka: "))
            print(f"Hasil: exp({num}) = {math.exp(num)}")
        
        else:
            print("Pilihan tidak valid. Coba lagi!")

# Menjalankan program kalkulator
kalkulator()
