# Memasukan Fungsi a,b,c
def cek_angka(a, b, c):

    # Mengeksekusi
    if a != b and b != c and c != a:
        return (a + b == c or b + a == c or c + b == a)     # menggunakan boolean expression, akan otomatis True 
    else:                                               
        return                                 # Return kosong karena sudah pasti selain dari diatas hasilnya false
   
# Memunculkan hasil
print(f"Angka tersebut =",cek_angka(1,2,3))         #True
print(f"Angka tersebut =",cek_angka(20,9,7))        #False
print(f"Angka tersebut =",cek_angka(4,3,1))         #True
print(f"Angka tersebut =",cek_angka(13,14,16))      #False