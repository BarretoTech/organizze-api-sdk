"""Integration tests for Credit Cards API."""
import unittest

import organizze_api
from organizze_api.rest import ApiException

from .base_test import BaseIntegrationTest


class TestCreditCardsApiIntegration(BaseIntegrationTest):
    """Integration tests for Credit Cards API endpoints."""

    def setUp(self) -> None:
        """Set up test case."""
        super().setUp()
        self.credit_cards_api = organizze_api.CreditCardsApi(self.api_client)

    def test_list_credit_cards(self) -> None:
        """Test listing credit cards."""
        try:
            cards = self.credit_cards_api.list_credit_cards()
            self.assertIsNotNone(cards, "Credit cards list should not be None")
            self.assertIsInstance(cards, list, "Credit cards should be a list")

            print(f"✓ Successfully retrieved {len(cards)} credit card(s)")

            if len(cards) > 0:
                card = cards[0]
                self.assertIsNotNone(card.id, "Credit card should have an ID")
                self.assertIsNotNone(card.name, "Credit card should have a name")
                print(f"  Sample card: {card.name}")
        except ApiException as e:
            self.fail(f"Failed to list credit cards: {e}")

    def test_read_credit_card(self) -> None:
        """Test reading a specific credit card."""
        try:
            cards = self.credit_cards_api.list_credit_cards()
            self.assertIsNotNone(cards, "Credit cards list should not be None")

            if len(cards) == 0:
                self.skipTest("No credit cards available to test reading")
                return

            card_id = cards[0].id
            card = self.credit_cards_api.read_credit_card(card_id)

            self.assertIsNotNone(card, "Credit card should not be None")
            self.assertEqual(card.id, card_id, "Credit card ID should match")
            self.assertIsNotNone(card.name, "Credit card should have a name")
            print(f"✓ Successfully read credit card: {card.name}")
        except ApiException as e:
            self.fail(f"Failed to read credit card: {e}")

    def test_list_credit_card_invoices(self) -> None:
        """Test listing credit card invoices."""
        try:
            cards = self.credit_cards_api.list_credit_cards()
            self.assertIsNotNone(cards, "Credit cards list should not be None")

            if len(cards) == 0:
                self.skipTest("No credit cards available to test invoices")
                return

            card_id = cards[0].id
            invoices = self.credit_cards_api.list_credit_card_invoices(card_id)

            self.assertIsNotNone(invoices, "Invoices list should not be None")
            self.assertIsInstance(invoices, list, "Invoices should be a list")
            print(f"✓ Successfully retrieved {len(invoices)} invoice(s) for card ID {card_id}")

            if len(invoices) > 0:
                invoice = invoices[0]
                self.assertIsNotNone(invoice.id, "Invoice should have an ID")
                print(f"  Sample invoice ID: {invoice.id}")
        except ApiException as e:
            self.fail(f"Failed to list credit card invoices: {e}")

    def test_read_credit_card_invoice(self) -> None:
        """Test reading a specific credit card invoice."""
        try:
            cards = self.credit_cards_api.list_credit_cards()
            if len(cards) == 0:
                self.skipTest("No credit cards available")
                return

            card_id = cards[0].id
            invoices = self.credit_cards_api.list_credit_card_invoices(card_id)

            if len(invoices) == 0:
                self.skipTest("No invoices available to test reading")
                return

            invoice_id = invoices[0].id
            invoice = self.credit_cards_api.read_credit_card_invoice(card_id, invoice_id)

            self.assertIsNotNone(invoice, "Invoice should not be None")
            self.assertEqual(invoice.id, invoice_id, "Invoice ID should match")
            print(f"✓ Successfully read invoice with ID: {invoice_id}")
        except ApiException as e:
            self.fail(f"Failed to read credit card invoice: {e}")

    def test_create_update_delete_credit_card(self) -> None:
        """Test creating, updating, and deleting a credit card (full lifecycle)."""
        created_card_id = None

        try:
            # Create a new credit card
            new_card = organizze_api.CreditCardInput(
                name="Test Card SDK",
                card_network="visa",
                closing_day=15,
                due_day=25,
                limit_cents=500000  # R$ 5000.00
            )

            created_card = self.credit_cards_api.create_credit_card(new_card)
            self.assertIsNotNone(created_card, "Created card should not be None")
            self.assertIsNotNone(created_card.id, "Created card should have an ID")
            created_card_id = created_card.id
            print(f"✓ Successfully created credit card with ID: {created_card_id}")

            # Update the card
            update_data = organizze_api.CreditCardInput(
                name="Test Card SDK Updated",
                card_network="visa",
                closing_day=15,
                due_day=25,
                limit_cents=750000  # R$ 7500.00
            )
            updated_card = self.credit_cards_api.update_credit_card(
                created_card_id,
                update_data
            )
            # Some API operations may return None on successful update
            if updated_card is not None:
                self.assertEqual(
                    updated_card.name,
                    "Test Card SDK Updated",
                    "Card name should be updated"
                )
                print(f"✓ Successfully updated credit card: {updated_card.name}")
            else:
                print(f"✓ Successfully updated credit card with ID: {created_card_id}")

            # Delete the card
            self.credit_cards_api.delete_credit_card(created_card_id)
            print(f"✓ Successfully deleted credit card with ID: {created_card_id}")
            created_card_id = None  # Mark as deleted

        except ApiException as e:
            # Clean up if test fails
            if created_card_id:
                try:
                    self.credit_cards_api.delete_credit_card(created_card_id)
                    print(f"  Cleaned up credit card with ID: {created_card_id}")
                except ApiException:
                    pass
            self.fail(f"Credit card lifecycle test failed: {e}")


if __name__ == '__main__':
    unittest.main()
