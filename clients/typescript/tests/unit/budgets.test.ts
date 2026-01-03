import { describe, it } from 'node:test';
import assert from 'node:assert';
import { BudgetsApi, Configuration } from '../../index';

describe('BudgetsApi - Unit Tests', () => {
  it('should instantiate BudgetsApi', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new BudgetsApi(config);
    assert.ok(api, 'API instance should be created');
  });

  it('should have all required methods', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new BudgetsApi(config);

    assert.ok(typeof api.listCurrentMonthBudgets === 'function', 'should have listCurrentMonthBudgets method');
    assert.ok(typeof api.listAnnualBudgets === 'function', 'should have listAnnualBudgets method');
    assert.ok(typeof api.listMonthlyBudgets === 'function', 'should have listMonthlyBudgets method');
  });
});
