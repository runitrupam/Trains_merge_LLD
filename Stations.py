class Stations:
    # private variable
    __station_distance_from_HYB = {
        "HYB": 0, "NGP": 400, "ITJ": 700, "BPL": 800,
        "AGA": 1300, "NDL": 1500, "PTA": 1800, "NJP": 2200, "GHY": 2700}

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
