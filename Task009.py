# Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти

def Coordinates(quarter):
    if quarter <= 4:
        match quarter:
            case 1:
                print(f"X > 0 и Y > 0")
            case 2:
                print(f"X > 0 и Y < 0")
            case 3:
                print(f"X < 0 и Y < 0")
            case 4:
                print(f"X < 0 и Y > 0")

Coordinates(2)
