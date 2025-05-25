from num2words import num2words

b_tulov=3.00
har_km_uchun=1.20

m=float(input("Masofani kiriting (km):"))
print(m)

umumiy_tulov=b_tulov+har_km_uchun*m
print(umumiy_tulov)

yaxlitlash=round(umumiy_tulov,2)
print(yaxlitlash)

words_en=num2words(yaxlitlash)
words_ru=num2words(yaxlitlash,lang='ru')

print(f"${yaxlitlash:,.2f}")
print(words_en)
print(words_ru)