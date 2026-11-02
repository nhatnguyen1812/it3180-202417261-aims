import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_dvd_until_full(self):
        for i in range(MAX_NUMBERS_ORDERED):
            res = self.cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10.0))
            self.assertTrue(res)
        res_21 = self.cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0))
        self.assertFalse(res_21)

    def test_discount_calculation(self):
        self.cart.add_dvd(DigitalVideoDisc("DVD 1", cost=100.0))
        # 100 giảm 20% thì còn 80
        self.assertEqual(self.cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(-10)


if __name__ == "__main__":
    unittest.main()

    def test_search_by_title_case_insensitive(self):
        from aims.search import search_by_title
        d = DigitalVideoDisc("The Lion King")
        results = search_by_title([d], "lion")
        self.assertEqual(len(results), 1)
