import unittest

import parser_field as pf


class ParserTestCase(unittest.TestCase):

    def placeholder(self, s: str):
        # self.s = s
        # return s
        pass

    def setUp(self):
        self.field_name = "Ты не пройдешь!!!"

    """
    parse_number_list(print_error, s: str, field_name: str)
    Классы эквивалентности для этой функции:
    1) валидные значения:
       a) строка с целыми чиселами через запятую;
       b) строка с float'ами через запятую;
    2) невалидные значения:
       a) пустая строка;
       b) строка с символами;
    """
    def test_parse_number_list_empty_str(self):
        errors = []
        res = pf.parse_number_list(lambda x: errors.append(x), "", self.field_name)
        self.assertEqual(errors[0], "Поле \"" + self.field_name + "\" не заполнено")
        self.assertEqual(res, [])

    def test_parse_number_list_int(self):
        res = pf.parse_number_list(None, "-1, 2, -3, 4, -5", self.field_name)
        # self.assertEqual(errors[0], "Поле \"" + self.field_name + "\" не заполнено")
        self.assertEqual(res, [-1, 2, -3, 4, -5])

    def test_parse_number_list_float(self):
        res = pf.parse_number_list(None, "1.185628563, 2.3, -3.0, 4.617, -5.0234820", self.field_name)
        # self.assertEqual(errors[0], "Поле \"" + self.field_name + "\" не заполнено")
        self.assertEqual(res, [1.185628563, 2.3, -3.0, 4.617, -5.0234820])

    def test_parse_number_list_str(self):
        res = pf.parse_number_list(None, "п, 2.3, -3.0, 4.6f7, -5.02sdf20", self.field_name)
        # self.assertEqual(errors[0], "Поле \"" + self.field_name + "\" не заполнено")
        self.assertEqual(res, "Поле \"" + self.field_name + "\" заполнено некорректно")

    # parse_number(number, field_name: str, print_error) -> int
    def test_parse_number_ok(self):
        res = pf.parse_number(1, self.field_name, None)
        # self.assertEqual(errors[0], "Поле \"" + self.field_name + "\" не заполнено")
        self.assertEqual(res, 1)

    def test_parse_number_fail(self):
        errors = []
        res = pf.parse_number(0, self.field_name, lambda x: errors.append(x))
        self.assertEqual(errors[0], "Поле \"" + self.field_name + "\" заполнено некорректно")
        self.assertEqual(res, 0)

    """
    parse_coordinates(s: str, print_error, separator = ';')
    Классы эквивалентности для этой функции:
    1) валидные значения:
       a) строка с целыми числами и float'ами через запятую и в [];
    2) невалидные значения:
       a) пустая строка;
       b) строка с символами;
    """
    def test_parse_coordinates_empty_str(self):
        errors = []
        res = pf.parse_coordinates("", lambda x: errors.append(x))
        self.assertEqual(errors[0], "Поле \"Координаты экстремумов\" не заполнено")
        self.assertEqual(res, [])

    def test_parse_coordinates_str(self):
        errors = []
        res = pf.parse_coordinates("[1, 2], [d, g], [9, 0o]", lambda x: errors.append(x))
        self.assertEqual(errors[0], "Поле \"Координаты экстремумов\" заполнено некорректно")
        self.assertEqual(res, [])

    def test_parse_coordinates_ok(self):
        res = pf.parse_coordinates("[1, 2], [8, 3], [9, 0]", None)
        self.assertEqual(res, [[1, 2], [8, 3], [9, 0]])


if __name__ == '__main__':
    unittest.main()
