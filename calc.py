def calculate(operator, angka1, angka2):
    #fungsi calculate
    if operator == '+':
        hasil = angka1 + angka2
        print(f"Hasil penjumlahan dari {angka1} + {angka2} = {hasil}")
    elif operator == '-':
        hasil = angka1 - angka2
        print(f"Hasil pengurangan dari {angka1} - {angka2} = {hasil}")
    elif operator == '*':
        hasil = angka1 * angka2
        print(f"Hasil perkalian dari {angka1} * {angka2} = {hasil}")
    elif operator == '/':
        hasil = angka1 / angka2
        print(f"Hasil pembagian dari {angka1} / {angka2} = {hasil}")
    else:
        print("Maaf, operator tidak tersedia atau salah, silahkan coba lagi ya.")

if __name__ == "__main__":
    #input itu scanf
    operator = input("Pilih operator matematika >>> (+, -, *, / ): ")
    angka1 = float(input("Masukan angka1: "))
    angka2 = float(input("Masukan angka2: "))

    calculate(operator, angka1, angka2)