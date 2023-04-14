n = int(input("Введите длинну шоколадки:"))
m = int(input("Введите ширину шоколадки:"))
k = int(input("Введите количество долек для отлома:"))

if k > n*m:
    print("Слишком большой кусок")
elif k%n == 0 or k%m == 0:
    print("yes")
else:
    print("no")

