# BankAccountsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBankAccount**](BankAccountsApi.md#createbankaccount) | **POST** /accounts | Create Bank Account |
| [**deleteBankAccount**](BankAccountsApi.md#deletebankaccount) | **DELETE** /accounts/{bankAccountID} | Delete Bank Account |
| [**listBankAccounts**](BankAccountsApi.md#listbankaccounts) | **GET** /accounts | List Bank Accounts |
| [**readBankAccount**](BankAccountsApi.md#readbankaccount) | **GET** /accounts/{bankAccountID} | Read Account |
| [**updateBankAccount**](BankAccountsApi.md#updatebankaccount) | **PUT** /accounts/{bankAccountID} | Update Bank Account |



## createBankAccount

> BankAccount createBankAccount(bankAccountInput)

Create Bank Account

### Example

```ts
import {
  Configuration,
  BankAccountsApi,
} from '';
import type { CreateBankAccountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BankAccountsApi(config);

  const body = {
    // BankAccountInput
    bankAccountInput: ...,
  } satisfies CreateBankAccountRequest;

  try {
    const data = await api.createBankAccount(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bankAccountInput** | [BankAccountInput](BankAccountInput.md) |  | |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Bank Account |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteBankAccount

> BankAccount deleteBankAccount(bankAccountID)

Delete Bank Account

### Example

```ts
import {
  Configuration,
  BankAccountsApi,
} from '';
import type { DeleteBankAccountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BankAccountsApi(config);

  const body = {
    // number | Bank Account ID
    bankAccountID: 1,
  } satisfies DeleteBankAccountRequest;

  try {
    const data = await api.deleteBankAccount(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bankAccountID** | `number` | Bank Account ID | [Defaults to `undefined`] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank Account |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listBankAccounts

> Array&lt;BankAccount&gt; listBankAccounts()

List Bank Accounts

### Example

```ts
import {
  Configuration,
  BankAccountsApi,
} from '';
import type { ListBankAccountsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BankAccountsApi(config);

  try {
    const data = await api.listBankAccounts();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Array&lt;BankAccount&gt;**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Bank Accounts |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readBankAccount

> BankAccount readBankAccount(bankAccountID)

Read Account

### Example

```ts
import {
  Configuration,
  BankAccountsApi,
} from '';
import type { ReadBankAccountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BankAccountsApi(config);

  const body = {
    // number | Bank Account ID
    bankAccountID: 1,
  } satisfies ReadBankAccountRequest;

  try {
    const data = await api.readBankAccount(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bankAccountID** | `number` | Bank Account ID | [Defaults to `undefined`] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank Account |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateBankAccount

> BankAccount updateBankAccount(bankAccountID, bankAccountInput)

Update Bank Account

### Example

```ts
import {
  Configuration,
  BankAccountsApi,
} from '';
import type { UpdateBankAccountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BankAccountsApi(config);

  const body = {
    // number | Bank Account ID
    bankAccountID: 1,
    // BankAccountInput (optional)
    bankAccountInput: ...,
  } satisfies UpdateBankAccountRequest;

  try {
    const data = await api.updateBankAccount(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bankAccountID** | `number` | Bank Account ID | [Defaults to `undefined`] |
| **bankAccountInput** | [BankAccountInput](BankAccountInput.md) |  | [Optional] |

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bank Account |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

