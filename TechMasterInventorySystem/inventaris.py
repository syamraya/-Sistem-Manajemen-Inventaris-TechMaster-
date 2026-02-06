from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = 0

    @property
    def stok(self):
        return self.__stok

    @property
    def harga_dasar(self):
        return self.__harga_dasar

    def tambah_stok(self, jumlah):
        if jumlah >= 0:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")
            return True
        else:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor
        self.pajak_rate = 0.10

    def tampilkan_detail(self):
        pajak_per_unit = self.harga_dasar * self.pajak_rate
        return f"[LAPTOP] {self.nama} | Proc: {self.processor}\n   Harga Dasar: Rp {self.harga_dasar:,} | Pajak(10%): Rp {pajak_per_unit:,}"

    def hitung_harga_total(self, jumlah):
        pajak = self.harga_dasar * self.pajak_rate
        return (self.harga_dasar + pajak) * jumlah

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera
        self.pajak_rate = 0.05 

    def tampilkan_detail(self):
        pajak_per_unit = self.harga_dasar * self.pajak_rate
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}\n   Harga Dasar: Rp {self.harga_dasar:,} | Pajak(5%): Rp {pajak_per_unit:,}"

    def hitung_harga_total(self, jumlah):
        pajak = self.harga_dasar * self.pajak_rate
        return (self.harga_dasar + pajak) * jumlah

def proses_transaksi(daftar_belanja):
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    for i, item in enumerate(daftar_belanja, 1):
        barang = item['produk']
        qty = item['qty']
        
        subtotal = barang.hitung_harga_total(qty)
        total_tagihan += subtotal
        
        print(f"{i}. {barang.tampilkan_detail()}")
        print(f"   Beli: {qty} unit | Subtotal: Rp {subtotal:,}")
    
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,}")
    print("-" * 40)


print("--- SETUP DATA ---")
laptop_rog = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
hp_iphone = Smartphone("iPhone 13", 15000000, "12MP")

laptop_rog.tambah_stok(10)
hp_iphone.tambah_stok(-5)
hp_iphone.tambah_stok(20)

keranjang = [
    {"produk": laptop_rog, "qty": 2},
    {"produk": hp_iphone, "qty": 1}
]

proses_transaksi(keranjang)