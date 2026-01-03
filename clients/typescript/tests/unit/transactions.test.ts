import { describe, it } from 'node:test';
import assert from 'node:assert';
import { TransactionsApi, Configuration } from '../../index';

describe('TransactionsApi - Unit Tests', () => {
  it('should instantiate TransactionsApi', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new TransactionsApi(config);
    assert.ok(api, 'API instance should be created');
  });

  it('should have all required methods', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new TransactionsApi(config);

    assert.ok(typeof api.listTransactions === 'function', 'should have listTransactions method');
    assert.ok(typeof api.createTransaction === 'function', 'should have createTransaction method');
    assert.ok(typeof api.readTransaction === 'function', 'should have readTransaction method');
    assert.ok(typeof api.updateTransaction === 'function', 'should have updateTransaction method');
    assert.ok(typeof api.deleteTransaction === 'function', 'should have deleteTransaction method');
  });
});
