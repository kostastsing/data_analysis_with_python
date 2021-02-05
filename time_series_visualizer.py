import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", delimiter=",", parse_dates=["date"], index_col="date")

# Clean data
bottom = df.quantile(.025)[0]
top = df.quantile(1 - 0.025)[0]

df = df[(df["value"] >= bottom) & (df["value"] <= top)]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots(figsize=(12, 8), nrows=1, ncols=1)
    ax.plot(df_line, color="r")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    int_to_month = {"1":"January", "2":"February", "3":"March", "4":"April", "5":"May", "6":"June", "7":"July", "8":"August", "9":"September", "10":"October", "11":"November", "12":"December"}
    df_datetime = df.copy()
    df_datetime["month"] = df_datetime.index.month
    df_datetime["year"] = df_datetime.index.year
    df_bar = df_datetime.groupby(["year", "month"]).mean("value").reset_index()
    fig, _ = plt.subplots(figsize=(12, 8))
    ax = sns.barplot(data=df_bar, y="value", x="year", hue="month", palette="muted", saturation=8)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    h, l = ax.get_legend_handles_labels()
    labels = map(int_to_month.get, l)
    ax.legend(h, labels, title="Months", loc="upper left")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 7)) 
    ax1 = sns.boxplot(ax=axes[0], x="year", y="value", data=df_box)
    ax2 = sns.boxplot(ax=axes[1], x="month", y="value", data=df_box, order=months)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

