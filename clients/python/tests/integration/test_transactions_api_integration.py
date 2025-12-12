"""Integration tests for Transactions API."""
import unittest
from datetime import date, datetime, timedelta

import organizze_api
from organizze_api.rest import ApiException

from .base_test import BaseIntegrationTest


class TestTransactionsApiIntegration(BaseIntegrationTest):
    """Integration tests for Transactions API endpoints."""

    def setUp(self) -> None:
        """Set up test case."""
        super().setUp()
        self.transactions_api = organizze_api.TransactionsApi(self.api_client)
        self.bank_accounts_api = organizze_api.BankAccountsApi(self.api_client)
        self.categories_api = organizze_api.CategoriesApi(self.api_client)

    def test_list_transactions(self) -> None:
        """Test listing transactions."""
        try:
            # Get transactions from the last 30 days
            end_date = date.today()
            start_date = end_date - timedelta(days=30)

            transactions = self.transactions_api.list_transactions(
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat()
            )
            self.assertIsNotNone(transactions, "Transactions list should not be None")
            self.assertIsInstance(transactions, list, "Transactions should be a list")

            print(f"✓ Successfully retrieved {len(transactions)} transaction(s) from last 30 days")

            if len(transactions) > 0:
                transaction = transactions[0]
                self.assertIsNotNone(transaction.id, "Transaction should have an ID")
                print(f"  Sample transaction ID: {transaction.id}")
        except ApiException as e:
            self.fail(f"Failed to list transactions: {e}")

    def test_read_transaction(self) -> None:
        """Test reading a specific transaction."""
        try:
            # Get recent transactions
            end_date = date.today()
            start_date = end_date - timedelta(days=30)
            transactions = self.transactions_api.list_transactions(
                start_date=start_date.isoformat(),
                end_date=end_date.isoformat()
            )

            if len(transactions) == 0:
                self.skipTest("No transactions available to test reading")
                return

            # Read the first transaction
            transaction_id = transactions[0].id
            transaction = self.transactions_api.read_transaction(transaction_id)

            self.assertIsNotNone(transaction, "Transaction should not be None")
            self.assertEqual(transaction.id, transaction_id, "Transaction ID should match")
            print(f"✓ Successfully read transaction with ID: {transaction_id}")
        except ApiException as e:
            self.fail(f"Failed to read transaction: {e}")

    def test_create_update_delete_transaction(self) -> None:
        """Test creating, updating, and deleting a transaction (full lifecycle)."""
        created_transaction_id = None

        try:
            # Get a bank account and category to use
            accounts = self.bank_accounts_api.list_bank_accounts()
            categories = self.categories_api.list_categories()

            if len(accounts) == 0:
                self.skipTest("No bank accounts available, cannot create transaction")
                return

            if len(categories) == 0:
                self.skipTest("No categories available, cannot create transaction")
                return

            account_id = accounts[0].id
            category_id = categories[0].id

            # Create a new transaction
            # Note: CreateTransactionRequest is a oneOf wrapper, use Transaction directly
            transaction_data = organizze_api.Transaction(
                description="Test Transaction SDK",
                var_date=date.today(),
                account_id=account_id,
                category_id=category_id,
                amount_cents=1000,  # R$ 10.00
                notes="Created by SDK integration tests"
            )
            new_transaction = organizze_api.CreateTransactionRequest(actual_instance=transaction_data)

            created_transaction = self.transactions_api.create_transaction(new_transaction)
            self.assertIsNotNone(created_transaction, "Created transaction should not be None")
            self.assertIsNotNone(created_transaction.id, "Created transaction should have an ID")
            created_transaction_id = created_transaction.id
            print(f"✓ Successfully created transaction with ID: {created_transaction_id}")

            # Update the transaction
            update_request = organizze_api.UpdateTransactionRequest(
                description="Test Transaction SDK Updated",
                amount_cents=2000,  # R$ 20.00
                notes="Updated by SDK integration tests"
            )
            updated_transaction = self.transactions_api.update_transaction(
                created_transaction_id,
                update_request
            )
            # Some API operations may return None on successful update
            if updated_transaction is not None:
                self.assertEqual(
                    updated_transaction.description,
                    "Test Transaction SDK Updated",
                    "Transaction description should be updated"
                )
                print(f"✓ Successfully updated transaction: {updated_transaction.description}")
            else:
                print(f"✓ Successfully updated transaction with ID: {created_transaction_id}")

            # Delete the transaction
            delete_request = organizze_api.DeleteTransactionRequest()
            self.transactions_api.delete_transaction(created_transaction_id, delete_request)
            print(f"✓ Successfully deleted transaction with ID: {created_transaction_id}")
            created_transaction_id = None  # Mark as deleted

        except ApiException as e:
            # Clean up if test fails
            if created_transaction_id:
                try:
                    delete_request = organizze_api.DeleteTransactionRequest()
                    self.transactions_api.delete_transaction(created_transaction_id, delete_request)
                    print(f"  Cleaned up transaction with ID: {created_transaction_id}")
                except ApiException:
                    pass
            self.fail(f"Transaction lifecycle test failed: {e}")


if __name__ == '__main__':
    unittest.main()
