import pytest
from app.сalculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator



    def test_division_good(self):
        assert self.calc.division(self, 10, 5) == 2


    def test_multiply_good(self):
        assert self.calc.multiply(self, 4, 6) == 24


    def test_subtraction_good(self):
        assert self.calc.subtraction(self, 16, 8) == 8


    def test_adding_good(self):
        assert self.calc.adding(self, 7, 8) == 15
