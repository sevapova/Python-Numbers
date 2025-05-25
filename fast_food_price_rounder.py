from num2words import num2words

m_narxi1=4.5
m_narxi2=3.2
m_narxi3=5.5

umumiy_yigindi=m_narxi1+m_narxi2+m_narxi3
print(umumiy_yigindi)

words_en=num2words(umumiy_yigindi)
words_ru=num2words(umumiy_yigindi,lang='ru')

yaxlitlash=round(umumiy_yigindi,2)
print(yaxlitlash)


print(f"${yaxlitlash:,.2f}")
print(words_en)
print(words_ru)
