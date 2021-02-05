import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", delimiter=",")
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)
    # Create first line of best fit
    fl_result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = np.array([i for i in range(df["Year"].min(), 2050)])
    ax.plot(x, fl_result.intercept + fl_result.slope*x, 'r', label='first line')
    ax.set_xlim(right=2050)
    # Create second line of best fit
    df_after_2000 = (df[df["Year"] >= 2000]).copy()
    sl_result = linregress(df_after_2000["Year"], df_after_2000["CSIRO Adjusted Sea Level"])
    x = np.array([i for i in range(2000, 2050)])
    ax.plot(x, sl_result.intercept + sl_result.slope*x, 'y', label='second line')
    
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
