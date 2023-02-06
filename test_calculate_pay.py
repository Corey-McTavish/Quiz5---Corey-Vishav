from unittest import TestCase
from calculate_pay import calculate_pay


class TestCalculate(TestCase):
    def test_negative(self):
        self.assertEqual(0.0, calculate_pay(-10, -10))

    def test_zero(self):
        self.assertEqual(0.0, calculate_pay(0, 0))

    def test_under_40_hours(self):
        self.assertEqual(100.0, calculate_pay(10, 10))

    def test_over_40_hours(self):
        self.assertEqual(600.0, calculate_pay(50, 10))





