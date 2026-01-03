import { describe, it } from 'node:test';
import assert from 'node:assert';
import { BankAccountsApi, Configuration } from '../../index';

describe('BankAccountsApi - Unit Tests', () => {
  it('should instantiate BankAccountsApi', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new BankAccountsApi(config);
    assert.ok(api, 'API instance should be created');
  });

  it('should have all required methods', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new BankAccountsApi(config);

    assert.ok(typeof api.listBankAccounts === 'function', 'should have listBankAccounts method');
    assert.ok(typeof api.createBankAccount === 'function', 'should have createBankAccount method');
    assert.ok(typeof api.readBankAccount === 'function', 'should have readBankAccount method');
    assert.ok(typeof api.updateBankAccount === 'function', 'should have updateBankAccount method');
    assert.ok(typeof api.deleteBankAccount === 'function', 'should have deleteBankAccount method');
  });
});
