board = list(range(1, 10))  # игровое поле для игры (board).


def draw_board():  # В функции выводим первую строку, состоящую из 13 символов «тире»,
    # после чего, в цикле прорисовываем остальные края поля.
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


"""Создадим функцию take_input() с аргументом player_token:
Внутри функции сначала задаётся переменная valid, которая равняется False, после чего идёт цикл while, который 
не закончится, пока valid не примет значение True. В цикле производится ввод пользователем определённой клетки,
в которую будет ставиться крестик, либо нолик. Если же пользователь ввёл, а какой-либо другой символ, выведется 
ошибка.
Далее в условии проверяется, занята ли введённая клетка. Если клетка занята, то выведется соответствующая ошибка, 
если же введено число не в диапазоне от 1, до 10 — будет так же выведено соответствующее сообщение."""


def take_input(player_token):

    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


"""Создадим функцию check_win(), в которой будем проверять, выиграл ли игрок. 
Внутри функции создаётся кортеж win_coord, в котором хранятся победные комбинации. 
В цикле производится проверка на победу игрока, если он побеждает, то выводится сообщение о победе, 
если же нет — возвращается False, и игра продолжается."""


def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


"""Теперь создадим функцию main(). Внутри функции, после обозначения переменных, создаётся цикл, 
который закончится после победы одного из игроков, или ничьей. Внутри цикла проводится проверка, 
какой игрок сходил, после чего вызывается функция take_input() с соответствующим символом игрока. 
Далее идёт проверка, какой игрок выиграл, или вышла ничья."""


def main():
    counter = 0
    win = False
    while not win:
        draw_board()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win()
        if tmp:
            print(tmp, "выиграл!")
            break
        if counter == 9:
            print("Ничья!")
            break
    draw_board()


main()
input("Нажмите Enter для выхода!")
