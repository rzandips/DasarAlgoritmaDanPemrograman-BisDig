def hitung_total_bayar():
    # Input total belanja dari pengguna
    try:
        total_belanja = float(input("Masukkan total belanja (Rp): "))
        
        # Validasi input harus positif
        if total_belanja < 0:
            print("Total belanja tidak boleh negatif!")
            return
        
        # Inisialisasi variabel diskon
        diskon = 0
        
        # Struktur kontrol percabangan untuk menentukan diskon
        if total_belanja > 500000:
            # Jika total belanja lebih dari Rp500.000, berikan diskon 10%
            diskon = 0.1 * total_belanja
            print(f"\nSelamat! Anda mendapatkan diskon 10%")
        else:
            # Jika total belanja kurang dari atau sama dengan Rp500.000, tidak ada diskon
            print(f"\nAnda belum mendapatkan diskon. Belanja minimal Rp500.000 untuk mendapatkan diskon 10%")
        
        # Menghitung total yang harus dibayar
        total_bayar = total_belanja - diskon
        
        # Menampilkan rincian pembayaran
        print("\n===== RINCIAN PEMBAYARAN =====")
        print(f"Total Belanja: Rp{total_belanja:,.2f}".replace(",", "."))
        print(f"Diskon: Rp{diskon:,.2f}".replace(",", "."))
        print(f"Total Bayar: Rp{total_bayar:,.2f}".replace(",", "."))
        
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

# Menjalankan program
if __name__ == "__main__":
    print("PROGRAM HITUNG DISKON E-COMMERCE")
    print("================================")
    hitung_total_bayar()
