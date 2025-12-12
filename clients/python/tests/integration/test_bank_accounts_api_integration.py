"""Integration tests for Bank Accounts API."""
import unittest

import organizze_api
from organizze_api.rest import ApiException

from .base_test import BaseIntegrationTest


class TestBankAccountsApiIntegration(BaseIntegrationTest):
    """Integration tests for Bank Accounts API endpoints."""

    def setUp(self) -> None:
        """Set up test case."""
        super().setUp()
        self.bank_accounts_api = organizze_api.BankAccountsApi(self.api_client)

    def test_list_bank_accounts(self) -> None:
        """Test listing bank accounts."""
        try:
            accounts = self.bank_accounts_api.list_bank_accounts()
            self.assertIsNotNone(accounts, "Bank accounts list should not be None")
            self.assertIsInstance(accounts, list, "Bank accounts should be a list")

            if len(accounts) > 0:
                account = accounts[0]
                self.assertIsNotNone(account.id, "Account should have an ID")
                self.assertIsNotNone(account.name, "Account should have a name")
                print(f"✓ Successfully retrieved {len(accounts)} bank account(s)")
                print(f"  Sample account: {account.name}")
        except ApiException as e:
            self.fail(f"Failed to list bank accounts: {e}")

    def test_read_bank_account(self) -> None:
        """Test reading a specific bank account."""
        try:
            # First get the list of accounts to get a valid account ID
            accounts = self.bank_accounts_api.list_bank_accounts()
            self.assertIsNotNone(accounts, "Bank accounts list should not be None")

            if len(accounts) == 0:
                self.skipTest("No bank accounts available to test reading")
                return

            # Read the first account
            account_id = accounts[0].id
            account = self.bank_accounts_api.read_bank_account(account_id)

            self.assertIsNotNone(account, "Account should not be None")
            self.assertEqual(account.id, account_id, "Account ID should match")
            self.assertIsNotNone(account.name, "Account should have a name")
            print(f"✓ Successfully read bank account: {account.name}")
        except ApiException as e:
            self.fail(f"Failed to read bank account: {e}")

    def test_create_update_delete_bank_account(self) -> None:
        """Test creating, updating, and deleting a bank account (full lifecycle)."""
        created_account_id = None

        try:
            # Create a new bank account
            # Note: type field should be omitted or set to valid values like "other" or "bank"
            new_account = organizze_api.BankAccount(
                name="Test Account SDK",
                description="Created by SDK integration tests",
                type="other"  # Valid values: "other", "bank", etc.
            )

            created_account = self.bank_accounts_api.create_bank_account(new_account)
            self.assertIsNotNone(created_account, "Created account should not be None")
            self.assertIsNotNone(created_account.id, "Created account should have an ID")
            created_account_id = created_account.id
            print(f"✓ Successfully created bank account with ID: {created_account_id}")

            # Update the account
            created_account.name = "Test Account SDK Updated"
            created_account.description = "Updated by SDK integration tests"
            updated_account = self.bank_accounts_api.update_bank_account(
                created_account_id,
                created_account
            )
            # Some API operations may return None on successful update
            if updated_account is not None:
                self.assertEqual(
                    updated_account.name,
                    "Test Account SDK Updated",
                    "Account name should be updated"
                )
                print(f"✓ Successfully updated bank account: {updated_account.name}")
            else:
                print(f"✓ Successfully updated bank account with ID: {created_account_id}")

            # Delete the account
            self.bank_accounts_api.delete_bank_account(created_account_id)
            print(f"✓ Successfully deleted bank account with ID: {created_account_id}")
            created_account_id = None  # Mark as deleted

        except ApiException as e:
            # Clean up if test fails
            if created_account_id:
                try:
                    self.bank_accounts_api.delete_bank_account(created_account_id)
                    print(f"  Cleaned up bank account with ID: {created_account_id}")
                except ApiException:
                    pass
            self.fail(f"Bank account lifecycle test failed: {e}")


if __name__ == '__main__':
    unittest.main()
