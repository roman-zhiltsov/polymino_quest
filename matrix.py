import copy

from config import COLOR_DICT
from config import RESET_COLOR


class Matrix:
    def __check_matrix_rectangle(self):
        s = {len(row) for row in self.data}
        assert len(s) == 1, 'matrix data is not rectangle'

    def __check_matrix_symbols(self):
        for row in self.data:
            for i in row:
                assert i in {0, 1}, 'wrong matrix data'

    def __get_rank(self):
        rank1 = 0
        for row in self.data:
            rank1 += sum(row)
        return self.width * self.height - rank1, rank1

    def __get_shift(self):
        for i, value in enumerate(self.data[0]):
            if value == 1:
                return i

    def __get_repr(self):
        s = ''.join(''.join(list(map(str, row))) for row in self.data)
        return f'{self.__width}{s}'

    def __init__(self, data):
        self.__data = []
        for row in data:
            self.__data.append(row[:])

        self.__width = len(self.__data[0])
        self.__height = len(self.__data)
        self.__rank0, self.__rank1 = self.__get_rank()
        self.__shift = self.__get_shift()
        self.__repr = self.__get_repr()

    def check_data(self):
        self.__check_matrix_rectangle()
        self.__check_matrix_symbols()

    def __get_zone_size(self, x, y, point_set):
        counter = 0
        if not (0 <= x < self.width and 0 <= y < self.height):
            return counter
        if self.data[y][x] != 0:
            return counter
        if (x, y) in point_set:
            return counter
        counter += 1
        point_set.add((x, y))
        counter += self.__get_zone_size(x, y + 1, point_set)
        counter += self.__get_zone_size(x, y - 1, point_set)
        counter += self.__get_zone_size(x + 1, y, point_set)
        counter += self.__get_zone_size(x - 1, y, point_set)
        return counter

    def check_zones(self, min_size):
        points_set = set()
        for y, row in enumerate(self.data):
            for x, i in enumerate(row):
                #if i != 0:
                #    continue
                #if (x, y) in points_set:
                #    continue
                zone_size = self.__get_zone_size(x, y, points_set)
                if zone_size % min_size != 0:
                    return
        return True

    def check_data_type(self, tp):
        # TODO: проверить, что данные сохранены в верном формате (для фигуры - tuple, для поля - list)
        pass

    def check_connectivity(self, symbol):
        # TODO: проверить связность (для фигуры - по единицам, для поля по нулям)
        pass

    def check_efficiency(self, symbol):
        # TODO: проверить, что данные хранятся от края до края (для фигуры - по единицам, для поля по нулям)
        pass

    @property
    def data(self):
        return self.__data

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def rank0(self):
        return self.__rank0

    @property
    def rank1(self):
        return self.__rank1

    @property
    def shift(self):
        return self.__shift

    def __eq__(self, other):
        return self.__data == other.__data

    def __repr__(self):
        return self.__repr

    @property
    def repr(self):
        return self.__repr

    def print_matrix(self, line=''):
        s = '\n'.join(''.join(list(map(str, row))) for row in self.__data)
        s = s.replace('0', ' ').replace('1', '▮')
        return f'{line}\n{s}\n'

    def __str__(self):
        return self.print_matrix()

    def print_color_matrix(self,):
        for row in self.data:
            for i in row:
                assert i > 0
                if i == 1:
                    print(' ', end='')
                else:
                    print(f'{COLOR_DICT[i]}▮{RESET_COLOR}', end='')
            print()
