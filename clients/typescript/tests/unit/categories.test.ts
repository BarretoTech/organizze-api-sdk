import { describe, it } from 'node:test';
import assert from 'node:assert';
import { CategoriesApi, Configuration } from '../../index';

describe('CategoriesApi - Unit Tests', () => {
  it('should instantiate CategoriesApi', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new CategoriesApi(config);
    assert.ok(api, 'API instance should be created');
  });

  it('should have all required methods', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new CategoriesApi(config);

    assert.ok(typeof api.listCategories === 'function', 'should have listCategories method');
    assert.ok(typeof api.createCategory === 'function', 'should have createCategory method');
    assert.ok(typeof api.readCategory === 'function', 'should have readCategory method');
    assert.ok(typeof api.updateCategory === 'function', 'should have updateCategory method');
    assert.ok(typeof api.deleteCategory === 'function', 'should have deleteCategory method');
  });
});
