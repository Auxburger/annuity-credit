# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import plotly.graph_objects as go

from credit.Apartment import Apartment
from credit.CombinedCredit import CombinedCredit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    y = [10, 15, 15]
    y = [10, 10, 15, 15]
    z = [0.0272, 0.0285, 0.0285, 0.0303]
    z = [0.0256, 0.0243, 0.0285, 0.0303]
    z = [0.0243, 0.0272, 0.0272, 0.0285, 0.0303]
    t = [0.02, 0.02, 0.02, 0.02]
    sum = [[450000, 101000]]
    combined = []
    i = 0

    # nice: 10, 20, 0.0256,0.0256, 0.02, 0.04
    fig = go.Figure()

    results = []
    for year in range(len(y)):
        for rent in range(len(sum)):
            combined.append(CombinedCredit(sum[rent], z[year], t[year], 0, y[year], [0, 0], [0, 0]))
            combined[i].add_post_credit(z[year], 0.04, 0, 30 - y[year])
            combined[i].post_credit.add_post_credit(z[year], 0.07, 0, 20)
            total = combined[i].get_series_total()
            annuity = combined[i].get_avg_annuity()
            rate = total[0][0]
            redemption = total[1][0]
            capital = total[2][0]
            results.append(
                {"credit": combined[i], "annuity": annuity, "rate": rate, "redemption": redemption, "capital": capital})

            combined[i].add_trace(fig)
            print("-----------")
            i += 1

    print("-----------")
    for year in range(len(y)):
        for rent in range(len(sum)):
            combined.append(CombinedCredit(sum[rent], z[year], t[year], 0, y[year], [0, 0], [0, 0]))
            combined[i].add_post_credit(0.05, t[year], 0, 30 - y[year])
            combined[i].post_credit.add_post_credit(0.05, 0.02, 0, 20)
            total = combined[i].get_series_total()
            annuity = combined[i].get_avg_annuity()
            rate = total[0][0]
            redemption = total[1][0]
            capital = total[2][0]
            results.append(
                {"credit": combined[i], "annuity": annuity, "rate": rate, "redemption": redemption, "capital": capital})

            combined[i].add_trace(fig)
            print("-----------")
            i += 1
    """
    apartment = Apartment(16, 45, 90)
    apartment.add_trace(fig)
    apartment = Apartment(18, 45, 90)
    apartment.add_trace(fig)
    apartment = Apartment(20, 45, 90)
    apartment.add_trace(fig)
    apartment = Apartment(24, 45, 90)
    apartment.add_trace(fig)
    """
    results = sorted(results, key=lambda d: d['rate'])
    for result in results:
        annuity = result["annuity"]
        rate = result["rate"]
        redemption = result["redemption"]
        capital = result["capital"]
        print(
            f"Total {result['credit']}:\t\t\t\t\t\t\t\t\t\t ~{annuity}\t\t\t-{rate:.2f}\t\t\t+{redemption:.2f}\t\t={capital:.2f}")

    # Create and style traces
    # Edit the layout
    fig.update_layout(title='Darlehen',
                      xaxis_title='Monat',
                      yaxis_title='Geld in €')

    fig.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
