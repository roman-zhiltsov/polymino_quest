import colorama

PENTAMINO = dict(
    F=((1, 1, 0),
       (0, 1, 1),
       (0, 1, 0)),
    I=((1, 1, 1, 1, 1), ),
    L=((1, 1, 1, 1),
       (1, 0, 0, 0)),
    N=((1, 1, 1, 0),
       (0, 0, 1, 1)),
    P=((1, 1, 1),
       (1, 1, 0)),
    T=((1, 1, 1),
       (0, 1, 0),
       (0, 1, 0)),
    U=((1, 1, 1),
       (1, 0, 1)),
    V=((1, 1, 1),
       (1, 0, 0),
       (1, 0, 0)),
    W=((1, 1, 0),
       (0, 1, 1),
       (0, 0, 1)),
    X=((0, 1, 0),
       (1, 1, 1),
       (0, 1, 0)),
    Y=((1, 1, 1, 1),
       (0, 1, 0, 0)),
    Z=((1, 1, 0),
       (0, 1, 0),
       (0, 1, 1))
)

TEST_FIELD = ([1, 1, 0, 0, 1, 1],
              [1, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1])

TEST_FIELD_2 = ([1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 1],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 1],
                [1, 0, 1, 0, 0, 1])


FIELD_3X10 = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],)

FIELD_3X15 = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],)

FIELD_3X20 = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],)

FIELD_4X15 = ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],)

FIELD_8X8 = ([0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],)

DIAG_FIELD_WITH_HOLE = ([1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],)

SPECIAL_FIELD = ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
                 [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],)

SPECIAL_FIELD_2 = ([1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
                   [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
                   [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1],)


COLOR_DICT = {
    0: colorama.Fore.BLACK,
    1: colorama.Fore.WHITE,
    2: colorama.Fore.BLUE,
    3: colorama.Fore.CYAN,
    4: colorama.Fore.GREEN,
    5: colorama.Fore.MAGENTA,
    6: colorama.Fore.RED,
    7: colorama.Fore.YELLOW,
    8: colorama.Fore.LIGHTBLACK_EX,
    9: colorama.Fore.LIGHTBLUE_EX,
    10: colorama.Fore.LIGHTCYAN_EX,
    11: colorama.Fore.LIGHTGREEN_EX,
    12: colorama.Fore.LIGHTMAGENTA_EX,
    13: colorama.Fore.LIGHTRED_EX,
    14: colorama.Fore.LIGHTYELLOW_EX,
}

RESET_COLOR = colorama.Style.RESET_ALL
