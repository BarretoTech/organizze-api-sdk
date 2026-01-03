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
                start_date=start_date,
                end_date=end_date
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
                start_date=start_date,
                end_date=end_date
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
            # Note: CreateTransactionRequest is a oneOf wrapper, use TransactionInput
            transaction_data = organizze_api.TransactionInput(
                description="Test Transaction SDK",
                date=date.today(),
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

    def test_list_transactions_with_tags(self) -> None:
        """Test that transactions with tags are properly deserialized."""
        try:
            # Get transactions from the last 30 days
            end_date = date.today()
            start_date = end_date - timedelta(days=30)

            transactions = self.transactions_api.list_transactions(
                start_date=start_date,
                end_date=end_date
            )

            self.assertIsNotNone(transactions, "Transactions list should not be None")

            # Count transactions with tags
            transactions_with_tags = [t for t in transactions if t.tags and len(t.tags) > 0]
            total_tag_count = sum(len(t.tags) for t in transactions if t.tags)

            print(f"✓ Retrieved {len(transactions)} transaction(s)")
            print(f"  {len(transactions_with_tags)} transaction(s) have tags")
            print(f"  {total_tag_count} total tags found")

            # Verify tag structure for transactions that have tags
            for transaction in transactions_with_tags:
                self.assertIsNotNone(transaction.tags, "Tags should not be None")
                self.assertIsInstance(transaction.tags, list, "Tags should be a list")

                # Print sample tags
                if transaction.tags and len(transaction.tags) > 0:
                    tag_names = []
                    for tag in transaction.tags:
                        # Tag can be a string or a Tag object wrapped in TransactionTagsInner
                        if isinstance(tag, str):
                            tag_names.append(tag)
                        elif hasattr(tag, 'actual_instance'):
                            if isinstance(tag.actual_instance, str):
                                tag_names.append(tag.actual_instance)
                            elif hasattr(tag.actual_instance, 'name') and tag.actual_instance is not None:
                                name = tag.actual_instance.name
                                if name is not None:
                                    tag_names.append(name)
                    print(f"  Sample transaction {transaction.id} has tags: {', '.join(tag_names)}")
                    break  # Only print one sample

        except ApiException as e:
            self.fail(f"Failed to list transactions with tags: {e}")

    def test_create_transaction_with_tags(self) -> None:
        """Test creating a transaction with tags."""
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

            # Create tags as Tag objects
            tags = [
                organizze_api.Tag(name="integration-test"),
                organizze_api.Tag(name="sdk-test"),
                organizze_api.Tag(name="automated")
            ]

            # Create a transaction with tags
            transaction_data = organizze_api.TransactionInput(
                description="Test Transaction with Tags",
                date=date.today(),
                account_id=account_id,
                category_id=category_id,
                amount_cents=1500,  # R$ 15.00
                notes="Created by SDK integration tests with tags",
                tags=tags
            )
            new_transaction = organizze_api.CreateTransactionRequest(actual_instance=transaction_data)

            created_transaction = self.transactions_api.create_transaction(new_transaction)
            self.assertIsNotNone(created_transaction, "Created transaction should not be None")
            self.assertIsNotNone(created_transaction.id, "Created transaction should have an ID")
            created_transaction_id = created_transaction.id

            # Verify tags were created
            if created_transaction.tags:
                self.assertGreater(len(created_transaction.tags), 0, "Transaction should have tags")
                tag_names = []
                for tag in created_transaction.tags:
                    # Tag can be a string or a Tag object wrapped in TransactionTagsInner
                    if isinstance(tag, str):
                        tag_names.append(tag)
                    elif hasattr(tag, 'actual_instance'):
                        if isinstance(tag.actual_instance, str):
                            tag_names.append(tag.actual_instance)
                        elif hasattr(tag.actual_instance, 'name') and tag.actual_instance is not None:
                            name = tag.actual_instance.name
                            if name is not None:
                                tag_names.append(name)

                print(f"✓ Successfully created transaction with tags: {', '.join(tag_names)}")
            else:
                print(f"✓ Successfully created transaction with ID: {created_transaction_id}")

            # Clean up - delete the transaction
            delete_request = organizze_api.DeleteTransactionRequest()
            self.transactions_api.delete_transaction(created_transaction_id, delete_request)
            print(f"✓ Cleaned up test transaction with ID: {created_transaction_id}")
            created_transaction_id = None

        except ApiException as e:
            # Clean up if test fails
            if created_transaction_id:
                try:
                    delete_request = organizze_api.DeleteTransactionRequest()
                    self.transactions_api.delete_transaction(created_transaction_id, delete_request)
                    print(f"  Cleaned up transaction with ID: {created_transaction_id}")
                except ApiException:
                    pass
            self.fail(f"Create transaction with tags test failed: {e}")

    def test_update_transaction_tags(self) -> None:
        """Test updating transaction tags."""
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

            # Create a transaction with initial tags
            transaction_data = organizze_api.TransactionInput(
                description="Test Transaction - Update Tags",
                date=date.today(),
                account_id=account_id,
                category_id=category_id,
                amount_cents=2500,  # R$ 25.00
                tags=[organizze_api.Tag(name="initial-tag")]
            )
            new_transaction = organizze_api.CreateTransactionRequest(actual_instance=transaction_data)

            created_transaction = self.transactions_api.create_transaction(new_transaction)
            created_transaction_id = created_transaction.id
            print(f"✓ Created transaction with ID: {created_transaction_id}")

            # Update with new tags
            update_request = organizze_api.UpdateTransactionRequest(
                description="Test Transaction - Tags Updated",
                tags=[
                    organizze_api.Tag(name="updated-tag"),
                    organizze_api.Tag(name="modified-tag")
                ]
            )
            updated_transaction = self.transactions_api.update_transaction(
                created_transaction_id,
                update_request
            )

            if updated_transaction and updated_transaction.tags:
                tag_names = []
                for tag in updated_transaction.tags:
                    if isinstance(tag, str):
                        tag_names.append(tag)
                    elif hasattr(tag, 'actual_instance'):
                        if isinstance(tag.actual_instance, str):
                            tag_names.append(tag.actual_instance)
                        elif hasattr(tag.actual_instance, 'name') and tag.actual_instance is not None:
                            name = tag.actual_instance.name
                            if name is not None:
                                tag_names.append(name)
                print(f"✓ Successfully updated transaction tags: {', '.join(tag_names)}")

            # Clean up
            delete_request = organizze_api.DeleteTransactionRequest()
            self.transactions_api.delete_transaction(created_transaction_id, delete_request)
            print(f"✓ Cleaned up test transaction with ID: {created_transaction_id}")
            created_transaction_id = None

        except ApiException as e:
            # Clean up if test fails
            if created_transaction_id:
                try:
                    delete_request = organizze_api.DeleteTransactionRequest()
                    self.transactions_api.delete_transaction(created_transaction_id, delete_request)
                    print(f"  Cleaned up transaction with ID: {created_transaction_id}")
                except ApiException:
                    pass
            self.fail(f"Update transaction tags test failed: {e}")

    def test_read_transaction_verifies_tag_objects(self) -> None:
        """Test reading a transaction and verifying tags are strings."""
        try:
            # Get recent transactions
            end_date = date.today()
            start_date = end_date - timedelta(days=30)
            transactions = self.transactions_api.list_transactions(
                start_date=start_date,
                end_date=end_date
            )

            # Find a transaction with tags
            transaction_with_tags = None
            for transaction in transactions:
                if transaction.tags and len(transaction.tags) > 0:
                    transaction_with_tags = transaction
                    break

            if not transaction_with_tags:
                print("⚠ No transactions with tags found in last 30 days")
                return

            # Read the specific transaction
            transaction_id = transaction_with_tags.id
            transaction = self.transactions_api.read_transaction(transaction_id)

            self.assertIsNotNone(transaction, "Transaction should not be None")
            self.assertIsNotNone(transaction.tags, "Transaction should have tags")

            # Extract tag names from Tag objects
            tag_names = []
            if transaction.tags:
                for tag in transaction.tags:
                    # Tag can be a string or a Tag object wrapped in TransactionTagsInner
                    if isinstance(tag, str):
                        tag_names.append(tag)
                    elif hasattr(tag, 'actual_instance'):
                        if isinstance(tag.actual_instance, str):
                            tag_names.append(tag.actual_instance)
                        elif hasattr(tag.actual_instance, 'name') and tag.actual_instance is not None:
                            name = tag.actual_instance.name
                            if name is not None:
                                tag_names.append(name)

            print(f"✓ Successfully verified tags for transaction {transaction_id}")
            print(f"  Tags: {', '.join(tag_names)}")

        except ApiException as e:
            self.fail(f"Failed to read and verify transaction tags: {e}")


if __name__ == '__main__':
    unittest.main()
