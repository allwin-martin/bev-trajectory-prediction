import unittest
from bev_demo import predict

class TestForecast(unittest.TestCase):
    def test_velocity(self):
        self.assertEqual(predict([(0,0),(2,3)], 2), [(4,6),(6,9)])
    def test_insufficient_points(self):
        with self.assertRaises(ValueError):
            predict([(1,2)])
    def test_invalid_steps(self):
        with self.assertRaises(ValueError):
            predict([(0,0),(1,1)], -1)

if __name__ == "__main__":
    unittest.main()
