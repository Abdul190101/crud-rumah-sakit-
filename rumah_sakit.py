from db import DBConnection as mydb
class Dokter:
    def __init__(self):
        self.__iddokter= None
        self.__nip= None
        self.__nama_lengkap= None
        self.__spesialis= None
        self.__tempat_praktek= None
        self.conn= None
        self.affected= None
        self.result= None
    @property
    def iddokter(self):
        return self.__iddokter
    
    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama_lengkap(self):
        return self.__nama_lengkap

    @nama_lengkap.setter
    def nama_lengkap(self, value):
        self.__nama_lengkap = value

    @property
    def spesialis(self):
        return self.__spesialis

    @spesialis.setter
    def spesialis(self, value):
        self.__spesialis = value

    @property
    def tempat_praktek(self):
        return self.__tempat_praktek

    @tempat_praktek.setter
    def tempat_praktek(self, value):
        self.__tempat_praktek = value

    def simpan(self):
        self.conn= mydb()
        val = (self.__nip,self.__nama_lengkap,self.__spesialis,self.__tempat_praktek)
        sql = "INSERT INTO dokter (nip,nama_lengkap,spesialis,tempat_praktek) VALUES" + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip,self.__nama_lengkap,self.__spesialis,self.__tempat_praktek, id)
        sql = "UPDATE dokter SET nip=%s nama_lengkap=%s, spesialis=%s, tempat_praktek=%s WHERE iddokter=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIP(self, nip):
        self.conn = mydb()
        val = (self.__nama_lengkap,self.__spesialis,self.__tempat_praktek, nip)
        sql = "UPDATE dokter SET nama_lengkap=%s, spesialis=%s, tempat_praktek=%s WHERE nip=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM dokter WHERE iddokter='"+ str(id) +"'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIP(self, nip):
        self.conn = mydb()
        sql = "DELETE FROM dokter WHERE nip='"+ str(nip) +"'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM dokter WHERE iddokter='"+ str(id) +"'"
        self.result = self.conn.findOne(sql)
        self.__nip = self.result[1]
        self.__nama_lengkap = self.result[2]
        self.__spesialis = self.result[3]
        self.__tempat_praktek = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIP(self, nip):
        a=str(nip)
        b=a.strip()
        self.conn = mydb()
        sql = "SELECT * FROM dokter WHERE nip='"+ b +"'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nip = self.result[1]
            self.__nama_lengkap = self.result[2]
            self.__spesialis = self.result[3]
            self.__tempat_praktek = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama_lengkap = ''
            self.__spesialis = ''
            self.__tempat_praktek = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM dokter"
        self.result = self.conn.findAll(sql)
        return self.result

dok = Dokter()

from db import DBConnection as mydb
class obat:
    def __init__(self):
        self.__idobat= None
        self.__kode_obat= None
        self.__nama_obat= None
        self.__bentuk= None
        self.__berat= None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idobat(self):
        return self.__idobat
    
    @property
    def kode_obat(self):
        return self.__kode_obat

    @kode_obat.setter
    def kode_obat(self, value):
        self.__kode_obat = value
    
    @property
    def nama_obat(self):
        return self.__nama_obat

    @nama_obat.setter
    def nama_obat(self, value):
        self.__nama_obat = value
    
    @property
    def bentuk(self):
        return self.__bentuk

    @bentuk.setter
    def bentuk(self, value):
        self.__bentuk = value
    
    @property
    def berat(self):
        return self.__berat

    @berat.setter
    def berat(self, value):
        self.__berat = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_obat,self.__nama_obat,self.__bentuk,self.__berat)
        sql="INSERT INTO obat (kode_obat,nama_obat,bentuk,berat) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_obat,self.__nama_obat,self.__bentuk,self.__berat, id)
        sql="UPDATE obat SET kode_obat=%s, nama_obat=%s, bentuk=%s, berat=%s WHERE idobat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateBykode_obat(self, kode_obat):
        self.conn = mydb()
        val = (self.__nama_obat,self.__bentuk,self.__berat, kode_obat)
        sql="UPDATE obat SET nama_obat=%s, bentuk=%s, berat=%s WHERE kode_obat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE idobat='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteBykode_obat(self, kode_obat):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE kode_obat='" + str(kode_obat) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE idobat='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__kode_obat = self.result[1]                   
        self.__nama_obat = self.result[2]                   
        self.__bentuk = self.result[3]                   
        self.__berat = self.result[4]                   
        self.conn.disconnect
        return self.result
        
    def getBykode_obat(self, kode_obat):
        a=str(kode_obat)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE kode_obat='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__kode_obat = self.result[1]
            self.__nama_obat = self.result[2]
            self.__bentuk = str(self.result[3])
            self.__berat = str(self.result[4])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kode_obat = ''                  
            self.__nama_obat = ''                  
            self.__bentuk = ''                  
            self.__berat = ''                  
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM obat"
        self.result = self.conn.findAll(sql)
        return self.result

mhs = obat() 

# Tampilkan semua data
'''result = mhs.getAllData()
print(result)'''

from db import DBConnection as mydb
class Pasien:
    def __init__(self):
        self.__idpasien= None
        self.__nomor_pasien= None
        self.__nama_lengkap= None
        self.__jenis_kelamin= None
        self.__umur= None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def idpasien(self):
        return self.__idpasien

    @property
    def nomor_pasien(self):
        return self.__nomor_pasien

    @nomor_pasien.setter
    def nomor_pasien(self, value):
        self.__nomor_pasien = value

    @property
    def nama_lengkap(self):
        return self.__nama_lengkap

    @nama_lengkap.setter
    def nama_lengkap(self, value):
        self.__nama_lengkap = value

    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin

    @jenis_kelamin.setter
    def jenis_kelamin(self, value):
        self.__jenis_kelamin = value

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        self.__umur = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nomor_pasien,self.__nama_lengkap,self.__jenis_kelamin,self.__umur)
        sql="INSERT INTO pasien (nomor_pasien,nama_lengkap,jenis_kelamin,umur) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nomor_pasien,self.__nama_lengkap,self.__jenis_kelamin,self.__umur, id)
        sql="UPDATE pasien SET nomor_pasien=%s, nama_lengkap=%s, jenis_kelamin=%s, umur=%s WHERE idpasien=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def updateByNIM(self, nomor_pasien):
        self.conn = mydb()
        val = (self.__nama_lengkap,self.__jenis_kelamin,self.__umur, nomor_pasien)
        sql="UPDATE pasien SET nama_lengkap=%s, jenis_kelamin=%s, umur=%s WHERE nomor_pasien=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM pasien WHERE idpasien='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def deleteByNIM(self, nomor_pasien):
        self.conn = mydb()
        sql="DELETE FROM pasien WHERE nomor_pasien='" + str(nomor_pasien) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM pasien WHERE idpasien='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nomor_pasien = self.result[1]
        self.__nama_lengkap = self.result[2]
        self.__jenis_kelamin = self.result[3]
        self.__umur = self.result[4]
        self.conn.disconnect
        return self.result

    def getByNIM(self, nomor_pasien):
        a=str(nomor_pasien)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM pasien WHERE nomor_pasien='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nomor_pasien = self.result[1]
            self.__nama_lengkap = self.result[2]
            self.__jenis_kelamin = self.result[3]
            self.__umur = str(self.result[4])
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nomor_pasien = ''
            self.__nama_lengkap = ''
            self.__jenis_kelamin = ''
            self.__umur = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pasien"
        self.result = self.conn.findAll(sql)
        return self.result

psn = Pasien()

# Tampilkan semua data
'''result = psn.getAllData()
print(result)'''

# Entri data
'''psn.nomor_pasien = '1'
psn.nama_lengkap = 'WIDIA'
psn.jenis_kelamin = P
psn.umur=20
hasil = psn.simpan()
print(hasil)'''

# Cari data
'''nomor_pasien = '1'
hasil = psn.getByNIM(nim)
print(hasil)'''

# Update Data
'''nim = '1'
psn.nama_lengkap = 'Angel'
psn.jenis_kelamin=P
psn.umur=19
hasil = psn.updateByNIM(nomor_pasien)
print(hasil)'''

# delete data
'''nomor_pasien = '1'
hasil = psn.deleteByNIM(nomor_pasien)
print(hasil)'''
