"""
Test goes here

"""

from main import (
    generate_vis_general_polars_congress,
    generate_summary,
    general_polars_describe,
)

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


def test_general_describe():
    """Function calling describe_iris and general_describe which tests different parts of
    the dataset"""

    # only works for the example_csv link
    median_test, desribe_test = general_polars_describe(example_csv)

    # write an assert statement to check median_test and desribe_test of age column
    # mean of age column in congress dataset
    assert median_test["age"][0] == 53.0
    # standard deviation of age column in congress dataset
    assert desribe_test[["describe", "age"]][2, 1] == 53.31373222430909
    # mean of age column in congress dataset
    assert desribe_test[["describe", "age"]][3, 1] == 10.678469157541093


def test_viz_general():
    """Function calling generate_vis_general_polars_congress"""

    generate_vis_general_polars_congress(example_csv)


def test_generate_summary_report():
    """Function calling generate_summary()"""
    generate_summary(example_csv)


if __name__ == "__main__":
    test_general_describe()
    # test_viz_general()
    # test_generate_summary_report()
