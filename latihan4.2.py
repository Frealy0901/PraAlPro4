# memasukan fungsi x,y,z
def cek_digit_belakang(x, y, z):
    
    # Mengeksekusi
    if x % 10 == y % 10 or y % 10 == z % 10 or z % 10 == x % 10:
        return "True"               # Menambahkan true karena jika tidak akan menghasilkan none
    else:
        return "False"              # Menambahkan false karena jika tidak akan menghasilkan none juga 
    
# Menampilkan
print(f"hasilnya =",cek_digit_belakang(10,20,30))           #True
print(f"hasilnya =",cek_digit_belakang(145, 5, 100))        #True
print(f"hasilnya =",cek_digit_belakang(71, 187, 18))        #False
print(f"hasilnya =",cek_digit_belakang(1024, 14, 94))       #True
print(f"hasilnya =",cek_digit_belakang(53, 8900, 658))      #False