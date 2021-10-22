
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from canshuhua.bank import bank_transformMoney
from canshuhua.Calc import Calc

da = [
    ['jason', 'asdfgh', '123456', 2000, 0],
    ['jason', 'asdfgh', '123466', 1000, 2],
    ['jason', 'asdfgh', '123456', 7000, 3],
    ['jason', 'asdfghk', '123456', 200, 1]
]

@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def test_bank(self, a, b, c, d, e):
        result = bank_transformMoney(a, b, c, d)

        self.assertEqual(result, e)


