import time

import config
from field import Field
from manifold import Manifold


manifold_rank = 5

filling_list = []
start = time.time()


def finder(field, figures):
    # получаем поле,
    # получаем позиции, которые можно перебирать

    # 1 получаем пустую клетку поля (если пустой клетки нет, то заполнение найдено; записываем его в хранилище)
    # 2 пытаемся применить к ней все возможные позиции по очереди (см. перебор позиций)
    # 3 если позицию удаётся применить, делаем новый рекурсивный вызов, отправляя туда новый объект field
    # 4 если нет, то пропускаем позицию

    # перебор позиций
    # для перебора позиций используется список фигур;
    # следует идти по фигурам списка, пропуская фигуру, если её позиция уже есть в заполнении поля

    empty_cell = field.get_empty_cell()
    if empty_cell is None:
        filling_list.append(field)
        print(len(filling_list))
        field.print_color_matrix()
        return

    x, y = empty_cell

    for i, figure in enumerate(figures):
        for position in figure:
            if not field.check_place(position, x - position.shift, y):
                continue

            field_next = field.get_copy()
            field_next.add(position, x - position.shift, y, field_next.length + 2)

            if not field_next.matrix.check_zones(manifold_rank):
                continue

            figures_next = figures[:]
            figures_next.pop(i)
            finder(field_next, figures_next)


def main():
    manifold = Manifold(manifold_rank)
    figures = manifold.figures
    #field = Field(config.TEST_FIELD)
    #field = Field(config.FIELD_3X10)  # 8.5, 0.95
    #field = Field(config.FIELD_3X15)  # 1223, 35.8
    #field = Field(config.FIELD_3X20)  # 71775, 919; pypy 114
    #field = Field(config.FIELD_8X8)  # 434, 432; pypy 52
    #field = Field(config.FIELD_4X15)  # ?, 10821; pypy 960
    field = Field(config.FIELD_5X12)  # ?, _; pypy 1597
    #field = Field(config.DIAG_FIELD_WITH_HOLE)  #294, 88
    #field = Field(config.SPECIAL_FIELD)  #?, 714
    #field = Field(config.SPECIAL_FIELD_2)  # ?, ?
    field.check_data()

    finder(field, figures)
    finish = time.time()

    print(f'timer: {finish - start}')


if __name__ == '__main__':
    main()
