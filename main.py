# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import plotly.graph_objects as go

from credit.Apartment import Apartment
from credit.CombinedCredit import CombinedCredit


def compute(rates, repays):
    for year in range(len(years)):
        for credit in range(len(credits)):
            combined.append(CombinedCredit(credits[credit], rates[year][0], repays[year][0], 0, years[year]))
            i = len(combined) - 1
            # combined[i].add_post_credit(rates[year][1], repays[year][1], 0, 30 - years[year])
            # combined[i].post_credit.add_post_credit(rates[year][2], repays[year][2], 0, 20)

            total = combined[i].get_series_total()
            annuity = combined[i].get_avg_annuity()
            rate = total[0][0]
            repay = total[1][0]
            capital = total[2][0]
            results.append(
                {"credit": combined[i], "annuity": annuity, "rate": rate, "repay": repay, "capital": capital})

            combined[i].add_trace(fig)
            print("-----------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    years = [32,32]
    rates = [
        [[0.026, 0.0263]] * 3,
        [[0.026, 0.0263]] * 3,
    ]
    repays = [
        [0.02, 0.035, 0.1],
        [0.04, 0.035, 0.1],
    ]
    total = 558000
    credits = [[total - 168000, 168000], [225000, 225000]]
    combined = []
    i = 0

    # 2,63 168 2,5 rest 15jahre

    # nice: 10, 20, 0.0256,0.0256, 0.02, 0.04
    fig = go.Figure()

    results = []
    compute(rates, repays)

    print("-----------")

    rates = [
        [[0.0259, 0.0259], [0.05, 0.05], [0.05, 0.05]],
        [[0.025, 0.0263], [0.05, 0.05], [0.05, 0.05]],
        [[0.025, 0.0263], [0.05, 0.05], [0.05, 0.05]],
    ]

    repays = [
        [0.02, 0.01, 0.05],
        [0.02, 0.01, 0.05],
        [0.02, 0.02, 0.075],
    ]

    # compute(rates, repays)

    """
    apartment = Apartment(16, 30, 90)
    apartment.add_trace(fig)
    apartment = Apartment(18, 30, 90)
    apartment.add_trace(fig)
    apartment = Apartment(20, 30, 90)
    apartment.add_trace(fig)
    apartment = Apartment(24, 30, 90)
    apartment.add_trace(fig)
    """

    results = sorted(results, key=lambda d: d['rate'])
    for result in results:
        annuity = result["annuity"]
        rate = result["rate"]
        repay = result["repay"]
        capital = result["capital"]
        print(
            f"Total {result['credit']}:\t\t\t\t\t\t\t\t\t\t ~{annuity}\t\t\t-{rate:.2f}\t\t\t+{repay:.2f}\t\t={capital:.2f}")

    # Create and style traces
    # Edit the layout
    fig.update_layout(title='Darlehen',
                      xaxis_title='Jahr',
                      yaxis_title='Geld in €')

    fig.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
