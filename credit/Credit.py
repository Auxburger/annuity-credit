import numpy as np

from credit.Series import Series


class Credit(Series):
    def __init__(self, capital, rate, repay, srepay, years, paid=0, cost=0):
        self.capital = capital
        self.rate = rate
        self.repay = repay
        self.years = years
        self.srepay = srepay
        self.annuity = (self.capital * self.rate / 12) + (self.capital * self.repay / 12)
        self.rate_monthly = []
        self.sum_rate_monthly = []
        self.sum_repay_monthly = []
        self.repay_monthly = []
        self.capital_monthly = []
        self.cost = cost
        self.paid = paid

    def compute(self):
        self._compute(self.capital)

    def _compute(self, capital):
        rate_total_sum = 0
        sum_rate_month = self.cost
        sum_repay_month = self.paid
        for y in range(self.years):
            rate_year_sum = 0
            for m in range(12):
                rate_month = round(self.rate * capital / 12 * 100) / 100
                self.rate_monthly.append(rate_month)

                sum_rate_month = round((sum_rate_month + rate_month) * 100) / 100
                self.sum_rate_monthly.append(sum_rate_month)

                rate_year_sum = round((rate_year_sum + rate_month) * 100) / 100
                repay_month = round((self.annuity - rate_month) * 100) / 100

                sum_repay_month = round((sum_repay_month + repay_month) * 100) / 100
                self.sum_repay_monthly.append(sum_repay_month)

                self.repay_monthly.append(repay_month)
                if repay_month > capital:
                    capital = 0
                    self.capital_monthly.append(capital)
                    self.years = y + 1
                    break
                capital = round((capital - repay_month) * 100) / 100
                self.capital_monthly.append(capital)
            rate_total_sum = round((rate_total_sum + rate_year_sum) * 100) / 100
            if capital == 0:
                break
        self.cost = sum_rate_month
        self.paid = sum_repay_month

    def get_series_monthly(self):
        series = [[]] * 7
        series[0] = self.rate_monthly
        series[1] = self.repay_monthly
        series[2] = self.capital_monthly
        series[3] = self.sum_rate_monthly
        series[4] = self.sum_repay_monthly
        series[5] = list(np.around(np.add(np.array(self.sum_repay_monthly), np.array(self.sum_rate_monthly)), 2))
        series[6] = [self.annuity for _ in range(len(series[0]))]
        return series

    def update_series(self, series, source_series, x1, x2):
        series[0][x1] = round((series[0][x1] + source_series[0][x2]) * 100) / 100
        series[1][x1] = round((series[1][x1] + source_series[1][x2]) * 100) / 100
        series[2][x1] = source_series[2][x2]
        series[3][x1] = source_series[3][x2]
        series[4][x1] = source_series[4][x2]
        series[5][x1] = source_series[5][x2]
        series[6][x1] = source_series[6][x2]

    def print_total(self):
        total = self.get_series_total()
        rate = total[0][0]
        repay = total[1][0]
        capital = total[2][0]
        print(f"Total: -{rate:.2f}\t\t\t+{repay:.2f}\t\t={capital:.2f}")
