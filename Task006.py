# Дано число обозначающее день недели.
# Вывести его название и является ли выходным.

def Weekday(number):
    words = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    print(words[number - 1])
    if (number == 6 or number == 7):
        print(f"выходной")

Weekday(7)
