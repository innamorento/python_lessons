a = int(input("Введите количество кораблей:"))
if a%6 != 0:
    print("Нельзя определить")
else:
    first_and_thed = a/3
    second = a - first_and_thed
    print(f"{first_and_thed/2}  {second}  {first_and_thed/2}")
#print(a%3)
#counter = 100
#sum = 0

#while counter > 0:
#    sum = sum + a//counter
#    a = a%counter
#    counter = counter/10
#print(int(sum))