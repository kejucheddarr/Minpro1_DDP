list_semua = [
    ["Endometril", "Tablet", "Bebas Terbatas"],
    ["Gastran", "Tablet", "Bebas"],
    ["Salbutamol", "Cair", "Keras"],
    ["Morfin", "Analgesik", "Narkotika"]
]
list_obat = ("Endometril", "Gastran", "Salbutamol", "Morfin")
list_golongan = ("Bebas", "Bebas Terbatas", "Keras", "Narkotika")
list_bentuk = ("Tablet", "Cair", "Analgesik")
laporan_bulan = [
    ["Nama Obat: Endometril", "Stok Awal: 80", "Keluar: 70", "Masuk: 32", "Stok Akhir: 42"],
    ["Nama Obat: Gastran", "Stok Awal: 65", "Keluar: 50", "Masuk: 21", "Stok Akhir: 36"],
    ["Nama Obat: Salbutamol", "Stok Awal: 70", "Keluar: 54", "Masuk: 42", "Stok Akhir: 58"],
    ["Nama Obat: Morfin", "Stok Awal: 93", "Keluar: 78", "Masuk: 45", "Stok Akhir: 60"]
]

print("Pendataan Obat di Rumah Sakit")

print("[1] Input Data Obat")
print("[2] Cari Obat")
print("[3] Cetak/Export Laporan")

opsi=int(input("Pilih Opsi 1-3 : "))

#Input_Obat
if opsi == 1:
    list_semua.append(input("Nama Obat, Bentuk sediaan, Golongan Obat: "))
    for element in list_semua:
        print(element)

#Cari_Obat
if opsi == 2:
    search_filter = input("Search atau Filter? : ")

    if search_filter == "Search":
        cari_obat = input("Ingin mencari obat apa? : ")
        if cari_obat in list_obat:
            print(f"{cari_obat}: Obat Tersedia")
            if cari_obat in ["Endometril"]:
                print("Bentuk sediaan: Obat Tablet")
                print("Golongan: Obat Bebas Terbatas")
                print("End")
            elif cari_obat in ["Gastran"]:
                print("Bentuk sediaan: Obat Tablet")
                print("Golongan: Obat Bebas")
                print("End")
            elif cari_obat in ["Salbutamol"]:
                print("Bentuk sediaan: Obat Cair")
                print("Golongan: Obat Keras")
                print("End")
            elif cari_obat in ["Morfin"]:
                print("Bentuk sediaan: Obat Analgesik")
                print("Golongan: Obat Narkotika")
                print("End")
        else:
            print("Obat Tidak Tersedia")
            print("End")
    elif search_filter == "Filter":
        golongan_bentuk = input("Golongan atau Bentuk sediaan obat? : ")
        if golongan_bentuk == "Golongan":
            cari_golongan = input("Ingin mencari golongan obat apa? : ")
            if cari_golongan in list_golongan:
                print(f"{cari_golongan}: Golongan Obat Tersedia")
                if cari_golongan in ["Bebas"]:
                    print("Gastran")
                    print("End")
                elif cari_golongan in ["Bebas Terbatas"]:
                    print("Endometril")
                    print("End")
                elif cari_golongan in ["Keras"]:
                    print("Salbutamol")
                    print("End")
                elif cari_golongan in ["Narkotika"]:
                    print("Morfin")
                    print("End")
            else:
                print("Golongan Obat Tidak Tersedia")
                print("End")
        elif golongan_bentuk == "Bentuk":
            cari_bentuk = input("Ingin mencari bentuk obat apa? : ")
            if cari_bentuk in list_bentuk:
                print(f"{cari_bentuk}: Bentuk Obat Tersedia")
                if cari_bentuk in ["Tablet"]:
                    print("Endometril", "Gastran", sep=", ")
                    print("End")
                if cari_bentuk in ["Cair"]:
                    print("Sabutamol")
                    print("End")
                if cari_bentuk in ["Analgesik"]:
                    print("Morfin")
                    print("End")
            else:
                print("Bentuk Obat Tidak Tersedia")
                print("End")
        else:
            print("End")
    else:
        print("End")

#Update_Stock 
elif opsi == 3:
    export_laporan = input("Cetak/Export laporan masuk/keluar obat bulan ini?: ( Ya / Tidak ) ")
    if export_laporan == "Ya":
        print(laporan_bulan)
        print("End")
    else:
        print("End")

else:
    print("End")
