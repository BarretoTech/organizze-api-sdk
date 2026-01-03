import { describe, it } from 'node:test';
import assert from 'node:assert';
import { BankAccountsApi } from '../../index';
import { getTestConfig } from '../setup';

describe('BankAccountsApi - Integration Tests', () => {
  it('should list bank accounts', async () => {
    const config = getTestConfig();
    const api = new BankAccountsApi(config);

    const accounts = await api.listBankAccounts();
    assert.ok(Array.isArray(accounts), 'should return an array');
  });

  it('should read a bank account by ID', async (t) => {
    const config = getTestConfig();
    const api = new BankAccountsApi(config);

    // First get the list to get a valid ID
    const accounts = await api.listBankAccounts();
    if (accounts.length === 0) {
      t.skip('No bank accounts available for testing');
      return;
    }

    const firstAccount = accounts[0];
    const account = await api.readBankAccount({ bankAccountID: firstAccount.id });

    assert.ok(account, 'should return an account');
    assert.strictEqual(account.id, firstAccount.id, 'should return the correct account');
  });
});
