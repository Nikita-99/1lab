import random
summa=0
spisok=random.sample(range(100),10)
for j in range(0,10):
    if spisok[j] > 10:
        summa=summa+spisok[j]

print(spisok)
print(summa)
