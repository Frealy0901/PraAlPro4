# Fungsi untuk konversi suhu menggunakan lambda function
celcius_ke_fahrenheit = lambda celcius: round((9/5) * celcius + 32)         #round untuk membulatkan
celcius_ke_reamur = lambda celcius: round(0.8 * celcius)                    #round untuk membulatkan


# Menampilkan Suhu yang sudah di konversikan
print(f"input C =",celcius_ke_fahrenheit(100))
print(f"input C =",celcius_ke_reamur(80))
print(f"input C =",celcius_ke_fahrenheit(0))