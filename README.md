# Python Bureau Of Economic Analysis API Client

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Support These Projects](#support-these-projects)

## Overview

An Python API client used to pull and retrieve data from the US Bureau of Economic Analysis.

## Setup

Right now, the library is not hosted on **PyPi** so you will need to do a local install on your system if you plan
to use it in other scrips you use.

First, clone this repo to your local system. After you clone the repo, make sure to run the `setup.py` file, so you
can install any dependencies you may need. To run the `setup.py` file, run the following command in your terminal.

```console
pip install -e .
```

This will install all the dependencies listed in the `setup.py` file. Once done you can use the library
wherever you want.

## Usage

Here is a simple example of using the `pybea` library to grab a list of the different datasets availabel.

```python
from pprint import pprint
from configparser import ConfigParser
from pybea.client import BureauEconomicAnalysisClient

# Grab configuration values.
config = ConfigParser()
config.read('configs/config.ini')
API_KEY = config.get('alex_credentials', 'API_KEY')

# Initalize the new Client.
bea_client = BureauEconomicAnalysisClient(api_key=API_KEY)

# Grab the Dataset List.
dataset_list = bea_client.get_dataset_list()
pprint(dataset_list)
```

You will note the output of the above code would look like the following:

```json
{
    "BEAAPI": {
        "Request": {
            "RequestParam": [
                {
                    "ParameterName": "METHOD",
                    "ParameterValue": "GETPARAMETERLIST"
                },
                ...
                {
                    "ParameterName": "RESULTFORMAT",
                    "ParameterValue": "JSON"
                }
            ]
        },
        "Results": {
            "Parameter": [
                {
                    "ParameterName": "GeoFips",
                    "ParameterDataType": "string",
                    "ParameterDescription": "Comma-delimited list of 5-character geographic codes; COUNTY for all counties, STATE for all states, MSA for all MSAs, MIC for all Micropolitan Areas, PORT for all state metro/nonmetro portions, DIV for all Metropolitan Divisions, CSA for all Combined Statistical Areas, state post office abbreviation for all counties in one state (e.g. NY)",
                    "ParameterIsRequiredFlag": "1",
                    "MultipleAcceptedFlag": "1"
                }
                ...
                ,
                {
                    "ParameterName": "Year",
                    "ParameterDataType": "string",
                    "ParameterDescription": "Comma-delimted list of years; LAST5 for latest 5 years; LAST10 for latest 10 years; ALL for all years",
                    "ParameterIsRequiredFlag": "0",
                    "ParameterDefaultValue": "LAST5",
                    "MultipleAcceptedFlag": "1"
                }
            ]
        }
    }
}
```

## Support these Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I"m always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me to pay monthly fees.

**YouTube:**
If you"d like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).

**Hire Me:**
If you have a project, you think I can help you with feel free to reach out at [coding.sigma@gmail.com](mailto:coding.sigma@gmail.com?subject=[GitHub]%20Project%20Proposal) or fill out the [contract request form](https://forms.office.com/Pages/ResponsePage.aspx?id=ZwOBErInsUGliXx0Yo2VfcCSWZSwW25Es3vPV2veU0pUMUs5MUc2STkzSzVQMFNDVlI5NjJVNjREUi4u)
