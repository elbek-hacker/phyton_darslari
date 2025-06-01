
ortachasi = lambda tpl: sum(tpl) // len(tpl) if len(tpl) > 0 else 0

tpl = tuple([1,2,3,4,5])
print(ortachasi(tpl))
