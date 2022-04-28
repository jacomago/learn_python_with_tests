import unittest


class TestStuff(unittest.TestCase):
    def test_int(self):
        self.assertEqual(3 + 4, 7)

    def test_float(self):
        self.assertEqual(1.1 + 0.5, 1.6)

    def test_float_unequal(self):
        self.assertEqual(1 / 3, 0.3333333333333333)

    def test_almost_equal_places(self):
        self.assertAlmostEqual(1.44, 1.45, places=1)

    def test_almost_equal(self):
        self.assertTrue(0.1 > (1.44 - 1.45))


if __name__ == "__main__":
    unittest.main()
