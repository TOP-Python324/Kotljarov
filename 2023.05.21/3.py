number = int(input('enter the number: '))
# УДАЛИТЬ: данные переменные используются каждая только единожды — неоптимально
# КОММЕНТАРИЙ: если бы операции, выполняемые для вычисления значений этих переменных, были бы более сложными и длинными, то можно было оправдать создание отдельных переменных — в данном случае операции тривиальны и вполне могут быть прописаны и выполнены вместо использования данных переменных
hour = number // 60
mins = number % 60
print(f'{number} минут = это {hour} часа {mins} минут')



# ДОБАВИТЬ: результат выполнения программы с собственными данными


# ИТОГ: хорошо — 2/3
