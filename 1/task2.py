a = int(input("Введите трехзначное число:"))
counter = 100
sum = 0

while counter > 0:
    sum = sum + a//counter
    a = a%counter
    counter = counter/10
print(int(sum))