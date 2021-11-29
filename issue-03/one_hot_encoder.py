from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestFT(unittest.TestCase):
    def test_tf(self):
        """
        Тест проверяет функцию fit_transform на массиве из 2-х городов
        """
        actual = fit_transform(['Moscow', 'Tula'])
        expected = [('Moscow', [0, 1]), ('Tula', [1, 0])]
        self.assertEqual(actual, expected)

    def test_tf_in(self):
        """
        Тест проверяет функцию fit_transform на массиве из 2-х городов на true
        """
        actual = fit_transform(['Moscow', 'Kiev'])
        expected = ('Moscow', [0, 1])
        self.assertIn(expected, actual)

    def test_tf_type(self):
        """
        Тест проверяет функцию fit_transform на тип результата
        """
        actual = fit_transform(['Moscow'])
        self.assertIsInstance(actual, List)

    def test_empty(self):
        """
        Тест проверяет функцию fit_transform на пустых входных данных
        """
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
    from pprint import pprint

    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities

