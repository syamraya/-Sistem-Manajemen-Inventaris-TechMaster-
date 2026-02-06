# 🖥️ TechMaster Inventory System

Sistem Manajemen Inventaris backend sederhana berbasis **Python OOP** untuk toko elektronik **TechMaster**.  
Proyek ini dibuat untuk memenuhi **Tugas Proyek Integrasi OOP (Advanced)** dengan penerapan **4 Pilar OOP**.

---

## 📸 Screenshot Program

> Screenshot berikut menampilkan hasil eksekusi program (setup data & transaksi).

![Screenshot Output Program](screenshot.png)

---

## 📌 Deskripsi Proyek

TechMaster adalah toko elektronik yang menjual barang bernilai tinggi seperti **Laptop** dan **Smartphone**.  
Sistem ini dibuat untuk:

- Mengelola stok barang secara aman
- Melindungi harga dan stok dari perubahan sembarangan
- Menghitung pajak berbeda untuk tiap jenis barang
- Menangani transaksi dengan berbagai tipe objek

---

## 🎯 Tujuan Pembelajaran

- Menggunakan **Abstract Class & Abstract Method**
- Menerapkan **Encapsulation** pada data sensitif
- Membangun **Inheritance** antar class
- Mengimplementasikan **Polymorphism** dalam transaksi

---

## 🧱 Konsep OOP yang Digunakan

### 1️⃣ Abstraction
- Abstract Class: `BarangElektronik`
- Tidak bisa diinstansiasi langsung
- Abstract Method:
  - `tampilkan_detail()`
  - `hitung_harga_total(jumlah)`

### 2️⃣ Encapsulation
- Atribut private:
  - `__stok`
  - `__harga_dasar`
- Akses stok menggunakan **getter**
- Perubahan stok melalui method dengan validasi

### 3️⃣ Inheritance
- `Laptop` dan `Smartphone` mewarisi `BarangElektronik`
- Memiliki atribut dan pajak berbeda

### 4️⃣ Polymorphism
- Method yang sama, perilaku berbeda
- Fungsi transaksi menerima campuran objek tanpa cek tipe

---

## 🧪 Alur Program (User Story)

1. Admin membuat 1 Laptop dan 1 Smartphone
2. Admin mencoba menambah stok negatif → **ditolak**
3. Admin menambah stok valid
4. User membeli:
   - 2 Laptop
   - 1 Smartphone
5. Sistem menampilkan detail dan total transaksi

---

## 🖨️ Contoh Output Program

