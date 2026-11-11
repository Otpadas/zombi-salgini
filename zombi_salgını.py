giris_kod = str(input("Giriş kodunuzu giriniz: (Örnek: SGNK-TR-41)")).upper().split("-")

if len(giris_kod) != 3:
    print("Hatalı giriş yaptınız.")
    exit()

if giris_kod[2] != "54":
    print("Sadece 54. bölgeden insanlar girebilir.")
    exit()

isi = float(input("Vücut ısınızı giriniz:"))

if isi > 38.5:
    print("Yüksek ateş. Enfeksiyon riski!")
    exit()
elif isi < 30:
    print("Normal koşullarda hipotermi geçirmeniz gerek. Enfeksiyon riski!")
    exit()

sinif = str(input("Sınıfınızı giriniz: (Sıhhiye/Yağmacı/Asker)")).upper()

budget = 2000

print(f"Toplam bütçeniz {budget} mermi.")

if sinif in ["ASKER", "YAĞMACI"]:
    silah = str(input("Silahını seçin. (Tabanca-300/Tüfek-700/Ağır Makineli-1200)")).upper()
    if silah == "TABANCA":
        budget -= 300
    elif silah == "TÜFEK":
        budget -= 700
    elif silah == "AĞIR MAKINELI":
        budget -= 1200
    else:
        print("Bir hata oluştu")
        exit()
elif sinif == "SIHHİYE":
    silah = str(input("Silahını seçin. (Tabanca-300/Tüfek-700)")).upper()
    if silah == "TABANCA":
        budget -= 300
    elif silah == "TÜFEK":
        budget -= 700
    else:
        print("Hatalı giriş yaptınız.")
        exit()
else:
    print("Hatalı giriş.")
    exit()

print(f"Toplam bütçeniz {budget} mermi.")

isirik = str(input("Vücüdunuzda herhangi bir ısırk var mı? (Evet/Hayır)")).lower()

if isirik == "evet":
    panzehir = str(input("Panzehir ister misin? 1000 Mermi (Evet/Hayır)")).lower()
    if panzehir == "evet":
        budget -= 1000
        if budget >= 0:
            print("Panzehir uygulandı.")
            print(f"Toplam bütçeniz {budget} mermi.")
        else:
            print("Yeterli bakiye yok.")
            if silah == "AĞIR MAKINELI":
                silah = str(input("Silahını tabanca ve ya tüfeğe çevirip bakiye arttımanız lazım.\nAlmak istediğiniz silahı söyleyin: (Tabanca/Tüfek)")).upper()
                if silah == "TABANCA":
                    budget += 900
                    print("Panzehir uygulandı.")
                elif silah == "TÜFEK":
                    budget += 500
                    print("Panzehir uygulandı.")
                else:
                    print("Karantinaya alındız.")
                    exit()
    elif panzehir == "hayır":
        print("Karantinaya alındınız.")
        exit()
    else:
        print("Hatalı giriş.")
        exit()
elif isirik not in ["evet", "hayır"]:
    print("Hatalı giriş yaptınız.")
    exit()

if silah != "AĞIR MAKINELI":
    print("-" * 36)
    print(f"\nBölge:\t{giris_kod[1].upper()}\nSınıf:\t\t\t{sinif}\nSilah:\t\t\t{silah}\nKalan Mermi:\t\t{budget}\n\nSığınağa hoşgeldiniz.")
    print("-"*36)
else:
    print("-" * 36)
    print(f"\nBölge:\t{giris_kod[1].upper()}\nSınıf:\t\t\t{sinif}\nSilah:\t\t\tAĞIR MAKİNELİ\nKalan Mermi:\t\t{budget}\n\nSığınağa hoşgeldiniz.")
    print("-"*36)

