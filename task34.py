s = 0
term = 1  # Начальный член (1/3^0)

for _ in range(12):  # Считаем до 3^8 (всего 9 членов)
    s += term
    term *= 1/3  # Следующий член - умножение на 1/3

print(s)
