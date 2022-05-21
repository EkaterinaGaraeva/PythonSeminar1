# Проверить истинность утверждений -(x v y v z) = ¬x ∧ ¬y ∧ ¬z
# для ВСЕХ значений предикат

# x = 1
# y = 1
# z = 1
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            left = not (x or y or z)
            rigth = not x and not y and not z
            statement = left == rigth
            print(statement)
            
