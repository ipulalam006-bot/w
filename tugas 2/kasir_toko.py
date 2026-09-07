def hitung_subtotal(daftar_harga):
    """
    Menghitung total harga sebelum diskon.

    Parameter:
        daftar_harga (list): Daftar harga barang dalam bentuk list numerik.

    Return:
        float atau int: Total harga dari semua barang dalam daftar.
    """
    total = 0
    for harga in daftar_harga:
        total += harga
    return total


def hitung_diskon(total, persentase_diskon=0):
    """
    Menghitung nominal potongan harga berdasarkan persentase diskon.

    Parameter:
        total (float atau int): Total belanja sebelum diskon.
        persentase_diskon (float atau int, opsional): Persentase diskon dalam % (default 0).

    Return:
        float: Nominal uang yang didiskonkan.
    """
    return total * (persentase_diskon / 100)


def hitung_pajak(total_setelah_diskon, tarif_pajak=0.11):
    """
    Menghitung nominal PPN (Pajak Pertambahan Nilai).

    Parameter:
        total_setelah_diskon (float atau int): Harga bersih setelah dikurangi diskon.
        tarif_pajak (float, opsional): Tarif pajak dalam desimal (default 0.11 = 11%).

    Return:
        float: Nominal pajak yang harus dibayar.
    """
    return total_setelah_diskon * tarif_pajak


def cetak_struk(nama_pelanggan, daftar_barang, persentase_diskon=0):
    """
    Mencetak struk belanjaan yang rapi ke terminal.

    Memanggil fungsi hitung_subtotal, hitung_diskon, dan hitung_pajak
    untuk menghitung seluruh komponen harga, kemudian mencetak struk
    dengan format yang mudah dibaca.

    Parameter:
        nama_pelanggan (str): Nama pelanggan yang berbelanja.
        daftar_barang (list): List berisi tuple (nama_barang, harga_barang).
        persentase_diskon (float atau int, opsional): Persentase diskon dalam % (default 0).
    """
    daftar_harga = [harga for (nama, harga) in daftar_barang]
    subtotal = hitung_subtotal(daftar_harga)
    diskon = hitung_diskon(subtotal, persentase_diskon)
    total_setelah_diskon = subtotal - diskon
    pajak = hitung_pajak(total_setelah_diskon)
    total_akhir = total_setelah_diskon + pajak

    print("=" * 50)
    print(f"{'TOKO SEMBAKO MAKMUR':^50}")
    print("=" * 50)
    print(f"Pelanggan: {nama_pelanggan}")
    print(f"Tanggal   : (dummy date)")
    print("-" * 50)
    print(f"{'Barang':<30} {'Harga':>10}")
    print("-" * 50)
    for (nama, harga) in daftar_barang:
        print(f"{nama:<30} Rp{harga:>9,.0f}")
    print("-" * 50)
    print(f"{'Subtotal':<30} Rp{subtotal:>9,.0f}")
    if persentase_diskon > 0:
        print(f"{'Diskon (' + str(persentase_diskon) + '%)':<30} -Rp{diskon:>8,.0f}")
    print(f"{'Total setelah diskon':<30} Rp{total_setelah_diskon:>9,.0f}")
    print(f"{'PPN (11%)':<30} Rp{pajak:>9,.0f}")
    print("=" * 50)
    print(f"{'TOTAL BAYAR':<30} Rp{total_akhir:>9,.0f}")
    print("=" * 50)
    print(f"{'Terima kasih atas kunjungan Anda!':^50}")
    print("=" * 50)
    print()


if __name__ == "__main__":
    # Skenario 1: Belanja tanpa diskon
    print("SKENARIO 1: BELANJA TANPA DISKON")
    pelanggan1 = "Budi Santoso"
    belanjaan1 = [
        ("Beras 5kg", 65000),
        ("Minyak Goreng 2L", 32000),
        ("Gula Pasir 1kg", 14000),
        ("Telur Ayam 1kg", 28000),
        ("Kecap Manis", 12000)
    ]
    cetak_struk(pelanggan1, belanjaan1)

    # Skenario 2: Belanja dengan diskon 15%
    print("SKENARIO 2: BELANJA DENGAN DISKON 15%")
    pelanggan2 = "Siti Rahayu"
    belanjaan2 = [
        ("Sabun Mandi 3pcs", 25000),
        ("Pasta Gigi 2pcs", 18000),
        ("Shampoo 750ml", 45000),
        ("Detergen Bubuk 2kg", 55000),
        ("Pembersih Lantai", 22000),
        ("Tisu Roll 10pcs", 30000)
    ]
    cetak_struk(pelanggan2, belanjaan2, persentase_diskon=15)
