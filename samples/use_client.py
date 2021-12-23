import json
from pprint import pprint
from configparser import ConfigParser
from pybea.client import BureauEconomicAnalysisClient

# Grab configuration values.
config = ConfigParser()
config.read("configs/config.ini")
API_KEY = config.get("alex_credentials", "API_KEY")


def save_response(name: str, data: dict) -> None:
    """Use this if you want to save the responses."""

    with open(
        file=f"samples/responses/{name}.jsonc",
        mode="w+",
        encoding="utf-8",
    ) as sample_file:
        json.dump(obj=data, fp=sample_file, indent=4)


# Initalize the new Client.
bea_client = BureauEconomicAnalysisClient(api_key=API_KEY)

# Grab the Dataset List.
dataset_list = bea_client.get_dataset_list()
pprint(dataset_list)

# Grab the Paramters List.
parameters_set_list = bea_client.get_parameters_list(dataset_name="Regional")
pprint(parameters_set_list)

# Grab GDP for the Finance & Insurance Industry (58), for the years 2018 &
# 2019 and an annual basis ('A')
gdp_by_industry = bea_client.gdp_by_industry(
    year=["2019", "2018"], industry="52", frequency="A"
)
pprint(gdp_by_industry)

# Grab National Product and Income Data.
national_income = bea_client.national_income_and_product_accounts(
    table_name="T10101", frequency=["A", "Q"], year=["2011", "2012"]
)
pprint(national_income)

# Grab National Product and Income Data.
national_income_detail = bea_client.national_income_and_product_accounts_detail(
    table_name="U20305", frequency=["A", "Q"], year=["2011", "2012"]
)
pprint(national_income_detail)

# Grab Current-Cost Net Stock of Private Fixed Assets, Equipment, Structures,
# and Intellectual Property Products by Type, for all years.
fixed_assets = bea_client.fixed_assets(table_name="FAAt201", year=["2011", "2012"])
pprint(fixed_assets)

# U. S. direct investment position in China and Asia for 2011 and 2012
investments = bea_client.direct_investments_and_multinational_enterprises(
    direction_of_investment="outward",
    classification="country",
    series_id=["30"],
    year=["2011", "2012"],
    country=["650", "699"],
)
pprint(investments)

# Net income and sales for Brazilian affiliates of U. S. parent enterprises,
# all industries, 2011 and 2012.
investments = bea_client.activities_investments_and_multinational_enterprises(
    direction_of_investment="outward",
    classification="CountryByIndustry",
    series_id=["4", "5"],
    year=["2011", "2012"],
    country=["202"],
    ownership_level=False,
    industry="ALL",
    non_bank_affilates_only=False,
)
pprint(investments)

# Balance on goods with China for 2011 and 2012.
balance_on_goods = bea_client.international_transactions(
    indicator=["BalGds"],
    area_or_country=["China"],
    year=["2011", "2012"],
    frequency=["A"],
)
pprint(balance_on_goods)

# U.S. assets excluding financial derivatives; change in position
# attributable to price changes for all available years
us_assets = bea_client.international_investments_positions(
    type_of_investment=["FinAssetsExclFinDeriv"],
    component=["ChgPosPrice"],
    year="ALL",
    frequency=["A"],
)
pprint(us_assets)

# Data from Industry‐by‐Commodity Total Requirements, After Redefinitions
# (Sector Level) table for years 2010, 2011, and 2012.
input_output_data = bea_client.input_output_statstics(
    table_id=["56"], year=["2010", "2011", "2012", "2013"]
)
pprint(input_output_data)

# Quarterly Value Added by Industry data for all industries for years 2012 and 2013.
underlying_gdp_by_industry = bea_client.underlying_gdp_by_industry(
    industry="ALL", frequency=["A"], year=["2012", "2013"], table_id="ALL"
)
pprint(underlying_gdp_by_industry)

# Exports of telecommunications services by U.S. parents to their foreign affiliates for all years.
international_trade_services = bea_client.international_trade_services(
    type_of_service="Telecom",
    trade_direction=["Exports"],
    year="ALL",
    affiliation=["USPARENTS"],
    area_or_country="AllCountries",
)
pprint(international_trade_services)

save_response(
    name="get_international_trade_services", data=international_trade_services
)

# Personal income for 2012 and 2013 for all counties.
regional_data = bea_client.regional(
    table_name=["CAINC1"], line_code=1, geo_fips=["COUNTY"], year=["2012", "2013"]
)
pprint(regional_data)

save_response(name="get_regional_data", data=regional_data)
