# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])


# fig.write_html('first_figure.html', auto_open=True)


class Darlehen:
    def __init__(self, capital, rate, redemption, sredemption, years):
        self.capital = capital
        self.rate = rate
        self.redemption = redemption
        self.years = years
        self.sredemption = sredemption
        self.annuity = (self.capital * self.rate / 12) + (self.capital * self.redemption / 12)
        self.rate_monthly = []
        self.redemption_monthly = []
        self.capital_monthly = []

    def compute(self):
        self._compute(self.capital)

    def _compute(self, capital):
        rate_total_sum = 0
        for y in range(self.years):
            rate_year_sum = 0
            for m in range(12):
                rate_month = round(self.rate * capital / 12 * 100) / 100
                self.rate_monthly.append(rate_month)
                rate_year_sum = round((rate_year_sum + rate_month) * 100) / 100
                redemption_month = round((self.annuity - rate_month) * 100) / 100
                self.redemption_monthly.append(redemption_month)
                capital = round((capital - redemption_month) * 100) / 100
                self.capital_monthly.append(capital)
            rate_total_sum = round((rate_total_sum + rate_year_sum) * 100) / 100


class CombinedDarlehen():
    def __init__(self, darlehen1: Darlehen, darlehen2: Darlehen):
        self.d1 = darlehen1
        self.d2 = darlehen2

    def print(self):
        print(
            "rate\tredemption\tcapital\t\t\trate\tredemption\tcapital\t\t\tsum_rate\tsum_redemption\tannuity\t\tsum_capital")
        for i in range(len(self.d1.capital_monthly)):
            rate = self.d1.rate_monthly[i] + self.d2.rate_monthly[i]
            redemption = self.d1.redemption_monthly[i] + self.d2.redemption_monthly[i]
            capital = self.d1.capital_monthly[i] + self.d2.capital_monthly[i]
            print(
                f"{self.d1.rate_monthly[i]:.2f}\t{self.d1.redemption_monthly[i]:.2f}\t\t{self.d1.capital_monthly[i]:.2f}\t\t" +
                f"{self.d2.rate_monthly[i]:.2f}\t{self.d2.redemption_monthly[i]:.2f}\t\t{self.d2.capital_monthly[i]:.2f}\t\t" +
                f"{rate:.2f}\t\t\t{redemption:.2f}\t\t{rate + redemption:.2f}\t\t{capital:.2f}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    z = 0.0256
    t = 0.02
    darlehen1 = Darlehen(450000, z, t, 0, 10)
    darlehen1.compute()
    darlehen2 = Darlehen(101000, z, t, 0, 10)
    darlehen2.compute()
    combined = CombinedDarlehen(darlehen1, darlehen2)
    combined.print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
