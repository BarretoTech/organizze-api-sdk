import { describe, it } from 'node:test';
import assert from 'node:assert';
import { TransactionsApi } from '../../index';
import { getTestConfig } from '../setup';

describe('TransactionsApi - Integration Tests', () => {
  it('should list transactions', async () => {
    const config = getTestConfig();
    const api = new TransactionsApi(config);

    const transactions = await api.listTransactions({
      startDate: '2024-01-01',
      endDate: '2024-12-31',
    });
    assert.ok(Array.isArray(transactions), 'should return an array');
  });

  it('should list transactions with date filtering', async () => {
    const config = getTestConfig();
    const api = new TransactionsApi(config);

    const startDate = '2024-01-01';
    const endDate = '2024-01-31';

    const transactions = await api.listTransactions({
      startDate,
      endDate,
    });

    assert.ok(Array.isArray(transactions), 'should return an array');

    // Verify all transactions are within the date range
    for (const transaction of transactions) {
      assert.ok(transaction.date >= startDate, 'transaction date should be >= start date');
      assert.ok(transaction.date <= endDate, 'transaction date should be <= end date');
    }
  });
});
