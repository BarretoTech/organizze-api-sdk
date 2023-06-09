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
 * @interface Category
 */
export interface Category {
    /**
     * 
     * @type {number}
     * @memberof Category
     */
    id?: number;
    /**
     * 
     * @type {string}
     * @memberof Category
     */
    name?: string;
    /**
     * 
     * @type {string}
     * @memberof Category
     */
    color?: string;
    /**
     * 
     * @type {string}
     * @memberof Category
     */
    groupId?: string;
    /**
     * 
     * @type {boolean}
     * @memberof Category
     */
    fixed?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof Category
     */
    available?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof Category
     */
    essential?: boolean;
    /**
     * 
     * @type {number}
     * @memberof Category
     */
    parentId?: number | null;
}

/**
 * Check if a given object implements the Category interface.
 */
export function instanceOfCategory(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function CategoryFromJSON(json: any): Category {
    return CategoryFromJSONTyped(json, false);
}

export function CategoryFromJSONTyped(json: any, ignoreDiscriminator: boolean): Category {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'name': !exists(json, 'name') ? undefined : json['name'],
        'color': !exists(json, 'color') ? undefined : json['color'],
        'groupId': !exists(json, 'group_id') ? undefined : json['group_id'],
        'fixed': !exists(json, 'fixed') ? undefined : json['fixed'],
        'available': !exists(json, 'available') ? undefined : json['available'],
        'essential': !exists(json, 'essential') ? undefined : json['essential'],
        'parentId': !exists(json, 'parent_id') ? undefined : json['parent_id'],
    };
}

export function CategoryToJSON(value?: Category | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'color': value.color,
        'group_id': value.groupId,
        'fixed': value.fixed,
        'available': value.available,
        'essential': value.essential,
        'parent_id': value.parentId,
    };
}

