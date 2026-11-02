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

    def test_sort_cart(self):
        d1 = DigitalVideoDisc("B title", cost=20.0)
        d2 = DigitalVideoDisc("A title", cost=50.0)
        self.cart.add_dvd(d1)
        self.cart.add_dvd(d2)
        self.cart.sort_by_title()
        self.assertEqual(self.cart.items[0].title, "A title")
        self.cart.sort_by_cost()
        self.assertEqual(self.cart.items[0].cost, 50.0)
