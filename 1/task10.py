coints_array=[]
size_array=int(input("Введите количество монет: "))
for i in range(size_array):
    coints_array.append(int(input("Введите монету 0 или 1: ")))
print(coints_array)
print(f"Минимальное количество монет для переворота  {coints_array.count(0)}")
