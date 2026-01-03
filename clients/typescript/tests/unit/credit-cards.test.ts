import { describe, it } from 'node:test';
import assert from 'node:assert';
import { CreditCardsApi, Configuration } from '../../index';

describe('CreditCardsApi - Unit Tests', () => {
  it('should instantiate CreditCardsApi', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new CreditCardsApi(config);
    assert.ok(api, 'API instance should be created');
  });

  it('should have all required methods', () => {
    const config = new Configuration({
      basePath: 'https://api.organizze.com.br/rest/v2',
      username: 'test@example.com',
      password: 'test-token',
    });
    const api = new CreditCardsApi(config);

    assert.ok(typeof api.listCreditCards === 'function', 'should have listCreditCards method');
    assert.ok(typeof api.createCreditCard === 'function', 'should have createCreditCard method');
    assert.ok(typeof api.readCreditCard === 'function', 'should have readCreditCard method');
    assert.ok(typeof api.updateCreditCard === 'function', 'should have updateCreditCard method');
    assert.ok(typeof api.deleteCreditCard === 'function', 'should have deleteCreditCard method');
    assert.ok(typeof api.listCreditCardInvoices === 'function', 'should have listCreditCardInvoices method');
    assert.ok(typeof api.readCreditCardInvoice === 'function', 'should have readCreditCardInvoice method');
    assert.ok(typeof api.listCreditCardInvoicePayments === 'function', 'should have listCreditCardInvoicePayments method');
  });
});
