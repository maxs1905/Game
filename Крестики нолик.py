field = list(range(1,10))
win = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3,6, 9), (1, 5, 9), (3, 5, 7)]
def draw_field():
    for i in range(3):
        print(field[0 + i * 3],field[1 + i * 3], field[2 + i * 3])
def take(game_sign):
    while True:
        value = input("Куда установите ваш знак?"+game_sign)
        if not(value in '123456789'):
            print("Некоректнный ход")
            continue
        value = int(value)
        if str(field[value - 1]) in 'XO':
            print("Клетка занята, выбери другую")
            continue
        field[value - 1] = game_sign
        break
def verification_wins():
    for i in win:
        if (field[i[0]-1]) == (field[i[1]-1]) == (field[i[2]-1]):
            return field[i[1]-1]
    else:
            return False
def end():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            take('X')
        else:
            take('O')
        if counter > 3:
            winner = verification_wins()
            if winner:
                draw_field()
                print(winner, "Победа")
                break
        counter += 1
        if counter > 8:
            draw_field()
            print("Ничья")
            break

end()

