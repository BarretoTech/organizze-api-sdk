"""Pytest configuration and fixtures."""
import os
from pathlib import Path

import pytest


def pytest_configure(config):
    """Configure pytest."""
    # Load .env file if it exists
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, _, value = line.partition("=")
                    os.environ[key.strip()] = value.strip()

    # Register markers
    config.addinivalue_line(
        "markers", "integration: Integration tests that make real API calls"
    )
    config.addinivalue_line(
        "markers", "unit: Unit tests that don't make API calls"
    )


@pytest.fixture(scope="session")
def api_credentials():
    """Provide API credentials from environment."""
    email = os.getenv("ORGANIZZE_EMAIL")
    api_key = os.getenv("ORGANIZZE_API_KEY")

    if not email or not api_key:
        pytest.skip(
            "Missing ORGANIZZE_EMAIL or ORGANIZZE_API_KEY environment variables. "
            "Please create a .env file with your credentials."
        )

    return {
        "email": email,
        "api_key": api_key,
        "user_agent": os.getenv("ORGANIZZE_USER_AGENT", f"organizze-api-sdk-python-test ({email})")
    }
