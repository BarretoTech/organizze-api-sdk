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


import * as runtime from '../runtime';
import type {
  FailedAuthentication,
  NotFound,
  Transaction,
} from '../models';
import {
    FailedAuthenticationFromJSON,
    FailedAuthenticationToJSON,
    NotFoundFromJSON,
    NotFoundToJSON,
    TransactionFromJSON,
    TransactionToJSON,
} from '../models';

export interface CreateTransactionRequest {
    transaction?: Transaction;
}

export interface DeleteTransactionRequest {
    transactionID: number;
}

export interface ListTransactionsRequest {
    startDate?: Date;
    endDate?: Date;
    accountId?: number;
}

export interface ReadTransactionRequest {
    transactionID: number;
}

export interface UpdateTransactionRequest {
    transactionID: number;
    transaction?: Transaction;
}

/**
 * 
 */
export class TransactionsApi extends runtime.BaseAPI {

    /**
     * Create Transaction
     */
    async createTransactionRaw(requestParameters: CreateTransactionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Transaction>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/transactions`,
            method: 'POST',
            headers: headerParameters,
            query: queryParameters,
            body: TransactionToJSON(requestParameters.transaction),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => TransactionFromJSON(jsonValue));
    }

    /**
     * Create Transaction
     */
    async createTransaction(requestParameters: CreateTransactionRequest = {}, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Transaction> {
        const response = await this.createTransactionRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Delete Transaction
     */
    async deleteTransactionRaw(requestParameters: DeleteTransactionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Transaction>> {
        if (requestParameters.transactionID === null || requestParameters.transactionID === undefined) {
            throw new runtime.RequiredError('transactionID','Required parameter requestParameters.transactionID was null or undefined when calling deleteTransaction.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/transactions/{transactionID}`.replace(`{${"transactionID"}}`, encodeURIComponent(String(requestParameters.transactionID))),
            method: 'DELETE',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => TransactionFromJSON(jsonValue));
    }

    /**
     * Delete Transaction
     */
    async deleteTransaction(requestParameters: DeleteTransactionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Transaction> {
        const response = await this.deleteTransactionRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * List Transactions
     */
    async listTransactionsRaw(requestParameters: ListTransactionsRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Array<Transaction>>> {
        const queryParameters: any = {};

        if (requestParameters.startDate !== undefined) {
            queryParameters['start_date'] = (requestParameters.startDate as any).toISOString().substr(0,10);
        }

        if (requestParameters.endDate !== undefined) {
            queryParameters['end_date'] = (requestParameters.endDate as any).toISOString().substr(0,10);
        }

        if (requestParameters.accountId !== undefined) {
            queryParameters['account_id'] = requestParameters.accountId;
        }

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/transactions`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(TransactionFromJSON));
    }

    /**
     * List Transactions
     */
    async listTransactions(requestParameters: ListTransactionsRequest = {}, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Array<Transaction>> {
        const response = await this.listTransactionsRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Read Transaction
     */
    async readTransactionRaw(requestParameters: ReadTransactionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Transaction>> {
        if (requestParameters.transactionID === null || requestParameters.transactionID === undefined) {
            throw new runtime.RequiredError('transactionID','Required parameter requestParameters.transactionID was null or undefined when calling readTransaction.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/transactions/{transactionID}`.replace(`{${"transactionID"}}`, encodeURIComponent(String(requestParameters.transactionID))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => TransactionFromJSON(jsonValue));
    }

    /**
     * Read Transaction
     */
    async readTransaction(requestParameters: ReadTransactionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Transaction> {
        const response = await this.readTransactionRaw(requestParameters, initOverrides);
        return await response.value();
    }

    /**
     * Update Transaction
     */
    async updateTransactionRaw(requestParameters: UpdateTransactionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Transaction>> {
        if (requestParameters.transactionID === null || requestParameters.transactionID === undefined) {
            throw new runtime.RequiredError('transactionID','Required parameter requestParameters.transactionID was null or undefined when calling updateTransaction.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        headerParameters['Content-Type'] = 'application/json';

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/transactions/{transactionID}`.replace(`{${"transactionID"}}`, encodeURIComponent(String(requestParameters.transactionID))),
            method: 'PUT',
            headers: headerParameters,
            query: queryParameters,
            body: TransactionToJSON(requestParameters.transaction),
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => TransactionFromJSON(jsonValue));
    }

    /**
     * Update Transaction
     */
    async updateTransaction(requestParameters: UpdateTransactionRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Transaction> {
        const response = await this.updateTransactionRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
