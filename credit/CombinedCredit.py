import numpy as np

from credit.Utils import Utils
from credit.Colors import colors
from credit.Credit import Credit
import plotly.graph_objects as go


class CombinedCredit:
    def __repr__(self):
        return f"{self.years, self.capitals, self.rate}, {self.post_credit.__repr__() if self.post_credit is not None else ''}"

    def __init__(self, capitals, rate, repay, srepay, years, paid=None, cost=None):
        if cost is None:
            cost = [0, 0]
        if paid is None:
            paid = [0, 0]
        self.d1 = Credit(capitals[0], rate[0], repay, srepay, years, paid[0], cost[0])
        self.d2 = Credit(capitals[1], rate[1], repay, srepay, years, paid[1], cost[1])
        self.years = years
        self.capitals = capitals
        self.rate = rate
        self.repay = repay
        self.srepay = srepay
        self.years = years
        self.d1.compute()
        self.d2.compute()
        self.annuity = round((self.d1.annuity + self.d2.annuity) * 100) / 100
        self.post_credit = None
        self.print_total()

    def get_years(self):
        years = self.years
        if self.post_credit is not None:
            years = f"{years}, {self.post_credit.get_years()}"
        return years

    def get_rates(self):
        rates = self.rate
        if self.post_credit is not None:
            rates = f"{rates}, {self.post_credit.get_rates()}"
        return rates

    def get_avg_annuity(self):
        annuity = self.annuity
        if self.post_credit is not None:
            annuity = round((annuity + self.post_credit.get_avg_annuity()) / 2)
        return annuity

    def add_post_credit(self, rate, repay, srepay, years):
        remaining_credit1 = self.d1.get_series_total()[2][0]
        remaining_credit2 = self.d2.get_series_total()[2][0]
        if remaining_credit1 == 0 and remaining_credit2 == 0:
            return
        cost = [self.d1.cost, self.d2.cost]
        paid = [self.d1.paid, self.d2.paid]
        self.post_credit = CombinedCredit([remaining_credit1, remaining_credit2], rate, repay, srepay, years,
                                          paid, cost)

    def get_series_monthly(self):
        series = np.around(np.add(np.array(self.d1.get_series_monthly()), np.array(self.d2.get_series_monthly())),
                           2)
        if self.post_credit is not None:
            series = np.concatenate((series, np.array(self.post_credit.get_series_monthly())), axis=1)
        return series.tolist()

    def get_series_yearly(self):

        series = Utils.rounded_sum_arrays(self.d1.get_series_yearly(), self.d2.get_series_yearly())
        if self.post_credit is not None:
            series = np.concatenate((series, np.array(self.post_credit.get_series_yearly())), axis=1)
        return series.tolist()

    def get_series_total(self):
        series = Utils.rounded_sum_arrays(self.d1.get_series_total(), self.d2.get_series_total())
        if self.post_credit is not None:
            post = self.post_credit.get_series_total()
            capital = post[2][0]
            series = np.around(np.add(series, np.array(post)))
            series[2][0] = capital
        return series.tolist()

    def print_yearly(self):
        yearly = self.get_series_yearly()
        for i in range(len(yearly[0])):
            rate = yearly[0][i]
            repay = yearly[1][i]
            capital = yearly[2][i]
            print(f"-{rate:.2f}\t\t\t+{repay:.2f}\t\t={capital:.2f}")

    def print_total(self):
        total = self.get_series_total()
        rate = total[0][0]
        repay = total[1][0]
        capital = total[2][0]
        print(
            f"Total {self.years, self.capitals, self.rate}:\t\t ~{self.annuity}\t\t -{rate:.2f}\t\t\t+{repay:.2f}\t\t={capital:.2f}")

    def add_trace(self, fig):
        series = self.get_series_yearly()
        x = np.arange(len(series[0]))

        i = 0
        for s in range(len(series[3])):  # hausgeld
            series[3][i] = round(series[3][s] + 12 * 370 * i, 2)
            i += 1

        color = next(colors)
        # fig.add_trace(go.Scatter(x=x, y=series[0], name=f"Rate {self.get_years(), self.capitals, self.get_rates()}",
        #                         line=dict(width=4, color=color), mode='lines+markers'))
        # fig.add_trace(go.Scatter(x=x, y=series[1], name=f"Tilg {self.get_years(), self.capitals, self.get_rates()}",
        #                         line=dict(width=4, dash='dot', color=color), mode='lines+markers'))
        # fig.add_trace(go.Scatter(x=x, y=series[2], name=f"Capital {self.get_years(), self.capitals, self.get_rates()}",
        #                         line=dict(width=4, dash='dash', color=color), mode='lines+markers'))
        fig.add_trace(go.Scatter(x=x, y=series[3], name=f"Cost {self.get_years(), self.capitals, self.get_rates()}",
                                 line=dict(width=4, dash='dot', color=color), mode='lines+markers'))
        # fig.add_trace(go.Scatter(x=x, y=series[4], name=f"Paid {self.get_years(), self.capitals, self.rate}",
        #                         line=dict(width=4, dash='dash', color=color), mode='lines+markers'))
        # fig.add_trace(go.Scatter(x=x, y=series[5], name=f"Total {self.get_years(), self.capitals, self.rate}",
        #                        line=dict(width=4, dash='dash', color=color), mode='lines+markers'))
        fig.add_trace(go.Scatter(x=x, y=series[6], name=f"Annuity {self.get_years(), self.capitals, self.get_rates()}",
                                 line=dict(width=4, dash='dot', color=color), mode='lines+markers'))
