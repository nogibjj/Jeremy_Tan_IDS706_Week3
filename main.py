import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import polars as pl


def general_polars_describe(csv):
    """polars describe function in csv"""
    polars_df = pl.read_csv(csv)
    return polars_df.median(), polars_df.describe()


def general_describe(csv):
    """general describe function in csv"""
    general_df = pd.read_csv(csv)
    return general_df.describe()


def general_polars_summary_with_profile(csv):
    """general describe function in csv"""
    polars_df = pl.scan_csv(csv)
    profile = ProfileReport(polars_df, title="Profiling Report")
    profile.to_file("polars.html")


def generate_vis_general_polars_congress(csv):
    """generate example visualization of the congress dataset"""
    pd.set_option("display.max_columns", None)
    polars_df = pl.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(polars_df["age"], bins=20, edgecolor="black")
    plt.title("Age Distribution of Congress Members")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.savefig("congress.png")


def generate_general_markdown(csv):
    """generate an md file with outputs"""
    markdown_table1, markdown_table2 = general_polars_describe(csv)
    markdown_table1 = str(markdown_table1)
    markdown_table2 = str(markdown_table2)

    # Write the markdown table to a file
    with open("congress_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("Median:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](congress.png)\n")


def generate_vis_general_congress(csv):
    """generate example visualization of the congress dataset"""
    pd.set_option("display.max_columns", None)
    general_df = pd.read_csv(csv)
    # print(general_df.head())
    # print(general_df.describe())
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["age"], bins=20, edgecolor="black")
    plt.title("Age Distribution of Congress Members")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()


def generate_summary(csv):
    """generates report of any dataset"""
    general_df = pd.read_csv(csv)
    profile = ProfileReport(general_df, title="Profiling Report")
    profile.to_file("profile.html")
