"""
Docstring for Lab16_xenzonz-1.py
i. Lab 16: Plot Ohio Unemployment Data
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

def read_data(filename: str) -> tuple[list[datetime], list[float]]:
    """
    Read dates and numeric values from a CSV file.

    The CSV file should contain a header row followed by rows of data.
    The first column should contain dates in YYYY-MM-DD format, and the
    second column should contain numeric values.

    Args:
        filename: The name of the CSV file to read.

    Returns:
        A tuple containing:
        - A list of datetime objects.
        - A list of float values.

    Notes:
        Rows with invalid dates or values are skipped.
    """

    dates: list[datetime] = []
    unemployment_rates: list[float] = []


    with open(filename, "r", newline="") as file:
        reader: csv.reader = csv.reader(file)

        header_row: list[str] = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header)

        for row_number, row in enumerate(reader, start=2):
            try:
                current_date: datetime = datetime.strptime(row[0], "%Y-%m-%d")
                unemployment_rate: float = float(row[1])
            except ValueError:
                print(f"Skipping row {row_number}: could not convert data.")
            else:
                dates.append(current_date)
                unemployment_rates.append(unemployment_rate)

    return dates, unemployment_rates


def create_plot(
    dates: list[datetime],
    values: list[float],
    title: str,
    y_label: str,
    output_filename: str
) -> None:
    
    """
    Create and save a line plot using the provided dates and values.

    Args:
        dates: A list of datetime objects used for the x-axis.
        values: A list of numeric values used for the y-axis.
        title: The title displayed at the top of the graph.
        y_label: The label displayed on the y-axis.
        output_filename: The name of the image file where the graph is saved.

    Returns:
        None
    """
    plt.style.use("seaborn-v0_8")

    plt.figure(figsize=(12, 7))
    plt.plot(dates, values)

    plt.title(title, fontsize=24)
    plt.xlabel("Date", fontsize=14)
    plt.ylabel(y_label, fontsize=14)

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_filename)



    

def main()-> None:
    """
    Run the program.

    This function reads the unemployment and gold volatility CSV files,
    then creates and saves one graph for each dataset.

    Returns:
        None
    """

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
