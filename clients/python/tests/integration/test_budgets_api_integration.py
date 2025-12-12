"""Integration tests for Budgets API."""
import unittest
from datetime import date

import organizze_api
from organizze_api.rest import ApiException

from .base_test import BaseIntegrationTest


class TestBudgetsApiIntegration(BaseIntegrationTest):
    """Integration tests for Budgets API endpoints."""

    def setUp(self) -> None:
        """Set up test case."""
        super().setUp()
        self.budgets_api = organizze_api.BudgetsApi(self.api_client)

    def test_list_current_month_budgets(self) -> None:
        """Test listing current month budgets."""
        try:
            budgets = self.budgets_api.list_current_month_budgets()
            self.assertIsNotNone(budgets, "Budgets list should not be None")
            self.assertIsInstance(budgets, list, "Budgets should be a list")
            print(f"✓ Successfully retrieved {len(budgets)} budget(s) for current month")

            if len(budgets) > 0:
                budget = budgets[0]
                self.assertIsNotNone(budget.category_id, "Budget should have a category ID")
                print(f"  Sample budget - Category ID: {budget.category_id}, Amount: {budget.amount_in_cents}")
        except ApiException as e:
            self.fail(f"Failed to list current month budgets: {e}")

    def test_list_monthly_budgets(self) -> None:
        """Test listing budgets for a specific month."""
        try:
            today = date.today()
            year = today.year
            month = today.month

            budgets = self.budgets_api.list_monthly_budgets(year, month)
            self.assertIsNotNone(budgets, "Budgets list should not be None")
            self.assertIsInstance(budgets, list, "Budgets should be a list")
            print(f"✓ Successfully retrieved {len(budgets)} budget(s) for {year}/{month:02d}")
        except ApiException as e:
            self.fail(f"Failed to list monthly budgets: {e}")

    def test_list_annual_budgets(self) -> None:
        """Test listing annual budgets."""
        try:
            year = date.today().year
            budgets = self.budgets_api.list_annual_budgets(year)
            self.assertIsNotNone(budgets, "Budgets list should not be None")
            self.assertIsInstance(budgets, list, "Budgets should be a list")
            print(f"✓ Successfully retrieved {len(budgets)} budget(s) for year {year}")
        except ApiException as e:
            self.fail(f"Failed to list annual budgets: {e}")


if __name__ == '__main__':
    unittest.main()
