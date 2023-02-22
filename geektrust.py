from sys import argv

from Arrival import Train_Arrival
from Departure import Train_Departure
from Get_Input import Fetch_Input


def get_arrival_and_departure():
    try:
        fetch_object = Fetch_Input(argv)

        fetch_object.train_a = fetch_object._get_trains(fetch_object.input_file[0])
        fetch_object.train_b = fetch_object._get_trains(fetch_object.input_file[1])

        fetch_object.train_a = Train_Arrival._get_train_arrival(
            fetch_object.train_a)  # Returns a 2D list having upcoming stations --> distance 
        fetch_object.train_b = Train_Arrival._get_train_arrival(
            fetch_object.train_b)  # Returns a 2D list having upcoming stations --> distance 

        Train_Departure._get_train_departure(fetch_object.train_a, fetch_object.train_b)
    except Exception as e:
        raise Exception("File path not entered")


def main():
    get_arrival_and_departure()


if __name__ == "__main__":
    main()
