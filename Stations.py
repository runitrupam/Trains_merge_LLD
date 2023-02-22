class Stations:
    __HYB = 'HYB'
    __NGP = 'NGP'
    __ITJ = 'ITJ'
    __BPL = 'BPL'
    __AGA = 'AGA'
    __NDL = 'NDL'
    __PTA = 'PTA'
    __NJP = 'NJP'
    __GHY = 'GHY'
    # private variable
    __station_distance_from_HYB = {__HYB: 0, __NGP: 400, __ITJ: 700, __AGA: 1300, __BPL: 800,
                                   __NDL: 1500, __PTA: 1800, __NJP: 2200,
                                   __GHY: 2700}

    @classmethod
    def _is_station_after_HYB(self, new_station: str) -> bool:
        if new_station in self.__station_distance_from_HYB:
            return True
        return False

    @classmethod
    def _get_distance_from_HYB(self, new_station: str) -> int:
        if new_station in self.__station_distance_from_HYB:
            return self.__station_distance_from_HYB[new_station]
        return -1
