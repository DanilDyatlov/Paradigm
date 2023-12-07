"""Задаем параметры поля"""
board_size = 3
board = list(range(1, 10))


def draw_board(board):
    """
    Метод отрисовки игрового поля
    """
    print("-" * 13)
    for i in range(board_size):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    """
    Метод для получения ввода от пользователя
    Вводим переменную valid = False и цикл while.
    Цикл будет выполняться до тех пор, пока valid = True
    """
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")

        try:
            player_answer = int(player_answer)
            """
            Проверка на ввод. Если ввели не число, а букву. try - если попытаются ввести букву
            """
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


def check_win(board):
    """
    Определили выигрышные комбинации. Если сходится
    """
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
        (0, 4, 8), (2, 4, 6)  # диагональные линии
    )
    for each in win_combination:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def main(board):
    counter = 0
    win = False
    while not win:
        """
        Запускаем отрисовку доски и определяем кто ходит первый.
        После хода меняем очередность.
        Цикл будет выполняться, до тех пор пока win не будет True
        """
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(board)
        """
        Сюда передается выигрышное значение. 
        """
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)

input("Нажмите Enter для выхода!")
