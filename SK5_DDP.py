def biaya_parkir(jenis_kendaraan, durasi):

    if jenis_kendaraan == "mobil":
        tarif = 5000
    else:
        tarif = 3000

    total = tarif*durasi
    return total

jenis = input("Jenis kendaraan mobil/motor: ")
jam_masuk = int(input("Jam masuk: "))
jam_keluar = int(input("Jam keluar: "))

durasi_parkir = jam_keluar - jam_masuk

total_biaya = biaya_parkir(jenis, durasi_parkir)

print("Lama parkir: ", durasi_parkir)
print("Total biaya parkir: Rp", total_biaya)
