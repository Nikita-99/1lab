stroka=str(input("Введите элемнты через пробел "))
s=stroka.split(' ')
for j in range (0,len(s)):
    if j % 2 != 0:
        print(s[j])
