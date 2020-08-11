import unittest

import config
from figure import Figure
from field import Field


# TODO: написать тесты к методу add класса Field
# TODO: написать тесты к классам Figure, Position


def equal(obj, field):
    obj.assertEqual(obj.field.name, field.name)
    obj.assertEqual(obj.field.repr, field.repr)
    obj.assertEqual(obj.field.width, field.width)
    obj.assertEqual(obj.field.height, field.height)
    obj.assertEqual(obj.field.rank, field.rank)
    obj.assertEqual(obj.field.area, field.area)


class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field(config.TEST_FIELD)
        #print(self.field)

    def tearDown(self):
        pass

    def test_params(self):
        self.assertEqual(self.field.rank, 20)
        self.assertEqual(self.field.area, 30)
        self.assertEqual(self.field.width, 6)
        self.assertEqual(self.field.height, 5)

    def test_check_place(self):
        figure = Figure(config.PENTAMINO['W'])

        for i, position in enumerate(figure):
            check = self.field.check_place(position, -1, 0)
            self.assertFalse(check)

        for i, position in enumerate(figure):
            check = self.field.check_place(position, 0, 0)
            if i == 3:
                self.assertTrue(check)
            else:
                self.assertFalse(check)

        for i, position in enumerate(figure):
            check = self.field.check_place(position, 3, 0)
            if i == 1:
                self.assertTrue(check)
            else:
                self.assertFalse(check)

        for position in figure:
            check = self.field.check_place(position, 4, 0)
            self.assertFalse(check)

        for position in figure:
            check = self.field.check_place(position, 6, 0)
            self.assertFalse(check)

        figure = Figure(config.PENTAMINO['Y'])

        for i, position in enumerate(figure):
            check = self.field.check_place(position, -1, 2)
            self.assertFalse(check)

        for i, position in enumerate(figure):
            check = self.field.check_place(position, 0, 1)
            if i in {2, 3, 6}:
                self.assertTrue(check)
            else:
                self.assertFalse(check)

        for i, position in enumerate(figure):
            check = self.field.check_place(position, 0, 2)
            if i in {0, 1}:
                self.assertTrue(check)
            else:
                self.assertFalse(check)

        for position in figure:
            check = self.field.check_place(position, 2, 4)
            self.assertFalse(check)

    def test_add(self):
        pass

    def test_get_copy(self):
        field2 = self.field.get_copy()
        equal(self, field2)
        self.assertEqual(self.field.matrix, field2.matrix)
        self.assertEqual(self.field.data, field2.data)

        figure = Figure(config.PENTAMINO['Y'])
        self.assertTrue(field2.add(figure[2], 0, 1, 1))
        equal(self, field2)
        self.assertNotEqual(self.field.matrix, field2.matrix)
        self.assertNotEqual(self.field.data, field2.data)
