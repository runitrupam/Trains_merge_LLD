from Stations import Stations


class Train_Arrival(Stations):

    def __int__(self):
        super().__init__()

    @classmethod
    def _get_train_arrival(self, train: list) -> list:
        # returns a 2D list containing stations -> distance from HYB mapping 

        journey = []
        for t in range(2, len(train)):
            if self._is_station_after_HYB(train[t]):
                journey.append([train[t], self._get_distance_from_HYB(train[t])])

        journey_str = "ARRIVAL " + train[0]
        if len(journey) == 0:  # no journey left
            journey_str += " " + "JOURNEY_ENDED"
        elif len(journey) == 1 and journey[0][0] == 'HYB':  # no journey after HYB
            journey_str += " HYB " + "JOURNEY_ENDED"
        else:  # Journey left so print all stations
            journey_str += " " + train[1] + " " + " ".join([x for x, y in journey])

        print(journey_str)
        return journey
