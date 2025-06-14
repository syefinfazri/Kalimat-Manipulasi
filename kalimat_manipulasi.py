# Function untuk mereverse setiap kata dalam kalimat
def reverse_per_kata(kalimat):
    """
    Membalik setiap kata dalam kalimat, tanpa mengubah urutan kata.
    Contoh: "AKU CINTA KAMU" -> "UKA ATNIC UMAK"
    """
    # Pisahkan kalimat menjadi list kata
    kata_list = kalimat.split()
    # Balik setiap kata dengan slicing [::-1]
    kata_balik = []
    for kata in kata_list:
        kata_balik.append(kata[::-1])
    # Gabungkan kembali kata yang sudah dibalik
    kalimat_baru = ' '.join(kata_balik)
    return kalimat_baru


# Function untuk mengurutkan kata dalam kalimat sesuai list urutan
def urutkan_kalimat(kalimat, urutan):
    """
    Mengurutkan kata dalam kalimat sesuai list urutan (posisi mulai dari 1).
    Contoh: "HARI INI SEDANG BELAJAR PYTHON" + [5,1,4,3,2]
    Output: "PYTHON HARI BELAJAR SEDANG INI"
    """
    # Pisahkan kalimat menjadi list kata
    kata_list = kalimat.split()
    # Buat list baru berdasarkan urutan
    kata_urut = []
    for i in urutan:
        kata_urut.append(kata_list[i - 1])  # karena urutan mulai dari 1
    # Gabungkan kembali menjadi string
    kalimat_baru = ' '.join(kata_urut)
    return kalimat_baru


# Function untuk mengganti huruf vokal dengan simbol tertentu
def ganti_vokal(kalimat, opsi):
    """
    Mengganti huruf vokal dengan simbol.
    opsi = 1 -> huruf vokal kecil saja.
    opsi = 2 -> huruf vokal kapital saja.
    """
    # Buat dictionary untuk mapping penggantian
    mapping_kecil = {'a': '4', 'i': '1', 'u': '|_|', 'e': '3', 'o': '0'}
    mapping_besar = {'A': '4', 'I': '1', 'U': '|_|', 'E': '3', 'O': '0'}
    hasil = ''
    # Iterasi setiap huruf di kalimat
    for huruf in kalimat:
        if opsi == 1:
            if huruf in mapping_kecil:
                hasil += mapping_kecil[huruf]
            else:
                hasil += huruf
        elif opsi == 2:
            if huruf in mapping_besar:
                hasil += mapping_besar[huruf]
            else:
                hasil += huruf
    return hasil

print(reverse_per_kata("AKU CINTA INDONESIA"))
#Output Seharusnya: UKA ATNIC AISENODNI

print(urutkan_kalimat("HARI INI SEDANG BELAJAR DASAR PEMROGRAMAN BERSAMA", [5, 1, 4, 6, 2, 7, 3]))
#Output Seharusnya: DASAR HARI BELAJAR PEMROGRAMAN INI BERSAMA SEDANG

print(ganti_vokal("Aku Cinta Indonesia", 1))
#Output Seharusnya: Ak|_| C1nt4 Ind0n3s14

print(ganti_vokal("Aku Cinta Indonesia", 2))
#Output Seharusnya: 4ku Cinta 1ndonesia
