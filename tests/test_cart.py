import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


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
        self.assertEqual(self.cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(-10)

    def test_sort_cart(self):
        d1 = DigitalVideoDisc("B title", cost=20.0)
        d2 = DigitalVideoDisc("A title", cost=50.0)
        self.cart.add_dvd(d1)
        self.cart.add_dvd(d2)
        self.cart.sort_by_title()
        self.assertEqual(self.cart.items[0].title, "A title")
        self.cart.sort_by_cost()
        self.assertEqual(self.cart.items[0].cost, 50.0)

    def test_search_by_category(self):
        d1 = DigitalVideoDisc("A", category="Animation")
        d2 = DigitalVideoDisc("B", category="Action")
        results = search_by_category([d1, d2], "animation")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "A")

    def test_search_by_title_case_insensitive(self):
        d = DigitalVideoDisc("The Lion King")
        results = search_by_title([d], "lion")
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
