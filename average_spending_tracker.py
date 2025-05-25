from num2words import num2words

b_kun=12.0
i_kun=15.0
u_kun=10.0
t_kun=13.0
besh_kun=12.5
o_kun=11.0
y_kun=14.0
bir_hafta_xarajat=b_kun+i_kun+u_kun+t_kun+besh_kun+o_kun+y_kun
print(bir_hafta_xarajat)

avg=bir_hafta_xarajat/7
print(avg)
words_en=num2words(avg)
words_ru=num2words(avg,lang='ru')

print(f"${avg:,.2f}")
print(words_en)
print(words_ru)
