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
        # Đĩa thứ 21 phải bị từ chối (trả về False)
        res_21 = self.cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10.0))
        self.assertFalse(res_21)


if __name__ == "__main__":
    unittest.main()
