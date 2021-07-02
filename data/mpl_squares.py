import csv
from datetime import datetime

from matplotlib import pyplot as plt

file_name = "sitka_weather_2014.csv"


class Squares:
    with open(file_name) as t:
        reader = csv.reader(t)
        head_row = next(reader)
        print(head_row)
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)

        plt.style.use("seaborn")
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red', alpha=0.5)
        ax.plot(dates, lows, c='blue', alpha=0.5)
        ax.set_title("zgwd", fontsize=24)
        ax.set_ylabel("F", fontsize=24)
        fig.autofmt_xdate()
        ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
        plt.show()


if __name__ == "__main__":
    sq = Squares()
