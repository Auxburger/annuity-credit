import math
from abc import abstractmethod


class Series():

    @abstractmethod
    def get_series_monthly(self):
        pass

    @abstractmethod
    def update_series(self, series, source_series, x1, x2):
        pass

    def reduce_series_from_monthly(self, interval=0):
        series_monthly = self.get_series_monthly()
        interval = len(series_monthly[0]) if interval == 0 else interval
        series = [[0 for y in range(math.ceil(len(series_monthly[0]) / interval))] for x in range(len(series_monthly))]
        interval_index = 0
        for i in range(len(series_monthly[0])):
            if i % interval == 0 and i != 0 and i != len(series_monthly[0]):
                interval_index += 1
            self.update_series(series, series_monthly, interval_index, i)
        return series

    def get_series_yearly(self):
        series = self.reduce_series_from_monthly(12)
        return series

    def get_series_total(self):
        series = self.reduce_series_from_monthly()
        return series
