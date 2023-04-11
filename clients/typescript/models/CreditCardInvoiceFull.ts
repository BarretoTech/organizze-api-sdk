/* tslint:disable */
/* eslint-disable */
/**
 * Organizze API
 * Specification for the Organizze API described in [https://github.com/organizze/api-doc](https://github.com/organizze/api-doc)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { Transaction } from './Transaction';
import {
    TransactionFromJSON,
    TransactionFromJSONTyped,
    TransactionToJSON,
} from './Transaction';

/**
 * 
 * @export
 * @interface CreditCardInvoiceFull
 */
export interface CreditCardInvoiceFull {
    /**
     * 
     * @type {number}
     * @memberof CreditCardInvoiceFull
     */
    id?: number;
    /**
     * 
     * @type {Date}
     * @memberof CreditCardInvoiceFull
     */
    date?: Date;
    /**
     * 
     * @type {Date}
     * @memberof CreditCardInvoiceFull
     */
    startingDate?: Date;
    /**
     * 
     * @type {Date}
     * @memberof CreditCardInvoiceFull
     */
    closingDate?: Date;
    /**
     * 
     * @type {number}
     * @memberof CreditCardInvoiceFull
     */
    amountCents?: number;
    /**
     * 
     * @type {number}
     * @memberof CreditCardInvoiceFull
     */
    paymentAmountCents?: number;
    /**
     * 
     * @type {number}
     * @memberof CreditCardInvoiceFull
     */
    balanceCents?: number;
    /**
     * 
     * @type {number}
     * @memberof CreditCardInvoiceFull
     */
    previousBalanceCents?: number;
    /**
     * 
     * @type {number}
     * @memberof CreditCardInvoiceFull
     */
    creditCardId?: number;
    /**
     * 
     * @type {Array<Transaction>}
     * @memberof CreditCardInvoiceFull
     */
    transactions?: Array<Transaction>;
    /**
     * 
     * @type {Array<Transaction>}
     * @memberof CreditCardInvoiceFull
     */
    payments?: Array<Transaction>;
}

/**
 * Check if a given object implements the CreditCardInvoiceFull interface.
 */
export function instanceOfCreditCardInvoiceFull(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function CreditCardInvoiceFullFromJSON(json: any): CreditCardInvoiceFull {
    return CreditCardInvoiceFullFromJSONTyped(json, false);
}

export function CreditCardInvoiceFullFromJSONTyped(json: any, ignoreDiscriminator: boolean): CreditCardInvoiceFull {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'date': !exists(json, 'date') ? undefined : (new Date(json['date'])),
        'startingDate': !exists(json, 'starting_date') ? undefined : (new Date(json['starting_date'])),
        'closingDate': !exists(json, 'closing_date') ? undefined : (new Date(json['closing_date'])),
        'amountCents': !exists(json, 'amount_cents') ? undefined : json['amount_cents'],
        'paymentAmountCents': !exists(json, 'payment_amount_cents') ? undefined : json['payment_amount_cents'],
        'balanceCents': !exists(json, 'balance_cents') ? undefined : json['balance_cents'],
        'previousBalanceCents': !exists(json, 'previous_balance_cents') ? undefined : json['previous_balance_cents'],
        'creditCardId': !exists(json, 'credit_card_id') ? undefined : json['credit_card_id'],
        'transactions': !exists(json, 'transactions') ? undefined : ((json['transactions'] as Array<any>).map(TransactionFromJSON)),
        'payments': !exists(json, 'payments') ? undefined : ((json['payments'] as Array<any>).map(TransactionFromJSON)),
    };
}

export function CreditCardInvoiceFullToJSON(value?: CreditCardInvoiceFull | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'date': value.date === undefined ? undefined : (value.date.toISOString().substr(0,10)),
        'starting_date': value.startingDate === undefined ? undefined : (value.startingDate.toISOString().substr(0,10)),
        'closing_date': value.closingDate === undefined ? undefined : (value.closingDate.toISOString().substr(0,10)),
        'amount_cents': value.amountCents,
        'payment_amount_cents': value.paymentAmountCents,
        'balance_cents': value.balanceCents,
        'previous_balance_cents': value.previousBalanceCents,
        'credit_card_id': value.creditCardId,
        'transactions': value.transactions === undefined ? undefined : ((value.transactions as Array<any>).map(TransactionToJSON)),
        'payments': value.payments === undefined ? undefined : ((value.payments as Array<any>).map(TransactionToJSON)),
    };
}

