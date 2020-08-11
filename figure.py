import copy

from position import Position


class Figure:
    def __get_positions(self, source_data):
        data_rotation = copy.deepcopy(source_data)
        positions = set()

        for _ in range(4):
            data_rotation = tuple(zip(*data_rotation[::-1]))
            positions.add(data_rotation)
        data_rotation = tuple(zip(*data_rotation))
        for _ in range(4):
            data_rotation = tuple(zip(*data_rotation[::-1]))
            positions.add(data_rotation)

        return positions

    def __init__(self, source_matrix_data):
        self.__positions = []
        for matrix_data in self.__get_positions(source_matrix_data):
            position = Position(matrix_data)
            position.check_data()
            self.__positions.append(position)
        self.__positions.sort(reverse=True)
        self.__position_repr = {position.repr for position in self.__positions}

    @property
    def positions(self):
        return self.__positions

    @property
    def position(self):
        return self.positions[0]

    @property
    def rank(self):
        return self.position.rank

    def __repr__(self):
        return self.position.repr

    @property
    def repr(self):
        return self.__repr__()

    @property
    def name(self):
        return f'figure {self.rank}-{self.repr}'

    def __len__(self):
        return len(self.positions)

    def __getitem__(self, item):
        return self.positions[item]

    def __iter__(self):
        return iter(self.positions)

    def __eq__(self, other):
        return self.repr == other.repr

    def __lt__(self, other):
        return self.repr < other.repr

    def __hash__(self):
        return self.position.hash

    def __str__(self):  #TODO: (?) писать инфу о фигуре правее рисунка
        return self.position.matrix.print_matrix(self.name)

