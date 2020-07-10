import json

from pprint import pprint
from configparser import ConfigParser
from pybea.client import BureauEconomicAnalysisClient

# Grab configuration values.
config = ConfigParser()
config.read('configs/config.ini')
API_KEY = config.get('alex_credentials', 'API_KEY')


def save_response(name: str, data: dict) -> None:
    """Use this if you want to save the responses."""

    with open('samples/responses/{name}.jsonc'.format(name=name), 'w+') as sample_file:
        json.dump(obj=data, fp=sample_file, indent=4)


# Initalize the new Client.
bea_client = BureauEconomicAnalysisClient(api_key=API_KEY)

# Grab the Dataset List.
dataset_list = bea_client.get_dataset_list()
pprint(dataset_list)

# Grab the Paramters List.
parameters_set_list = bea_client.get_parameters_list(dataset_name='Regional')
pprint(parameters_set_list)

# Grab GDP for the Finance & Insurance Industry (58), for the years 2018 & 2019 and an annual basis ('A')
gdp_by_industry = bea_client.gdp_by_industry(
    year=['2019', '2018'],
    industry='52',
    frequency='A'
)
pprint(gdp_by_industry)
