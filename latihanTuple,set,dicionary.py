#membuat data tuple
print("Nomor 1")
print("a. Membuat data tuple")
mahasiswa = ("Nama", "Nim", "Prodi")

print(f"b. Menampilkan nim dan prodi :{mahasiswa[1]}, {mahasiswa[2]}")

print("c. Menjalankan data mahasiswa index 2")
print("Terjadi error, karena tuple bersifat immutable atau data yang ada di dalamnya tidak bisa diubah atau ditimpa langsung lewat index")
print("d. Membuat set")
data_set = {10, 4, 3, 2, 4, 10, 7, 5}
print(f"nilai dataSet = {data_set}")
print("ini terjadi karena pada data set tidak boleh ada nilai ganda, jika terjadi nilai ganda nilai yang ditulis hanya sample nilai tersebut")

print("\nNomor 2")
print("a. Membuat dictionary :")
data_mahasiswa = {
    "nim"  : "240101",
    "nama" : "Budi Santoso",
    "prodi" : "teknologi informasi"

}
print(data_mahasiswa)

print("b. Mengubah nilai prodi dan mahasiswa")
data_mahasiswa["prodi"] = "sastra mesin"
data_mahasiswa["angkatan"] = 2026
print(data_mahasiswa)

print("c. Menghapus key nim ")
del data_mahasiswa["nim"]
print(data_mahasiswa)

#perulangan pada dictionary
print("\nNomor 3")
print("a. Membuat dictionary keranjang")
keranjang = {
    "apel" : 5000,
    "pisang" : 3000,
    "jeruk" : 7000,
    "anggur" : 15000

}
print(keranjang)
print("b. Membuat perulangan untuk menampilkan setiap barang beserta harganya , dan c. menampilkan total belanja")
total = 0
for buah, value in keranjang.items() :
    print(f"harga {buah} = {value}")
    total += value

print(f"harga total = {total}")






