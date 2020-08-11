from matrix import Matrix


class Field:
    def __init__(self, data):
        self.__matrix = Matrix(data)
        self.__length = 0

    def check_data(self):
        self.matrix.check_data()
        self.matrix.check_data_type(list)
        self.matrix.check_connectivity(0)
        self.matrix.check_efficiency(0)

    @property
    def matrix(self):
        return self.__matrix

    @property
    def data(self):
        return self.matrix.data

    @property
    def width(self):
        return self.matrix.width

    @property
    def height(self):
        return self.matrix.height

    @property
    def rank(self):
        return self.__matrix.rank0

    @property
    def area(self):
        return self.width * self.height

    @property
    def length(self):
        return self.__length

    def __repr__(self):
        return self.matrix.repr

    @property
    def repr(self):
        return self.__repr__()

    @property
    def name(self):
        return f'field {self.rank}-{self.repr}'

    def get_empty_cell(self):
        for y, row in enumerate(self.__matrix.data):
            for x, i in enumerate(row):
                if i == 0:
                    return x, y

    def __check_borders(self, position, x, y):
        if x < 0 or y < 0:
            return
        if x + position.width > self.width or y + position.height > self.height:
            return
        return True

    def check_place(self, position, x, y):
        if not self.__check_borders(position, x, y):
            return

        for py, row in enumerate(position.data):
            for px, i in enumerate(row):
                if i == 1 and self.matrix.data[y + py][x + px] >= 1:
                    return

        return True

    def add(self, position, x, y, number=0):
        if not self.__check_borders(position, x, y):
            return False

        for py, row in enumerate(position.data):
            for px, i in enumerate(row):
                if i == 1:
                    self.data[y + py][x + px] += number

        self.__length += 1
        return True

    def get_copy(self):
        new_field = Field(self.matrix.data)
        new_field.__length = self.__length
        return new_field

    def print_color_matrix(self):
        self.matrix.print_color_matrix()

    def __str__(self):
        return self.matrix.print_matrix(self.name)
