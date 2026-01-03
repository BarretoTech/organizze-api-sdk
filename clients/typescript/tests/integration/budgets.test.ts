import { describe, it } from 'node:test';
import assert from 'node:assert';
import { BudgetsApi } from '../../index';
import { getTestConfig } from '../setup';

describe('BudgetsApi - Integration Tests', () => {
  it('should list current month budgets', async () => {
    const config = getTestConfig();
    const api = new BudgetsApi(config);

    const budgets = await api.listCurrentMonthBudgets();
    assert.ok(Array.isArray(budgets), 'should return an array');
  });

  it('should list annual budgets', async () => {
    const config = getTestConfig();
    const api = new BudgetsApi(config);

    const year = new Date().getFullYear();
    const budgets = await api.listAnnualBudgets({ year });
    assert.ok(Array.isArray(budgets), 'should return an array');
  });

  it('should list monthly budgets', async () => {
    const config = getTestConfig();
    const api = new BudgetsApi(config);

    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth() + 1;

    const budgets = await api.listMonthlyBudgets({ year, month });
    assert.ok(Array.isArray(budgets), 'should return an array');
  });
});
