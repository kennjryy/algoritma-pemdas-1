def tampilkan_judul():
    """Menampilkan judul program."""
    print("STRUK PENGIRIMAN TOKO DARING")
    print("============================")

def biaya_berat(berat):
    """Menghitung biaya berdasarkan berat paket."""
    if berat <= 2:
        return 10000
    else:
        return 10000 + (berat - 2) * 4000

def biaya_jarak(jarak):
    """Menghitung biaya berdasarkan jarak pengiriman."""
    if jarak <= 20:
        return 0
    else:
        return 5000

def diskon(ongkir, anggota):
    """Menghitung diskon untuk pelanggan anggota."""
    if anggota == "Ya":
        return ongkir * 0.1
    else:
        return 0

def tampilkan_struk(nama, berat, jarak, anggota):
    """Menghitung dan menampilkan struk pengiriman."""
    biaya1 = biaya_berat(berat)
    biaya2 = biaya_jarak(jarak)

    ongkir = biaya1 + biaya2
    potongan = diskon(ongkir, anggota)
    total = ongkir - potongan

    print("\nNama pelanggan:", nama)
    print("Biaya berat: Rp", biaya1)
    print("Biaya jarak: Rp", biaya2)
    print("Diskon: Rp", potongan)
    print("Ongkir akhir: Rp", total)

    return total

def main():
    """Menjalankan program struk pengiriman."""
    tampilkan_judul()

    total_pendapatan = 0

    total_pendapatan = total_pendapatan + tampilkan_struk("Rina", 1, 10, "Bukan")
    total_pendapatan = total_pendapatan + tampilkan_struk("Sari", 5, 25, "Bukan")
    total_pendapatan = total_pendapatan + tampilkan_struk("Tono", 5, 25, "Ya")
    total_pendapatan = total_pendapatan + tampilkan_struk("Umar", 2, 30, "Ya")
    total_pendapatan = total_pendapatan + tampilkan_struk("Vina", 8, 15, "Bukan")

    print("\n============================")
    print("Total pendapatan: Rp", total_pendapatan)

if __name__ == "__main__":
    main()
