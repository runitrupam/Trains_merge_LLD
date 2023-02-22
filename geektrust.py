'''
Some assumptions I have taken : 
 If there are no passenger bogies to travel from Hyderabad station,
  then train should stop there. In such a case it should print JOURNEY_ENDED 
e.g. 
ARRIVAL TRAIN_A ENGINE NJP GHY AGA BPL PTA
ARRIVAL TRAIN_B JOURNEY_ENDED
DEPARTURE TRAIN_B ENGINE GHY NJP PTA AGA BPL

For journey continue after HYB , 
ARRIVAL TRAIN_A ENGINE NDL NDL GHY NJP NGP
ARRIVAL TRAIN_B ENGINE NJP GHY AGA BPL PTA
DEPARTURE TRAIN_AB ENGINE ENGINE GHY GHY NJP NJP PTA NDL NDL AGA BPL NGP

'''

from sys import argv

from Arrival import Train_Arrival
from Departure import Train_Departure


class TakeInput:
    def __init__(self):
        input = self.take_input()
        self.train_a = self.get_trains(input[0])
        self.train_b = self.get_trains(input[1])

    def take_input(self):
        if len(argv) != 2:
            raise Exception("File path not entered")
        file_path = argv[1]
        f = open(file_path, 'r')
        input = f.readlines()
        return input

    def get_trains(self, input):
        input1 = input.split()
        train = []

        for st in input1:
            if st.strip() != '':
                train.append(st.strip())
        return train

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


def solution():
    try:
        ob = TakeInput()
        ob.train_a = Train_Arrival._get_train_arrival(
            ob.train_a)  # Returns a 2D list having upcoming stations --> distance 
        ob.train_b = Train_Arrival._get_train_arrival(
            ob.train_b)  # Returns a 2D list having upcoming stations --> distance 
        Train_Departure._get_train_departure(ob.train_a, ob.train_b)
    except Exception as e:
        raise Exception("File path not entered")


def main():
    solution()


if __name__ == "__main__":
    main()
