import pytest
from app.сalculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator


    @pytest.mark.parametre('x, y , expected_result', [(10, 2, 5),
                                                        (20, 10, 2),
                                                        (30, -3, -10),
                                                        (5, 2, 2.5)])
    def test_division_good(self, x, y, expected_result):
        assert self.calc.divizion(self, x, y) == expected_result

    @pytest.mark.parametre('x, y , expected_result', [(10, 2, 20),
                                                        (20, 10, 200),
                                                        (30, -3, -90),
                                                        (5, 2.5, 12.5)])
    def test_multiply_good(self, x, y, expected_result):
        assert self.calc.multiply(self, x, y) == expected_result

    @pytest.mark.parametre('x, y , expected_result', [(10, 2, 8),
                                                        (20, 10, 10),
                                                        (30, -3, 33),
                                                        (5, 2.5, 2.5)])
    def test_subtraction_good(self, x, y, expected_result):
        assert self.calc.substraction(self, x, y) == expected_result

    @pytest.mark.parametre('x, y , expected_result', [(10, 2, 12),
                                                        (20, 10, 30),
                                                        (30, -3, 27),
                                                        (5, 2.5, 7.5)])
    def test_adding_good(self, x, y, expected_result):
        assert self.calc.adding(self, x, y) == expected_result

