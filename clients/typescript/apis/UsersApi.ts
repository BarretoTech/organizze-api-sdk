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
  User,
} from '../models';
import {
    FailedAuthenticationFromJSON,
    FailedAuthenticationToJSON,
    NotFoundFromJSON,
    NotFoundToJSON,
    UserFromJSON,
    UserToJSON,
} from '../models';

export interface ReadUserRequest {
    userID: number;
}

/**
 * 
 */
export class UsersApi extends runtime.BaseAPI {

    /**
     * List Users
     */
    async listUsersRaw(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<Array<User>>> {
        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/users`,
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => jsonValue.map(UserFromJSON));
    }

    /**
     * List Users
     */
    async listUsers(initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<Array<User>> {
        const response = await this.listUsersRaw(initOverrides);
        return await response.value();
    }

    /**
     * Read User
     */
    async readUserRaw(requestParameters: ReadUserRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<runtime.ApiResponse<User>> {
        if (requestParameters.userID === null || requestParameters.userID === undefined) {
            throw new runtime.RequiredError('userID','Required parameter requestParameters.userID was null or undefined when calling readUser.');
        }

        const queryParameters: any = {};

        const headerParameters: runtime.HTTPHeaders = {};

        if (this.configuration && (this.configuration.username !== undefined || this.configuration.password !== undefined)) {
            headerParameters["Authorization"] = "Basic " + btoa(this.configuration.username + ":" + this.configuration.password);
        }
        const response = await this.request({
            path: `/users/{userID}`.replace(`{${"userID"}}`, encodeURIComponent(String(requestParameters.userID))),
            method: 'GET',
            headers: headerParameters,
            query: queryParameters,
        }, initOverrides);

        return new runtime.JSONApiResponse(response, (jsonValue) => UserFromJSON(jsonValue));
    }

    /**
     * Read User
     */
    async readUser(requestParameters: ReadUserRequest, initOverrides?: RequestInit | runtime.InitOverrideFunction): Promise<User> {
        const response = await this.readUserRaw(requestParameters, initOverrides);
        return await response.value();
    }

}
