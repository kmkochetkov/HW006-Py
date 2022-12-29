# Дан список, вывести отдельно буквы и цифры, пользуясь filter
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

# Начальные данные
data = [12,'sadf',5643]

# Списки цифр и строк

nums = list(filter(lambda x: type(x) == int, data))
letters = list(filter(lambda x: type(x) == str, data))
print(f"Начальные данные: {data}")
print(f"Вывод букв и цифр отдельно: {letters}, {nums}")