"""
Docstring for Lab16_xenzonz-1.py
i. Lab 15: Plot Ohio Unemployment Data
ii. Sam Cocquyt
iii. Read Ohio unemployment data from OHUR.csv, parse the dates and unemployment
        rates, and create a time-series line plot saved as an image file.

        Also reads the CBOE Gold ETF Volatility Index data from GVZCLS.csv
iv. No starter code
v. 5/10/2026
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

def read_data(filename):

    dates = []
    unemployment_rates = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header)

        for row_number, row in enumerate(reader, start=2):
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                unemployment_rate = float(row[1])
            except ValueError:
                print(f"Skipping row {row_number}: could not convert data.")
            else:
                dates.append(current_date)
                unemployment_rates.append(unemployment_rate)

    return dates, unemployment_rates


def create_plot(dates, values, title, y_label, output_filename):
    plt.style.use("seaborn-v0_8")

    plt.figure(figsize=(12, 7))
    plt.plot(dates, values)

    plt.title(title, fontsize=24)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel(y_label, fontsize=14)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_filename)



    

def main():

    filename = "OHUR.csv"
    dates, unemployment_rates = read_data(filename)


    create_plot(
        dates,
        unemployment_rates,
        "Ohio Unemployment (by Month): 1976 - 2022",
        "Unemp Rate",
        "ohio_unemployment.png"
    )

    gold_filename = "GVZCLS.csv"
    gold_dates, gold_values = read_data(gold_filename)

    create_plot(
        gold_dates,
        gold_values,
        "Gold Volatility Index",
        "GVZCLS",
        "gold_volatility.png"
    )


if __name__ == "__main__":
    main()
