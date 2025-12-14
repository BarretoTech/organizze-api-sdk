# TransactionsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTransaction**](TransactionsApi.md#createtransactionoperation) | **POST** /transactions | Create Transaction |
| [**deleteTransaction**](TransactionsApi.md#deletetransactionoperation) | **DELETE** /transactions/{transactionID} | Delete Transaction |
| [**listTransactions**](TransactionsApi.md#listtransactions) | **GET** /transactions | List Transactions |
| [**readTransaction**](TransactionsApi.md#readtransaction) | **GET** /transactions/{transactionID} | Read Transaction |
| [**updateTransaction**](TransactionsApi.md#updatetransactionoperation) | **PUT** /transactions/{transactionID} | Update Transaction |



## createTransaction

> Transaction createTransaction(createTransactionRequest)

Create Transaction

### Example

```ts
import {
  Configuration,
  TransactionsApi,
} from '';
import type { CreateTransactionOperationRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new TransactionsApi(config);

  const body = {
    // CreateTransactionRequest
    createTransactionRequest: ...,
  } satisfies CreateTransactionOperationRequest;

  try {
    const data = await api.createTransaction(body);
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
| **createTransactionRequest** | [CreateTransactionRequest](CreateTransactionRequest.md) |  | |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Transaction |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteTransaction

> Transaction deleteTransaction(transactionID, deleteTransactionRequest)

Delete Transaction

### Example

```ts
import {
  Configuration,
  TransactionsApi,
} from '';
import type { DeleteTransactionOperationRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new TransactionsApi(config);

  const body = {
    // number | Transaction ID
    transactionID: 1,
    // DeleteTransactionRequest
    deleteTransactionRequest: ...,
  } satisfies DeleteTransactionOperationRequest;

  try {
    const data = await api.deleteTransaction(body);
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
| **transactionID** | `number` | Transaction ID | [Defaults to `undefined`] |
| **deleteTransactionRequest** | [DeleteTransactionRequest](DeleteTransactionRequest.md) |  | |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listTransactions

> Array&lt;Transaction&gt; listTransactions(startDate, endDate, accountId)

List Transactions

### Example

```ts
import {
  Configuration,
  TransactionsApi,
} from '';
import type { ListTransactionsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new TransactionsApi(config);

  const body = {
    // Date | ISO8601 Date with the start period for filtering (optional)
    startDate: 2015-09-01,
    // Date | ISO8601 Date with the end period for filtering (optional)
    endDate: 2015-10-01,
    // number | Account ID for filtering (optional)
    accountId: 1,
  } satisfies ListTransactionsRequest;

  try {
    const data = await api.listTransactions(body);
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
| **startDate** | `Date` | ISO8601 Date with the start period for filtering | [Optional] [Defaults to `undefined`] |
| **endDate** | `Date` | ISO8601 Date with the end period for filtering | [Optional] [Defaults to `undefined`] |
| **accountId** | `number` | Account ID for filtering | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;Transaction&gt;**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Transactions |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readTransaction

> Transaction readTransaction(transactionID)

Read Transaction

### Example

```ts
import {
  Configuration,
  TransactionsApi,
} from '';
import type { ReadTransactionRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new TransactionsApi(config);

  const body = {
    // number | Transaction ID
    transactionID: 1,
  } satisfies ReadTransactionRequest;

  try {
    const data = await api.readTransaction(body);
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
| **transactionID** | `number` | Transaction ID | [Defaults to `undefined`] |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateTransaction

> Transaction updateTransaction(transactionID, updateTransactionRequest)

Update Transaction

### Example

```ts
import {
  Configuration,
  TransactionsApi,
} from '';
import type { UpdateTransactionOperationRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new TransactionsApi(config);

  const body = {
    // number | Transaction ID
    transactionID: 1,
    // UpdateTransactionRequest
    updateTransactionRequest: ...,
  } satisfies UpdateTransactionOperationRequest;

  try {
    const data = await api.updateTransaction(body);
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
| **transactionID** | `number` | Transaction ID | [Defaults to `undefined`] |
| **updateTransactionRequest** | [UpdateTransactionRequest](UpdateTransactionRequest.md) |  | |

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Transaction |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

