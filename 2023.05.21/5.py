# ПЕРЕИМЕНОВАТЬ: в Python для имён почти всех переменных используется змеиный_нижний_регистр или слитныйнижнийрегистр (для имён классов используется ВерблюжийРегистр)
wholeNumber = input('ввод: ')
fractNumber = input('ввод: ')
num = float(wholeNumber + '.' + fractNumber)
km = num * 1.61
print(f'{num} миль = {km:.1f} км')


# ввод: 2
# ввод: 367
# 2.367 миль = 3.8 км


# КОММЕНТАРИЙ: изучите PEP 8 — набор рекомендаций по оформлению кода: https://peps.python.org/pep-0008/


# ИТОГ: отлично — 5/5
