import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://raw.githubusercontent.com/abhirup-ghosh/e2e-data-pipeline/main/data/competitions.csv'

    comp_dtype = {
        'competition_id': str,
        'competition_code': str,
        'name': str,
        'sub_type': str,
        'type': str,
        'country_id': pd.Int64Dtype(),
        'country_name': str,
        'domestic_league_code': str,
        'confederation': str,
        'url': str,
        'is_major_national_league': pd.Int64Dtype()
    }

    return pd.read_csv(url, sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'