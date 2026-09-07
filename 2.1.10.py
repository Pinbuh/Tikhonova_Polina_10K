sec = int(input())
hours = sec // 3600
mins = (sec % 3600) // 60
sec1 = sec % 60
print(f"Время с момента старта: {sec} секунд.\nФорматированное время: {hours} ч {mins} мин {sec1} сек.")