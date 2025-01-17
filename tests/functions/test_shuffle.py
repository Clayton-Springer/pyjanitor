import pytest


@pytest.mark.functions
def test_shuffle(dataframe):
    """
    Test the shuffle function.

    This test checks that the set of indices in the shuffled dataframe are
    identical to the set of indices in the original.
    """
    df = dataframe.shuffle()

    assert set(df.index) == set(dataframe.index)
