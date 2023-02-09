import unittest
import buysellstock
import buysellstock_arr

class TestBuySellStock(unittest.TestCase):
    def test_buySellStock(self):
        # Provided Examples
        self.assertEqual(buysellstock.maxProfit([7,1,5,3,6,4]),5)
        self.assertEqual(buysellstock.maxProfit([7,6,4,3,1]),0)

        # Arrays generated with random.randint()
        self.assertEqual(buysellstock.maxProfit(buysellstock_arr.arr0),158)
        self.assertEqual(buysellstock.maxProfit(buysellstock_arr.arr1),14)
        self.assertEqual(buysellstock.maxProfit(buysellstock_arr.arr2),91)
        self.assertEqual(buysellstock.maxProfit(buysellstock_arr.arr3),662)
        self.assertEqual(buysellstock.maxProfit(buysellstock_arr.arr4),178)
        self.assertEqual(buysellstock.maxProfit(buysellstock_arr.arr5),0)
        self.assertEqual(buysellstock.maxProfit(buysellstock_arr.arr6),4)


        

if __name__ == '__main__':
    unittest.main()
