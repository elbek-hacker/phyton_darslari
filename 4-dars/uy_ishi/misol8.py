set1={"Artel","Alif","Yandex", "Google", "Meta"}
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

set4 = (set1.intersection(set2)).intersection(set3)
set1 = set1.difference(set4)
print("Umumiy elementlar: ", ", ".join(set4))
print("Faqat birinchi setda mavjud: ", ", ".join(set1))