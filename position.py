from matrix import Matrix


class Position:
    def __init__(self, matrix_data):
        self.__matrix = Matrix(matrix_data)
        self.__rank = self.__matrix.rank1
        self.__shift = self.__matrix.shift

    def check_data(self):
        self.matrix.check_data_type(tuple)
        self.matrix.check_connectivity(1)
        self.matrix.check_efficiency(1)

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
    def rank(self):
        return self.__rank

    @property
    def height(self):
        return self.matrix.height

    @property
    def shift(self):
        return self.__shift

    def __repr__(self):
        return self.matrix.repr

    @property
    def repr(self):
        return self.__repr__()

    @property
    def name(self):
        return f'position {self.rank}-{self.repr}'

    def __eq__(self, other):
        return self.repr == other.repr

    def __lt__(self, other):
        return self.repr < other.repr

    def __hash__(self):
        return self.repr.__hash__()

    @property
    def hash(self):
        return self.__hash__()

    def __str__(self):
        return self.matrix.print_matrix(self.name)
