'''1. cash_denomination_splitter.py – Kupyuraga ajratish (pulni kupyuralarga ajratish)'''

from num2words import num2words

pul=int(input("Pul miqdorini kiriting ($):"))
words_en=num2words(pul)
words_ru=num2words(pul,lang='ru')

x_50 = pul//50
pul=pul%50
print("%50 kupyuradan:",x_50,"ta")

x_10=pul//10
pul=pul%10
print("$10 kupyuradan:",x_10,"ta")

x_5=pul//5
pul=pul%5
print("$5 kupyuradan:",x_5,"ta")

x_1=pul//1
pul=pul%1
print("$1 kupyuradan:",x_1,"ta")

print(f"${pul:,.1f}")
print(words_en)
print(words_ru)
