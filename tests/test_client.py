import os
import unittest

from unittest import TestCase
from configparser import ConfigParser
from pybea.client import BureauEconomicAnalysisClient


class TestBeaClient(TestCase):

    """Will perform a unit test for the `BureauEconomicAnalysisClient`."""

    def setUp(self) -> None:
        """Set up the Client."""

        # Grab configuration values.
        if not os.environ.get("api_key"):
            config = ConfigParser()
            config.read("configs/config.ini")
            api_key = config.get("alex_credentials", "API_KEY")
        else:
            api_key = os.environ.get("api_key")

        # Initalize the new Client.
        self.bea_client = BureauEconomicAnalysisClient(api_key=api_key)

    def test_creates_instance_of_session(self):
        """Create an instance and make sure it's a <PLACEHOLDER>."""

        self.assertIsInstance(self.bea_client, BureauEconomicAnalysisClient)

    def tearDown(self) -> None:
        """Teardown the `BureauEconomicAnalysisClient`."""
        del self.bea_client


if __name__ == "__main__":
    unittest.main()
