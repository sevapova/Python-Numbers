
from num2words import num2words

b_tulov=5.00
h_km_u=0.80

m=float(input("Masofani kiriting (km):"))
u_narx=b_tulov+m+h_km_u

words_en=num2words(u_narx)
words_ru=num2words(u_narx,lang='ru')

print((f"${u_narx:,.2f}"))
print(words_en)
print(words_ru)


