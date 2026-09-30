bulan = int(input("Masukkan Bulan (1-12): "))
tahun = int(input("Masukkan Tahun: "))

i = 0
while i < 1:
    if bulan < 1 or bulan > 12:
        print("Input bulan tidak valid!")
    else:
        if bulan in [1, 3, 5, 7, 8, 10, 12]:
            jumlah_hari = 31
        elif bulan in [4, 6, 9, 11]:
            jumlah_hari = 30
        elif bulan == 2:
            if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
                jumlah_hari = 29
            else:
                jumlah_hari = 28
        
        print("Jumlah hari pada bulan", bulan, "tahun", tahun, "adalah", jumlah_hari, "hari")
    
    i = i + 1