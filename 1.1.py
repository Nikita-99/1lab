print("Введите a")
a = int(input())
print("Введите b")
b = int(input())
print("Введите c")
c = int(input())
print("Введите k")
k = int(input())
try:
    s = (a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c

    if s > 0:
         
         print(s)
    else:
         print(-s)
except ZeroDivisionError:
    print("Выделите на 0")
    print("Давайте попробуем еще раз")
finally:
    main()
