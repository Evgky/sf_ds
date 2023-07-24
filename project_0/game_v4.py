import numpy as np

def game_core_v4(number: int = 1) -> int:
    """Сначала устанавливаем любое random число.
       А потом в зависимости от того, больше оно или меньше нужного, ищем рандомно в нужном интервале.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0

    i = 1
    j = 101
    predict = np.random.randint(i, j)

    while number != predict:
        count += 1

        if number > predict:
            i = predict + 1
        else:
            j = predict
            
        predict = np.random.randint(i, j)
    # Ваш код заканчивается здесь

    return count
