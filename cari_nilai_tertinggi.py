def cari_nilai_tertinggi():
    # Inisialisasi list kosong untuk menyimpan nilai
    nilai = []
    
    # Menggunakan perulangan untuk input nilai 5 siswa
    for i in range(5):
        try:
            # Meminta input nilai dari pengguna
            input_nilai = float(input(f"Masukkan nilai siswa ke-{i+1}: "))
            nilai.append(input_nilai)
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            # Jika input tidak valid, ulangi iterasi ini
            i -= 1
    
    # Mencari nilai tertinggi dan indeksnya
    nilai_tertinggi = max(nilai)
    indeks_tertinggi = nilai.index(nilai_tertinggi)
    
    # Menampilkan hasil
    print("\nHasil Analisis:")
    print(f"Nilai siswa: {nilai}")
    print(f"Nilai tertinggi: {nilai_tertinggi}")
    print(f"Diperoleh oleh siswa ke-{indeks_tertinggi + 1}")

# Menjalankan program
if __name__ == "__main__":
    print("PROGRAM PENCARI NILAI TERTINGGI")
    print("==============================")
    cari_nilai_tertinggi()
