def faktorial_rekursif(n):
    """
    Fungsi untuk menghitung faktorial dari bilangan n menggunakan metode rekursif.
    
    Args:
        n (int): Bilangan yang akan dihitung faktorialnya
        
    Returns:
        int: Hasil faktorial dari n
    """
    # Basis: faktorial dari 0 dan 1 adalah 1
    if n == 0 or n == 1:
        return 1
    # Rekursi: n! = n * (n-1)!
    else:
        return n * faktorial_rekursif(n - 1)

def main():
    print("PROGRAM HITUNG FAKTORIAL (METODE REKURSIF)")
    print("==========================================")
    
    try:
        # Meminta input bilangan dari pengguna
        bilangan = int(input("Masukkan bilangan untuk dihitung faktorialnya: "))
        
        # Validasi input: harus bilangan non-negatif
        if bilangan < 0:
            print("Error: Faktorial hanya didefinisikan untuk bilangan non-negatif!")
            return
        
        # Menghitung faktorial menggunakan fungsi rekursif
        hasil = faktorial_rekursif(bilangan)
        
        # Menampilkan hasil
        print(f"\nFaktorial dari {bilangan} adalah: {hasil}")
        
        # Menampilkan proses perhitungan faktorial
        print("\nProses perhitungan:")
        tampilkan_proses_faktorial(bilangan)
        
    except ValueError:
        print("Error: Input harus berupa bilangan bulat!")

def tampilkan_proses_faktorial(n):
    """
    Fungsi untuk menampilkan proses perhitungan faktorial secara visual.
    
    Args:
        n (int): Bilangan yang faktorialnya dihitung
    """
    if n == 0 or n == 1:
        print(f"{n}! = 1")
    else:
        # Bangun string untuk menampilkan proses perhitungan
        proses = f"{n}! = {n}"
        hasil = n
        
        for i in range(n-1, 0, -1):
            proses += f" × {i}"
            hasil *= i
        
        proses += f" = {hasil}"
        print(proses)

# Menjalankan program jika file dieksekusi langsung
if __name__ == "__main__":
    main()
