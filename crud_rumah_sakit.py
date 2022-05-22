from dokter import Dokter
from obat import obat
from pasien import Pasien

def Tampil():
    print("\nData Dokter yang di tampilkan sebagai berikut:")
    dok = Dokter()
    result = dok.getAllData()
    for x in result:
        print(x)
    print("\nData Obat yang di tampilkan sebagai berikut:")
    obt = obat()
    result = obt.getAllData()
    for x in result:
        print(x)
    print("\nData Pasien yang di tampilkan sebagai berikut:")
    psn = Pasien()
    result = psn.getAllData()
    for x in result:
        print(x)
    MenuRumahsakit()

def Entry():
    dok = Dokter()
    nip = input("Masukan NIP DOKTER :")
    nama_lengkap = input("Masukan Nama Lengkap:")
    sp = input("Masukan Spesialis:")
    tp = input("Masukan Tempat Praktek:")
    dok.nip=nip
    dok.nama_lengkap=nama_lengkap
    dok.spesialis=sp
    dok.tempat_praktek=tp
    hasil = dok.simpan()
    if(hasil==1):
        print("Entry data berhasil\n")
    else:
        print("Enty data gagal.\n")

    obt = obat()
    kode_obat = input("Masukan kode obat :")
    nama_obat = input("Masukan nama obat :")
    bentuk = input("Masukan bentuk :")
    berat = input("Masukan berat :")
    obt.kode_obat=kode_obat
    obt.nama_obat=nama_obat
    obt.bentuk=bentuk
    obt.berat=berat
    hasil = obt.simpan()
    if(hasil==1):
        print("Entry data berhasil\n")
    else:
        print("Enty data gagal.\n")

    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien: ")
    nama_lengkap = input("Masukkan nama lengkap pasien: ")
    jenis_kelamin = input("Masukkan jenis kelamin pasien: ")
    umur = input("Masukkan umur pasien: ")
    psn.nomor_pasien = nomor_pasien
    psn.nama_lengkap = nama_lengkap
    psn.jenis_kelamin = jenis_kelamin
    psn.umur = umur
    hasil = psn.simpan()
    if (hasil==1):
        print("Entry Data Berhasil!\n")
    else:
        print("Entry Data Gagal...\n")
    MenuRumahsakit()

def Cari():
    dok = Dokter()
    nip = input("Masukan NIP DOKTER yang di cari:")
    hasil = dok.getByNIP(nip)
    print(hasil)
    print("\nData Dokter yang di tampilkan sebagai berikut:\n")

    obt = obat()
    kode_obat = input("Masukan kode obat yang di cari :")
    hasil = obt.getBykode_obat(kode_obat)
    print(hasil)
    print("\nData Obat yang di tampilkan sebagai berikut:\n")

    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien yang Dicari: ")
    hasil = psn.getByNIM(nomor_pasien)
    print(hasil)
    print("\nData Pasien yang di tampilkan sebagai berikut:\n")
    MenuRumahsakit()

def Ubah():
    dok = Dokter()
    nip = input("Masukan NIP yang akan di ubah:")
    hasil = dok.getByNIP(nip)
    print("Data yang di temukan sebagai berikut:")
    print(hasil)
    print("Silakan lengkapi data berikut untuk mengganti:")
    nama_lengkap = input("Masukan Nama Dokter:")
    sp = input("Masukan Spesialis:")
    tp = input("Masukan Tempat Praktek:")
    dok.nip=nip
    dok.nama_lengkap=nama_lengkap
    dok.spesialis=sp
    dok.tempat_praktek=tp
    hasil = dok.updateByNIP(nip)
    if(hasil==1):
        print("Data berhasil di ubah.\n")
    else:
        print("Data gagal di ubah.\n")

    obt = obat()
    kode_obat = input("Masukan kode obat yang akan di ubah :")
    hasil = obt.getBykode_obat(kode_obat)
    print("Data yang di temukan sebagai berikut :")
    print(hasil)
    print("Silakan lengkapi data berikut untuk mengganti :")
    nama_obat = input("Masukan nama obat :")
    bentuk = input("Masukan bentuk :")
    berat = input("Masukan berat :")
    obt.kode_obat=kode_obat
    obt.nama_obat=nama_obat
    obt.bentuk=bentuk
    obt.berat=berat
    hasil = obt.updateBykode_obat(kode_obat)
    if(hasil==1):
        print("Data berhasil di ubah.\n")
    else:
        print("Data gagal di ubah.\n")

    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien yang Akan Diubah: ")
    hasil = psn.getByNIM(nomor_pasien)
    print("Data yang Ditemukan Sebagai Berikut:")
    print(hasil)
    print("Silahkan Lengkapi Data Berikut Untuk Mengganti:")
    nama_lengkap = input("Masukkan nama lengkap pasien: ")
    jenis_kelamin = input("Masukkan jenis kelamin pasien: ")
    umur = input("Masukkan umur pasien : ")
    psn.nomor_pasien = nomor_pasien
    psn.nama_lengkap = nama_lengkap
    psn.jenis_kelamin = jenis_kelamin
    psn.umur = int(umur)
    hasil = psn.updateByNIM(nomor_pasien)
    if(hasil==1):
        print("Data Berhasil Diubah!\n")
    else:
        print("Data Gagal Diubah...\n")
    MenuRumahsakit()
    
def Hapus():
    dok = Dokter()
    nip = input("Masukan NIP yang akan dihapus:")
    hasil = dok.getByNIP(nip)
    print("Data yang ditemukan sebagai berikut:")
    print(hasil)
    jawab = input("Apakah data ini akan di hapus (y/t) ?")
    if(jawab=="y"):
        hasil = dok.deleteByNIP(nip)
        if(hasil==1):
            print("Data berhasil di hapus.\n")
        else:
            print("Data gagal di hapus.\n")
    else:
        print("Data batal untuk di hapus.\n")

    obt = obat()
    kode_obat = input("Masukan kode obat yang akan dihapus :")
    hasil = obt.getBykode_obat(kode_obat)
    print("Data yang ditemukan sebagai berikut :")
    print(hasil)
    jawab = input("Apakah data ini akan di hapus (y/t) ? : ")
    if(jawab=="y"):
        hasil = obt.deleteBykode_obat(kode_obat)
        if(hasil==1):
            print("Data berhasil di hapus.\n")
        else:
            print("Data gagal di hapus.\n")
    else:
        print("Data batal untuk di hapus.\n")

    psn = Pasien()
    nomor_pasien = input("Masukkan nomor pasien yang Akan Dihapus: ")
    hasil = psn.getByNIM(nomor_pasien)
    print("Data yang Ditemukan Sebagai Berikut:")
    print(hasil)
    jawab = input("Apakah Data Ini Akan Dihapus (y/t)?:")
    if(jawab=="y"):
        hasil = psn.deleteByNIM(nomor_pasien)
        if(hasil==1):
            print("Data Berhasil Dihapus!\n")
        else:
            print("Data Gagal Dihapus...\n")
    else:
        print("Data Batal Untuk Dihapus.\n")
    MenuRumahsakit()
        
def MenuRumahsakit():
    lanjut = True
    while lanjut:
        print("\n\nKELOLA DATA RUMAH SAKIT\nOleh: RM. MEDIKA CENTER MAJALAYA\nMenu:\n1.LIHAT DATA RUMAH SAKIT\n2.CARI DATA RUMAH SAKIT\n3.TAMBAH DATA RUMAH SAKIT\n4.UBAH DATA RUMAH SAKIT\n5.HAPUS DATA RUMAH SAKIT\n6.KELUAR")
        p = int(input("PILIH MENU :"))
        if(p==1):
            Tampil()
        elif(p==2):
            Cari()
        elif(p==3):
            Entry()
        elif(p==4):
            Ubah()
        elif(p==5):
            Hapus()
        elif(p==6):
            lanjut = False
            break
        else:
            lanjut = False
            break
MenuRumahsakit()
