def hitung_rata_rata_dan_status():
    """
    Fungsi untuk menghitung rata-rata nilai dari 3 mata pelajaran
    dan menentukan status kelulusan berdasarkan kriteria:
    - Lulus jika rata-rata >= 75
    - Tidak lulus jika rata-rata < 75
    """
    print("PROGRAM PENENTU KELULUSAN")
    print("=========================")
    print("Masukkan nilai untuk 3 mata pelajaran (skala 0-100):")
    
    # List untuk menyimpan nilai-nilai mata pelajaran
    nilai_mata_pelajaran = []
    mata_pelajaran = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris"]
    
    # Input nilai untuk 3 mata pelajaran
    for i in range(3):
        while True:
            try:
                nilai = float(input(f"Nilai {mata_pelajaran[i]}: "))
                
                # Validasi nilai (harus antara 0-100)
                if nilai < 0 or nilai > 100:
                    print("Error: Nilai harus dalam rentang 0-100! Silakan masukkan kembali.")
                    continue
                
                # Tambahkan nilai ke list
                nilai_mata_pelajaran.append(nilai)
                break
                
            except ValueError:
                print("Error: Input tidak valid! Masukkan angka.")
    
    # Hitung rata-rata nilai
    total_nilai = sum(nilai_mata_pelajaran)  # Operator penjumlahan untuk mencari total
    jumlah_mata_pelajaran = len(nilai_mata_pelajaran)  # Fungsi len() untuk mencari jumlah elemen
    rata_rata = total_nilai / jumlah_mata_pelajaran  # Operator pembagian untuk mencari rata-rata
    
    # Tentukan status kelulusan menggunakan operator perbandingan
    if rata_rata >= 75:  # Operator perbandingan (>=) untuk membandingkan rata-rata dengan batas kelulusan
        status = "LULUS"
    else:
        status = "TIDAK LULUS"
    
    # Tampilkan hasil
    print("\n===== HASIL PERHITUNGAN =====")
    for i in range(jumlah_mata_pelajaran):
        print(f"Nilai {mata_pelajaran[i]}: {nilai_mata_pelajaran[i]}")
    
    print(f"\nTotal Nilai: {total_nilai}")
    print(f"Rata-rata Nilai: {rata_rata:.2f}")
    print(f"Status Kelulusan: {status}")
    print("=============================")
    
    # Tambahan: Analisis selisih dari batas kelulusan
    selisih = abs(rata_rata - 75)  # Fungsi abs() untuk mendapatkan nilai absolut
    
    if rata_rata >= 75:
        print(f"Anda melampaui batas kelulusan sebesar {selisih:.2f} poin.")
    else:
        print(f"Anda masih kurang {selisih:.2f} poin untuk mencapai batas kelulusan.")

def main():
    """
    Fungsi utama program penentu kelulusan.
    """
    print("Selamat datang di Program Penentu Kelulusan!")
    print("Program ini akan menghitung rata-rata nilai dari 3 mata pelajaran")
    print("dan menentukan status kelulusan (lulus jika rata-rata >= 75).")
    print("")
    
    # Jalankan perhitungan rata-rata dan penentuan status
    hitung_rata_rata_dan_status()
    
    print("\nTerima kasih telah menggunakan Program Penentu Kelulusan!")

# Jalankan program jika file dieksekusi langsung
if __name__ == "__main__":
    main()
