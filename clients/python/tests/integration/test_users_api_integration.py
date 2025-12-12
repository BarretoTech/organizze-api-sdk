"""Integration tests for Users API."""
import unittest

import organizze_api
from organizze_api.rest import ApiException

from .base_test import BaseIntegrationTest


class TestUsersApiIntegration(BaseIntegrationTest):
    """Integration tests for Users API endpoints."""

    def setUp(self) -> None:
        """Set up test case."""
        super().setUp()
        self.users_api = organizze_api.UsersApi(self.api_client)

    def test_list_users(self) -> None:
        """Test listing users."""
        try:
            users = self.users_api.list_users()
            self.assertIsNotNone(users, "Users list should not be None")
            self.assertIsInstance(users, list, "Users should be a list")
            if len(users) > 0:
                user = users[0]
                self.assertIsNotNone(user.id, "User should have an ID")
                self.assertIsNotNone(user.email, "User should have an email")
                print(f"✓ Successfully retrieved {len(users)} user(s)")
        except ApiException as e:
            self.fail(f"Failed to list users: {e}")

    def test_read_user(self) -> None:
        """Test reading a specific user."""
        try:
            # First get the list of users to get a valid user ID
            users = self.users_api.list_users()
            self.assertIsNotNone(users, "Users list should not be None")
            self.assertGreater(len(users), 0, "Should have at least one user")

            # Read the first user
            user_id = users[0].id
            user = self.users_api.read_user(user_id)

            self.assertIsNotNone(user, "User should not be None")
            self.assertEqual(user.id, user_id, "User ID should match")
            self.assertIsNotNone(user.email, "User should have an email")
            print(f"✓ Successfully read user: {user.email}")
        except ApiException as e:
            self.fail(f"Failed to read user: {e}")


if __name__ == '__main__':
    unittest.main()
