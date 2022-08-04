import numpy as np
from credit.Colors import colors
import plotly.graph_objects as go

from credit.Series import Series


class Apartment(Series):
    def __init__(self, rent, years, size):
        self.rent = rent * size
        self.years = years
        sum_rent_month = 0
        self.sum_rent_monthly = []
        for i in range(years * 12):
            sum_rent_month = round((sum_rent_month + self.rent), 2)
            self.sum_rent_monthly.append(sum_rent_month)

    def get_series_monthly(self):
        series = [[]]
        series[0] = self.sum_rent_monthly
        return series

    def update_series(self, series, source_series, x1, x2):
        series[0][x1] = source_series[0][x2]

    def add_trace(self, fig):
        series = self.get_series_yearly()
        x = np.arange(len(series[0]))

        color = next(colors)
        fig.add_trace(go.Scatter(x=x, y=series[0], name=f"Rent {self.years, self.rent}",
                                 line=dict(width=4, color=color), mode='lines+markers'))
