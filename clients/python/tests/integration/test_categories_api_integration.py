"""Integration tests for Categories API."""
import unittest

import organizze_api
from organizze_api.rest import ApiException

from .base_test import BaseIntegrationTest


class TestCategoriesApiIntegration(BaseIntegrationTest):
    """Integration tests for Categories API endpoints."""

    def setUp(self) -> None:
        """Set up test case."""
        super().setUp()
        self.categories_api = organizze_api.CategoriesApi(self.api_client)

    def test_list_categories(self) -> None:
        """Test listing categories."""
        try:
            categories = self.categories_api.list_categories()
            self.assertIsNotNone(categories, "Categories list should not be None")
            self.assertIsInstance(categories, list, "Categories should be a list")

            if len(categories) > 0:
                category = categories[0]
                self.assertIsNotNone(category.id, "Category should have an ID")
                self.assertIsNotNone(category.name, "Category should have a name")
                print(f"✓ Successfully retrieved {len(categories)} category(ies)")
                print(f"  Sample category: {category.name}")
        except ApiException as e:
            self.fail(f"Failed to list categories: {e}")

    def test_read_category(self) -> None:
        """Test reading a specific category."""
        try:
            # First get the list of categories to get a valid category ID
            categories = self.categories_api.list_categories()
            self.assertIsNotNone(categories, "Categories list should not be None")

            if len(categories) == 0:
                self.skipTest("No categories available to test reading")
                return

            # Read the first category
            category_id = categories[0].id
            category = self.categories_api.read_category(category_id)

            self.assertIsNotNone(category, "Category should not be None")
            self.assertEqual(category.id, category_id, "Category ID should match")
            self.assertIsNotNone(category.name, "Category should have a name")
            print(f"✓ Successfully read category: {category.name}")
        except ApiException as e:
            self.fail(f"Failed to read category: {e}")

    def test_create_update_delete_category(self) -> None:
        """Test creating, updating, and deleting a category (full lifecycle)."""
        created_category_id = None

        try:
            # Create a new category
            # Color format: lowercase hex without # (e.g., "ff5733")
            new_category = organizze_api.CategoryInput(
                name="Test Category SDK",
                color="ff5733"
            )

            created_category = self.categories_api.create_category(new_category)
            self.assertIsNotNone(created_category, "Created category should not be None")
            self.assertIsNotNone(created_category.id, "Created category should have an ID")
            created_category_id = created_category.id
            print(f"✓ Successfully created category with ID: {created_category_id}")

            # Update the category
            update_data = organizze_api.CategoryInput(
                name="Test Category SDK Updated",
                color="ffd5ff"
            )
            updated_category = self.categories_api.update_category(
                created_category_id,
                update_data
            )
            # Some API operations may return None on successful update
            if updated_category is not None:
                self.assertEqual(
                    updated_category.name,
                    "Test Category SDK Updated",
                    "Category name should be updated"
                )
                print(f"✓ Successfully updated category: {updated_category.name}")
            else:
                print(f"✓ Successfully updated category with ID: {created_category_id}")

            # Delete the category
            self.categories_api.delete_category(created_category_id)
            print(f"✓ Successfully deleted category with ID: {created_category_id}")
            created_category_id = None  # Mark as deleted

        except ApiException as e:
            # Clean up if test fails
            if created_category_id:
                try:
                    self.categories_api.delete_category(created_category_id)
                    print(f"  Cleaned up category with ID: {created_category_id}")
                except ApiException:
                    pass
            self.fail(f"Category lifecycle test failed: {e}")


if __name__ == '__main__':
    unittest.main()
