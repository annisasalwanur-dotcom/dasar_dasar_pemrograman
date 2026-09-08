batas_nilai = (65, 100)  
nilai_masuk = []
lulus = []
remedi = []

print("SYSTEM PENGELOMPOKAN NILAI UJIAN MAHASISWA")
print(f"batas nilai lulus: {batas_nilai[0]} (maksimal: {batas_nilai[1]})\n")

while True:
    input_user = input("masukkan nilai ujian (ketik 'selesai' untuk berhenti): ")
    
    if input_user.lower() == 'selesai':
        
        if len(nilai_masuk) < 5:
            print(f"harus menginput minimal 5 nilai! (Saat ini: {len(nilai_masuk)} nilai)\n")
            continue
        
        lulus = (n >= batas_nilai[0] for n in nilai_masuk)
        remedi = (n < batas_nilai[0] for n in nilai_masuk)
        
        if not (lulus and remedi):
            print("input harus minimal satu nilai lulus dan satu nilai remedi!\n")
            continue
        
        break
    
        nilai = float(input_user)
        if 0 <= nilai <= batas_nilai[1]:
            nilai_masuk.append(nilai)
            print(f"-> nilai {nilai} berhasil ditambahkan")
        else:
            print(f"nilai harus berada dalam rentang 0 - {batas_nilai[1]}")
        print("masukkan angka yang valid atau ketik 'selesai'")

for n in nilai_masuk:
    if n >= batas_nilai[0]:
        lulus.append(n)
    else:
        remedi.append(n)

print("daftar nilai saat ini:", nilai_masuk)
pilihan_hapus = input("apakah ada nilai yang salah input dan ingin dihapus? (y/n): ")

if pilihan_hapus == 'y':
    while True:
            nilai_hapus = float(input("Masukkan nilai yang ingin dihapus: "))
            if nilai_hapus in nilai_masuk:
                nilai_masuk.remove(nilai_hapus)
                if nilai_hapus in lulus:
                    lulus.remove(nilai_hapus)
                elif nilai_hapus in remedi:
                    remedi.remove(nilai_hapus)
                
                print(f"-> nilai {nilai_hapus} berhasil dihapus")
                break
            else:
                print("nilai tersebut tidak ada dalam daftar nilai masuk")

print("HASIL AKHIR")
print("semua nilai masuk :", nilai_masuk)
print("list nilai lulus :", lulus)
print("daftar nilai remedi:", remedi)