class Mahsulot:
    def __init__(self, nom: str, miqdor: int, narx: int):
        self.nom = nom          
        self.miqdor = miqdor     
        self.narx = narx           

    def narxni_qaytar(self, sotiladigan_soni: int) -> float:
        """Sotilayotgan mahsulotlar umumiy narxini hisoblaydi, chegirma bilan"""
        umumiy_narx = self.narx * sotiladigan_soni
        if 10 <= sotiladigan_soni < 100:
            umumiy_narx *= 0.9  # 10% chegirma
        elif sotiladigan_soni >= 100:
            umumiy_narx *= 0.8  # 20% chegirma
        return umumiy_narx

    def sotuvni_bajar(self, sotiladigan_soni: int):
       
        if sotiladigan_soni <= self.miqdor:
            self.miqdor -= sotiladigan_soni
        else:
            print("Yetarli mahsulot yo'q!")


def main():
    m1 = Mahsulot("Shokolad", 120, 10000)
    m2 = Mahsulot("Sharbat", 80, 15000)
    m3 = Mahsulot("Non", 200, 3000)

    mahsulotlar = [m1, m2, m3]

    for mahsulot in mahsulotlar:
        print(f"\nMahsulot: {mahsulot.nom}")
        try:
            soni = int(input(f"Nechta '{mahsulot.nom}' sotib olmoqchisiz? "))
        except ValueError:
            print("⚠️ Faqat butun son kiriting!")
            continue

        umumiy_narx = mahsulot.narxni_qaytar(soni)
        mahsulot.sotuvni_bajar(soni)

        print(f"📦 Mahsulot: {mahsulot.nom}")
        print(f"🧾 Sotilayotgan soni: {soni} dona")
        print(f"💰 Umumiy chegirmali narx: {int(umumiy_narx)} so‘m")
        print(f"📦 Omborda qolgan soni: {mahsulot.miqdor} dona")


if __name__ == "__main__":
    main()
