class Fetch_Input:

    def __init__(self, argv):
        self.input_file = self._take_input(argv)

    @classmethod
    def _take_input(self, argv):
        if len(argv) != 2:
            raise Exception("File path not entered")
        file_path = argv[1]
        f = open(file_path, 'r')
        return f.readlines()

    @classmethod
    def _get_trains(self, input):
        input1 = input.split()
        train = []

        for st in input1:
            if st.strip() != '':
                train.append(st.strip())
        return train

    @property
    def input_file(self):
        return self.__input

    @input_file.setter
    def input_file(self, value):
        self.__input = value

    @property
    def train_a(self):
        return self.__train_a

    @property
    def train_b(self):
        return self.__train_b

    @train_a.setter
    def train_a(self, value):
        self.__train_a = value

    @train_b.setter
    def train_b(self, value):
        self.__train_b = value
