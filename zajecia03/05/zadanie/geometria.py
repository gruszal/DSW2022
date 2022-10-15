def pole_prostokata(a, b=None):
    if b is None:
        b = a
    if a < 0 or b < 0:
        raise ValueError('Bok prostokąta nie może mieć ujemnej długości.')
    return a * b


def pole_kola(r, pi):
    """
    Funkcja obliczająca pole koła dla zadanego przybliżenia liczby PI.
    :param r: promień koła.
    :param pi: przybliżenie liczby PI.
    :return: pole koła.
    """
    if r < 0:
        raise ValueError('Promień koła nie może mieć ujemnej długości.')
    return pi * r ** 2
