with open("arabcha.txt", "w", encoding="utf-8") as file:
    file.write(" مرحباً، أنا طالب في تعليم الخلاص.")

with open("arabcha.txt", "r", encoding="utf-8") as file:
    arabcha_matn = file.read().strip()

if arabcha_matn == "مرحباً، أنا طالب في تعليم الخلاص.":
    tarjima = "Salom, men Najot Ta'lim o'quvchisiman."
else:
    tarjima = "Tarjima topilmadi."

with open("tarjimasi.txt", "w", encoding="utf-8") as file:
    file.write(f"{tarjima}.")