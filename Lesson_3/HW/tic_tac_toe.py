"""Задаем параметры поля"""
board_size = 3
board_tic_tac_toe = list(range(1, 10))


def draw_board(board):
    """
    Метод отрисовки игрового поля
    """
    print("-" * 13)
    for i in range(board_size):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_chip):
    """
    Метод для получения ввода от пользователя
    Вводим переменную valid = False и цикл while.
    Цикл будет выполняться до тех пор, пока valid = True
    """
    while True:
        # Бесконечный цикл
        """
        Просим ввести значения. Если этих значение нет в строке "123456789" - пишем что не верно 
        и просим ввести заново.
        И запускаем код заново с помощью continue
        """
        value = input("Ходит " + player_chip + ". Куда поставим ?: ")
        if not (value in "123456789"):
            print("Неверный ввод. Введите значения от 1 до 9")
            continue
        """
        Превращаем введенный символ в число и проверяем свободна ли клетка.
        Для этого проверяем строку str(board[value - 1]) in "XO" есть ли там "XO". если есть говорим об этом игрокам
        И запускаем код заново с помощью continue
        """
        value = int(value)
        if str(board_tic_tac_toe[value - 1]) in "XO":
            print("Клетка занята. Выберите другое место")
            continue
        """
        Если все условия соблюдаются, в ячейку будет вписан знак, которым играем пользователь.
        player_chip это Х или О
        """
        board_tic_tac_toe[value - 1] = player_chip
        break


def check_win(board_tic_tac_toe):

    """
    Определили выигрышные комбинации
    """
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
        (0, 4, 8), (2, 4, 6)  # диагональные линии
    )
    """
        Для каждого элемента в массиве. Обращаемся к каждому элементу в картеже.
        Если условия соблюдается, возвращаем выигрышную позицию (board[each[0]]).  
        
    """
    for each in win_combination:
        if board_tic_tac_toe[each[0]] == board_tic_tac_toe[each[1]] == board_tic_tac_toe[each[2]]:
            return board_tic_tac_toe[each[0]]
    return False


def main(board):
    counter = 0
    while True:

        # Бесконечный цикл
        """
        Используем бесконечный цикл.
        Запускаем отрисовку доски и определяем кто ходит первый.
        После хода меняем очередность.
        Цикл будет выполняться, до тех пор пока win не будет True
        """
        draw_board(board)
        """
        Проверяем кто ходит первый. Значение counter можно изменить для смены игрока 
        """
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")

        """
        Сюда передается выигрышное значение
        """
        if counter > 3:
            winner = check_win(board)
            if winner:
                draw_board(board)
                print(winner, "выиграл!")
                break

        counter += 1
        if counter == 9:
            draw_board(board)
            print("Ничья!")
            break


main(board_tic_tac_toe)

input("Нажмите Enter для выхода!")
