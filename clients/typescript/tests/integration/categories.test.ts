import { describe, it } from 'node:test';
import assert from 'node:assert';
import { CategoriesApi } from '../../index';
import { getTestConfig } from '../setup';

describe('CategoriesApi - Integration Tests', () => {
  it('should list categories', async () => {
    const config = getTestConfig();
    const api = new CategoriesApi(config);

    const categories = await api.listCategories();
    assert.ok(Array.isArray(categories), 'should return an array');
  });

  it('should read a category by ID', async (t) => {
    const config = getTestConfig();
    const api = new CategoriesApi(config);

    const categories = await api.listCategories();
    if (categories.length === 0) {
      t.skip('No categories available for testing');
      return;
    }

    const firstCategory = categories[0];
    const category = await api.readCategory({ categoryID: firstCategory.id });

    assert.ok(category, 'should return a category');
    assert.strictEqual(category.id, firstCategory.id, 'should return the correct category');
  });
});
