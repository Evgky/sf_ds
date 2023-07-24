def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем число, находящееся в середине загаданного интервала (1, 100).
       А потом в зависимости от того, больше оно или меньше нужного, ищем середину интервала.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0

    i = 0
    j = 100
    predict = (i+j)//2

    while number != predict:
        count += 1

        if number > predict:
            i = predict + 1
            predict = (i+j)//2
        elif number < predict:
            j = predict - 1
            predict = (i+j)//2
    # Ваш код заканчивается здесь

    return count
