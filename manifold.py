import config

from figure import Figure

class Manifold:
    def __get_figures(self):
        #TODO: generate all figures of the specified size

        figures = []
        for data in config.PENTAMINO.values():
            figures.append(Figure(data))
        figures.sort(reverse=True)
        return figures

    def __init__(self, rank):
        self.__rank = 5
        self.__figures = self.__get_figures()
        self.__size = len(self.__figures)

    @property
    def size(self):
        return self.__size

    @property
    def figures(self):
        return self.__figures

    @property
    def rank(self):
        return self.__rank

    @property
    def name(self):
        return f'polyomino {self.rank}'

    def __len__(self):
        return len(self.figures)

    def __getitem__(self, item):
        return self.figures[item]

    def __iter__(self):
        return iter(self.figures)

    def __str__(self):
        start = f'start {self.name}'
        end = f'end {self.name}'
        return f'{start}\n{"".join(map(str, self.__figures))}{end}'
