import { describe, it } from 'node:test';
import assert from 'node:assert';
import { CreditCardsApi } from '../../index';
import { getTestConfig } from '../setup';

describe('CreditCardsApi - Integration Tests', () => {
  it('should list credit cards', async () => {
    const config = getTestConfig();
    const api = new CreditCardsApi(config);

    const cards = await api.listCreditCards();
    assert.ok(Array.isArray(cards), 'should return an array');
  });

  it('should list credit card invoices', async (t) => {
    const config = getTestConfig();
    const api = new CreditCardsApi(config);

    const cards = await api.listCreditCards();
    if (cards.length === 0) {
      t.skip('No credit cards available for testing');
      return;
    }

    const firstCard = cards[0];
    const invoices = await api.listCreditCardInvoices({
      creditCardID: firstCard.id,
      startDate: new Date('2024-01-01'),
      endDate: new Date('2024-12-31'),
    });

    assert.ok(Array.isArray(invoices), 'should return an array of invoices');
  });
});
