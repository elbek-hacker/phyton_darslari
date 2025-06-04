
tekshir = lambda a: a.lstrip('-').replace('.', '', 1).isdigit()
a = "-0.202"

print(tekshir(a))