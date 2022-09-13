#  Пользователь вводит время в минутах и расстояние в километрах. 
#  Найдите скорость в м/c..

def fast(time_num, way_num):
    speed_count = round(way_num * 1000 / (time_num * 60), 1)
    print(f'Скорость = {speed_count} м/с')

fast(2, 10)