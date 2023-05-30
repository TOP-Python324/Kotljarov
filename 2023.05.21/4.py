number = int(input('введите трёхзначное число: '))
sot = number // 100
des = (number - (sot * 100)) // 10
ed = number - ((sot * 100) + (des * 10))
summa = sot + des + ed
proizv = sot * des * ed
print(f'сумма цифр = {summa}\nпроизведение цифр = {proizv}')