a = int(input("Введите номер билета:"))

first = a%1000
second = a//1000

counter = 100
sum1 = 0

while counter > 0:
    sum1 = sum1 + first//counter
    first = first%counter
    counter = counter/10


counter = 100
sum2 = 0

while counter > 0:
    sum2 = sum2 + second//counter
    second = second%counter
    counter = counter/10

if sum1 == sum2:
    print("YES")
else:
    print("NO")
