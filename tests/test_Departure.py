import unittest


class TestMethods(unittest.TestCase):
    def test__get_train_departure(self):
        # pytest tests/test_Departure.py::test__get_train_departure
        from Departure import Train_Departure
        train_a = [['AGA', 1300], ['HYB', 0], ['ITJ', 700], ['BPL', 800]]
        train_b = [['PTA', 1800], ['HYB', 0], ['BPL', 800], ['ITJ', 700], ['NJP', 2200]]
        Train_Departure._get_train_departure(train_a, train_b)
        self.assertTrue(True)
