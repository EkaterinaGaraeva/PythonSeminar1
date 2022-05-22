# Сообщить в какой четверти координационной плоскости 
# или на какой оси находится точка с координатами X и Y

def coordinates(x, y):
    if (x > 0) and (y > 0):
        print(f"1 четверть")
    elif (x > 0) and (y < 0):
        print(f"2 четверть")
    elif (x < 0) and (y < 0):
        print(f"3 четверть")
    elif (x < 0) and (y > 0):
        print(f"4 четверть")
    elif (x == 0) and (y != 0):
        print(f"на оси X")
    elif (x != 0) and(y == 0):
        print(f"на оси Y")
    else:
        print(f"начало координат")

coordinates(0, 0)
