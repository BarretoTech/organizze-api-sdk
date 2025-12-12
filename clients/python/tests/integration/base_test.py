"""Base test class for Organizze API integration tests."""
import os
import unittest
from typing import Optional

import organizze_api
from organizze_api.rest import ApiException


class BaseIntegrationTest(unittest.TestCase):
    """Base class for integration tests with environment-based configuration."""

    api_client: Optional[organizze_api.ApiClient] = None
    configuration: Optional[organizze_api.Configuration] = None

    @classmethod
    def setUpClass(cls) -> None:
        """Set up API client with credentials from environment variables."""
        # Get credentials from environment
        email = os.getenv("ORGANIZZE_EMAIL")
        api_key = os.getenv("ORGANIZZE_API_KEY")
        user_agent = os.getenv("ORGANIZZE_USER_AGENT", f"organizze-api-sdk-python-test ({email})")

        if not email or not api_key:
            raise ValueError(
                "Missing required environment variables: ORGANIZZE_EMAIL and ORGANIZZE_API_KEY must be set. "
                "Please create a .env file or export these variables."
            )

        # Configure API client
        cls.configuration = organizze_api.Configuration(
            host="https://api.organizze.com.br/rest/v2",
            username=email,
            password=api_key
        )

        # Set required User-Agent header
        cls.configuration.api_key['userAgent'] = user_agent

        # Create API client
        cls.api_client = organizze_api.ApiClient(cls.configuration)

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up API client."""
        # ApiClient doesn't have a close method, just set to None
        cls.api_client = None

    def setUp(self) -> None:
        """Set up test case."""
        super().setUp()

    def tearDown(self) -> None:
        """Tear down test case."""
        super().tearDown()

    def assert_api_success(self, func, *args, **kwargs):
        """Helper to assert API call succeeds."""
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            self.fail(f"API call failed: {e}")

    def skip_if_env_not_set(self) -> None:
        """Skip test if environment variables are not set."""
        if not os.getenv("ORGANIZZE_EMAIL") or not os.getenv("ORGANIZZE_API_KEY"):
            self.skipTest("Environment variables ORGANIZZE_EMAIL and ORGANIZZE_API_KEY not set")
