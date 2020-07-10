import requests

from typing import List
from typing import Dict
from typing import Union

from datetime import date
from datetime import datetime


class BureauEconomicAnalysisClient():

    def __init__(self, api_key: str):
        """Initalize the Bureau of Economic Analysis Client."""

        # base URL for the SEC EDGAR browser
        self.bea_url = "https://apps.bea.gov/api/data/"
        self.api_key = api_key
        self._format = 'JSON'

        if self.api_key:
            self.authstate = True
        else:
            self.authstate = False

    @property
    def format(self) -> str:
        """Used to return the Content format currently set for request.

        Returns:
        ----
        str: If `JSON`, then data from API request will be sent back
            as JSON data. If `XML` then the data will be returned back
            as XML data.
        """
        return self._format

    @format.setter
    def format(self, value) -> None:
        """Used to return the Content format currently set for request.

        Raises:
        ----
        ValueError: If the format is incorrect will raise a ValueError.

        Arguments:
        ----
        value (str): If `JSON`, then data from API request will be sent back
            as JSON data. If `XML` then the data will be returned back
            as XML data.
        """

        if value.upper() not in ['JSON', 'XML']:
            raise ValueError(
                'Incorrect format, please set to either `XML` or `JSON`.'
            )

        self._format = value.upper()

    def __repr__(self) -> str:
        """String representation of our BEA Class instance."""

        # define the string representation
        str_representation = '<BureauEconomicAnalysis Client (authorized={auth_state})>'.format(
            auth_state=self.authstate
        )

        return str_representation

    def _make_request(self, method: str, params: Dict) -> Dict:
        """Makes all the request for the BEA Client.

        Arguments:
        ----
        method (str): The type of request to make. Can be one of the
            following: ['get', 'post', 'put', 'delete', 'put']

        params (Dict): Any parameters to send along with the request.

        Raises:
        ----
        requests.ConnectionError: If connection error occurs will raise
            an error.

        Returns:
        ----
        Dict: The JSON or XML content.
        """

        # Define a new session.
        request_session = requests.Session()
        request_session.verify = True

        # Define a new request.
        request_request = requests.Request(
            method=method.upper(),
            url=self.bea_url,
            params=params
        ).prepare()

        # Send the request.
        response: requests.Response = request_session.send(
            request=request_request
        )

        # Close the Session
        request_session.close()

        print(response.url)

        # If the response is OK then return it.
        if response.ok and self._format == 'JSON':
            return response.json()
        elif response.ok and self._format == 'XML':
            return response.text
        else:
            raise requests.ConnectionError()

    def get_dataset_list(self) -> Dict:
        """Returns a list of all the datasets available from the API.

        Returns:
        ----
        Dict: A dictionary with a collection of datasets, their corresponding names,
            and their descriptions

        Example URL:
        ----
        https://apps.bea.gov/api/data/?UserID={YOUR_API_KEY}&method=GETDATASETLIST&ResultFormat=JSON

        Usage:
        ----
            >>> # Initalize the new Client.
            >>> bea_client = BureauEconomicAnalysisClient(api_key=API_KEY)

            >>> # Grab the Dataset List.
            >>> dataset_list = bea_client.get_dataset_list()
        """

        # Define the parameters.
        params = {
            'UserID': self.api_key,
            'method': 'GETDATASETLIST',
            'ResultFormat': self._format
        }

        # Make the request.
        response = self._make_request(
            method='get',
            params=params
        )

        return response

    def get_parameters_list(self, dataset_name: str) -> Dict:
        """Retrieves a list of the parameters (required and optional) for a particular dataset.

        Returns:
        ----
        Dict: A dictionary with a collection of datasets parameters, their corresponding names,
            and their descriptions

        Example URL:
        ----
        https://apps.bea.gov/api/data?&UserID={YOUR_API_KEY}&method=GETPARAMETERLIST&datasetname=Regional&ResultFormat=JSON

        Usage:
        ----
            >>> # Initalize the new Client.
            >>> bea_client = BureauEconomicAnalysisClient(api_key=API_KEY)

            >>> # Grab the Paramters List.
            >>> parameters_set_list = bea_client.get_parameters_list()
        """

        # Define the parameters.
        params = {
            'userid': self.api_key,
            'method': 'GETPARAMETERLIST',
            'datasetname': dataset_name,
            'resultformat': self._format
        }

        # Make the request.
        response = self._make_request(
            method='get',
            params=params
        )

        return response

    def gdp_by_industry(self, year: List[str] = 'ALL', industry: List[str] = 'ALL', frequency: str = 'A,Q', table_id: List[str] = 'ALL') -> Dict:
        """Grabs the estimates of value added, gross output, intermediate inputs, KLEMS, and employment statistics by industry.

        Arguments:
        ----
        year (List[str], optional): . Defaults to 'ALL'.
        
        industry (List[str], optional): [description]. Defaults to 'ALL'.
        
        frequency (str, optional): [description]. Defaults to 'A,Q'.
        
        table_id (List[str], optional): [description]. Defaults to 'ALL'.

        Returns:
        ----
        Dict: A list of GDP figures for the industry specified.

        Example URL:
        ----
        https://apps.bea.gov/api/data?&UserID={YOUR_API_KEY}&method=GETPARAMETERLIST&datasetname=Regional&ResultFormat=JSON

        Usage:
        ----
            >>> # Initalize the new Client.
            >>> bea_client = BureauEconomicAnalysisClient(api_key=API_KEY)

            >>> # Grab the Paramters List.
            >>> parameters_set_list = bea_client.get_parameters_list()
        """        

        if year != 'ALL':
            year = ','.join(year)

        # Define the parameters.
        params = {
            'userid': self.api_key,
            'method':'GetData',
            'datasetname': 'GDPbyIndustry',
            'year': year,
            'resultformat': self._format,
            'industry': industry,
            'frequency': frequency,
            'tableid': table_id
        }

        # Make the request.
        response = self._make_request(
            method='get',
            params=params
        )

        return response
