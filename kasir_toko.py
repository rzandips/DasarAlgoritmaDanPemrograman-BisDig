def hitung_total_pembelian():
    """
    Fungsi untuk menghitung total harga pembelian 3 barang.
    
    Returns:
        float: Total harga pembelian
    """
    print("SISTEM KASIR TOKO")
    print("================")
    print("Masukkan harga untuk 3 barang:")
    
    total_harga = 0
    
    # Meminta input harga untuk 3 barang
    for i in range(3):
        while True:
            try:
                harga = float(input(f"Harga barang ke-{i+1}: Rp"))
                
                # Validasi input harga (harus positif)
                if harga < 0:
                    print("Error: Harga tidak boleh negatif! Silakan masukkan kembali.")
                    continue
                
                # Tambahkan ke total harga
                total_harga += harga
                break
                
            except ValueError:
                print("Error: Input tidak valid! Masukkan angka.")
    
    return total_harga

def tampilkan_rincian_pembayaran(total_harga):
    """
    Fungsi untuk menampilkan rincian pembayaran dengan format yang baik.
    
    Args:
        total_harga (float): Total harga pembelian
    """
    print("\n===== RINCIAN PEMBAYARAN =====")
    print(f"Total Harga: Rp{total_harga:,.2f}".replace(",", "."))
    print("==============================")

def main():
    """
    Fungsi utama program kasir toko.
    """
    print("Selamat datang di Program Kasir Toko!")
    print("Program ini akan menghitung total harga dari 3 barang yang dibeli.")
    
    # Hitung total harga pembelian
    total_harga = hitung_total_pembelian()
    
    # Tampilkan rincian pembayaran
    tampilkan_rincian_pembayaran(total_harga)
    
    print("\nTerima kasih telah menggunakan Program Kasir Toko!")

# Jalankan program jika file dieksekusi langsung
if __name__ == "__main__":
    main()
