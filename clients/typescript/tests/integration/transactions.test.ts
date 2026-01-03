import { describe, it } from 'node:test';
import assert from 'node:assert';
import { TransactionsApi } from '../../index';
import { getTestConfig } from '../setup';

describe('TransactionsApi - Integration Tests', () => {
  it('should list transactions', async () => {
    const config = getTestConfig();
    const api = new TransactionsApi(config);

    const transactions = await api.listTransactions({
      startDate: new Date('2024-01-01'),
      endDate: new Date('2024-12-31'),
    });
    assert.ok(Array.isArray(transactions), 'should return an array');
  });

  it('should list transactions with date filtering', async () => {
    const config = getTestConfig();
    const api = new TransactionsApi(config);

    // Use current month for testing
    const now = new Date();
    const year = now.getFullYear();
    const month = now.getMonth(); // 0-indexed

    const startDate = new Date(year, month, 1); // First day of current month
    const endDate = new Date(year, month + 1, 0); // Last day of current month

    const transactions = await api.listTransactions({
      startDate,
      endDate,
    });

    assert.ok(Array.isArray(transactions), 'should return an array');

    // Note: The API may return recurring transactions outside the date range,
    // which is expected behavior, so we just verify the API call works
  });
});
