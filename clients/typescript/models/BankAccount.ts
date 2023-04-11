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
/**
 * 
 * @export
 * @interface BankAccount
 */
export interface BankAccount {
    /**
     * ID of the Bank Account
     * @type {number}
     * @memberof BankAccount
     */
    id?: number;
    /**
     * Name of the Bank Account
     * @type {string}
     * @memberof BankAccount
     */
    name?: string;
    /**
     * 
     * @type {string}
     * @memberof BankAccount
     */
    institutionId?: string;
    /**
     * 
     * @type {string}
     * @memberof BankAccount
     */
    institutionName?: string;
    /**
     * 
     * @type {string}
     * @memberof BankAccount
     */
    description?: string | null;
    /**
     * 
     * @type {boolean}
     * @memberof BankAccount
     */
    archived?: boolean;
    /**
     * 
     * @type {string}
     * @memberof BankAccount
     */
    createdAt?: string;
    /**
     * 
     * @type {string}
     * @memberof BankAccount
     */
    updatedAt?: string;
    /**
     * 
     * @type {boolean}
     * @memberof BankAccount
     */
    _default?: boolean;
    /**
     * 
     * @type {string}
     * @memberof BankAccount
     */
    type?: BankAccountTypeEnum;
}

/**
* @export
* @enum {string}
*/
export enum BankAccountTypeEnum {
    Checking = 'checking',
    Savings = 'savings',
    Other = 'other'
}


/**
 * Check if a given object implements the BankAccount interface.
 */
export function instanceOfBankAccount(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function BankAccountFromJSON(json: any): BankAccount {
    return BankAccountFromJSONTyped(json, false);
}

export function BankAccountFromJSONTyped(json: any, ignoreDiscriminator: boolean): BankAccount {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'name': !exists(json, 'name') ? undefined : json['name'],
        'institutionId': !exists(json, 'institution_id') ? undefined : json['institution_id'],
        'institutionName': !exists(json, 'institution_name') ? undefined : json['institution_name'],
        'description': !exists(json, 'description') ? undefined : json['description'],
        'archived': !exists(json, 'archived') ? undefined : json['archived'],
        'createdAt': !exists(json, 'created_at') ? undefined : json['created_at'],
        'updatedAt': !exists(json, 'updated_at') ? undefined : json['updated_at'],
        '_default': !exists(json, 'default') ? undefined : json['default'],
        'type': !exists(json, 'type') ? undefined : json['type'],
    };
}

export function BankAccountToJSON(value?: BankAccount | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'institution_id': value.institutionId,
        'institution_name': value.institutionName,
        'description': value.description,
        'archived': value.archived,
        'created_at': value.createdAt,
        'updated_at': value.updatedAt,
        'default': value._default,
        'type': value.type,
    };
}

