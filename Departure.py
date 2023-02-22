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

from Stations import Stations


class Train_Departure(Stations):

    def __int__(self):
        super().__init__()

    @classmethod
    def _get_train_departure(self, train_a: list, train_b: list) -> None:
        train_a = [[t, dist] for t, dist in train_a if t != 'HYB']  # Remove the station Hyderabad
        train_b = [[t, dist] for t, dist in train_b if t != 'HYB']
        train_a.sort(key = lambda x: x[1], reverse = True)  # sort based on 2nd element
        train_b.sort(key = lambda x: x[1], reverse = True)  # sort based on 2nd element

        res = "DEPARTURE TRAIN_AB ENGINE ENGINE"

        # merge sort : merging two sorted arrays
        i = 0
        j = 0
        while (i < len(train_a) and j < len(train_b)):
            if train_a[i][1] >= train_b[j][1]:
                res += " " + train_a[i][0]
                i += 1
            else:
                res += " " + train_b[j][0]
                j += 1

        while (i < len(train_a)):
            res += " " + train_a[i][0]
            i += 1

        while (j < len(train_b)):
            res += " " + train_b[j][0]
            j += 1
        print(res)
