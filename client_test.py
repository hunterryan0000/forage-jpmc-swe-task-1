import unittest
from client3 import getDataPoint


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_edge_cases(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 100}, 'top_bid': {'price': 0, 'size': 100}, 'stock': 'XYZ'},
            {'top_ask': {'price': 99999, 'size': 1}, 'top_bid': {'price': 99999, 'size': 1}, 'stock': 'XYZ'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_equal_bid_ask_price(self):
        quote = {'top_ask': {'price': 150, 'size': 10}, 'top_bid': {'price': 150, 'size': 10}, 'stock': 'GHI'}
        self.assertEqual(getDataPoint(quote), ('GHI', 150, 150, 150))

    def test_multiple_data_points(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'top_bid': {'price': 117.87, 'size': 81}, 'stock': 'DEF'},
            {'top_ask': {'price': 119.2, 'size': 36}, 'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'GHI'}
        ]
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))


if __name__ == '__main__':
    unittest.main()
