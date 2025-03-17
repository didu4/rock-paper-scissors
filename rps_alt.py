import random

def play():
    while True:

        player = input("Выберите знак: r — камень, p — бумага, s — ножницы:\n")

        if (player == 'Stop') or (player == 'stop') or (player == 'quit') or (player == 'Quit'):
            print('Игра успешно завершена')
            break

        if error(player):
            print('Неправильно подобран знак. Попробуй ещё раз\nДля завершения игры напиши стоп-слово quit или stop')
            continue

        robot = random.choice(['r','p','s'])
        print('Робот выбрал', robot)

        if player == robot:
            print('Ничья.\nДля завершения игры напиши стоп-слово quit или stop')

        elif winner(player, robot):
            print('Поздравляю! Ты победил!\nДля завершения игры напиши стоп-слово quit или stop')

        else:
            print('Ты проиграл. Попробуй ещё раз!\nДля завершения игры напиши стоп-слово quit или stop')

def winner(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
def error(sign):
    if (sign != 'r') and (sign != 'p') and (sign != 's'):
        return True

play()