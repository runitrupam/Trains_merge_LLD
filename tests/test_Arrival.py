import unittest


class TestMethods(unittest.TestCase):
    def test__get_train_arrival(self):
        #  pytest tests/test_Arrival.py::test__get_train_arrival
        from Arrival import Train_Arrival
        train = ['TRAIN_A', 'ENGINE', 'BLR', 'AGA', 'BLR', 'HYB', 'ITJ', 'BPL']
        train = Train_Arrival._get_train_arrival(train)
        # assert train == [['AGA', 1300], ['HYB', 0], ['ITJ', 700], ['BPL', 800]]
        self.assertEqual(train, [['AGA', 1300], ['HYB', 0], ['ITJ', 700], ['BPL', 800]])
