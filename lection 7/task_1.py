# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

from math import sqrt

class Segment:
    def __init__(self, point_1, point_2):
        """ Инициализации двух кортежей с координатами точек (x1, y1), (x2, y2)
        :param point_1: Координаты точки 1
        :param point_2: Координаты точки 2
        """
        self.x1 = point_1[0]
        self.y1 = point_1[1]
        self.x2 = point_2[0]
        self.y2 = point_2[1]

    def length(self):
        """ Измерения длины отрезка по заданным координатам двух точек
        :return: длина отрезка, с округлением до 2 знаков после запятой
        """
        length = round(sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2), 2)
        return length

    def x_axis_intersection(self):
        """ Индикация пересечения отрезком оси абцисс
        :return: True, если отрезок пересекает ось абцисс, иначе False
        """
        res = (self.x1 >= 0 and self.x2 <= 0) or (self.x1 <= 0 and self.x2 >= 0)
        return res

    def y_axis_intersection(self):
        """ Индикация пересечения отрезком оси ординат
        :return: True, если отрезок пересекает ось ординат, иначе False
        """
        res = (self.y1 >= 0 and self.y2 <= 0) or (self.y1 <= 0 and self.y2 >= 0)
        return res


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
