from num2words import num2words
narx_kwh=0.45

a=float(input("$Oyning boshidagi ko'rsatkichni kiriting ($): "))
b=float(input("$Oyning oxiridagi ko'rsatkichni kiriting ($): "))

c=b-a
x=round(c*narx_kwh,2)

words_en=num2words(x)
words_ru=num2words(x,lang='ru')

print((f"${x:,.2f}"))
print(words_en)
print(words_ru)
