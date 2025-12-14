# CreditCardsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCreditCard**](CreditCardsApi.md#createcreditcard) | **POST** /credit_cards | Create Credit Card |
| [**deleteCreditCard**](CreditCardsApi.md#deletecreditcard) | **DELETE** /credit_cards/{creditCardID} | Delete Credit Card |
| [**listCreditCardInvoicePayments**](CreditCardsApi.md#listcreditcardinvoicepayments) | **GET** /credit_cards/{creditCardID}/invoices/{creditCardInvoiceID}/payments | List Credit Card Invoice Payments |
| [**listCreditCardInvoices**](CreditCardsApi.md#listcreditcardinvoices) | **GET** /credit_cards/{creditCardID}/invoices | List Credit Card Invoices |
| [**listCreditCards**](CreditCardsApi.md#listcreditcards) | **GET** /credit_cards | List Credit Cards |
| [**readCreditCard**](CreditCardsApi.md#readcreditcard) | **GET** /credit_cards/{creditCardID} | Read Credit Card |
| [**readCreditCardInvoice**](CreditCardsApi.md#readcreditcardinvoice) | **GET** /credit_cards/{creditCardID}/invoices/{creditCardInvoiceID} | Read Credit Card Invoice |
| [**updateCreditCard**](CreditCardsApi.md#updatecreditcard) | **PUT** /credit_cards/{creditCardID} | Update Credit Card |



## createCreditCard

> CreditCard createCreditCard(creditCardInput)

Create Credit Card

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { CreateCreditCardRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  const body = {
    // CreditCardInput
    creditCardInput: ...,
  } satisfies CreateCreditCardRequest;

  try {
    const data = await api.createCreditCard(body);
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
| **creditCardInput** | [CreditCardInput](CreditCardInput.md) |  | |

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Credit Card |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteCreditCard

> CreditCard deleteCreditCard(creditCardID)

Delete Credit Card

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { DeleteCreditCardRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  const body = {
    // number | Credit Card ID
    creditCardID: 1,
  } satisfies DeleteCreditCardRequest;

  try {
    const data = await api.deleteCreditCard(body);
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
| **creditCardID** | `number` | Credit Card ID | [Defaults to `undefined`] |

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credit Card |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listCreditCardInvoicePayments

> Array&lt;Transaction&gt; listCreditCardInvoicePayments(creditCardID, creditCardInvoiceID)

List Credit Card Invoice Payments

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { ListCreditCardInvoicePaymentsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  const body = {
    // number | Credit Card ID
    creditCardID: 1,
    // number | Credit Card Invoice ID
    creditCardInvoiceID: 1,
  } satisfies ListCreditCardInvoicePaymentsRequest;

  try {
    const data = await api.listCreditCardInvoicePayments(body);
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
| **creditCardID** | `number` | Credit Card ID | [Defaults to `undefined`] |
| **creditCardInvoiceID** | `number` | Credit Card Invoice ID | [Defaults to `undefined`] |

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
| **200** | List of Credit Card Invoice Payments |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listCreditCardInvoices

> Array&lt;CreditCardInvoice&gt; listCreditCardInvoices(creditCardID)

List Credit Card Invoices

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { ListCreditCardInvoicesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  const body = {
    // number | Credit Card ID
    creditCardID: 1,
  } satisfies ListCreditCardInvoicesRequest;

  try {
    const data = await api.listCreditCardInvoices(body);
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
| **creditCardID** | `number` | Credit Card ID | [Defaults to `undefined`] |

### Return type

[**Array&lt;CreditCardInvoice&gt;**](CreditCardInvoice.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Credit Card Invoices |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listCreditCards

> Array&lt;CreditCard&gt; listCreditCards()

List Credit Cards

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { ListCreditCardsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  try {
    const data = await api.listCreditCards();
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

[**Array&lt;CreditCard&gt;**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Credit Cards |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readCreditCard

> CreditCard readCreditCard(creditCardID)

Read Credit Card

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { ReadCreditCardRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  const body = {
    // number | Credit Card ID
    creditCardID: 1,
  } satisfies ReadCreditCardRequest;

  try {
    const data = await api.readCreditCard(body);
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
| **creditCardID** | `number` | Credit Card ID | [Defaults to `undefined`] |

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credit Card |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readCreditCardInvoice

> CreditCardInvoiceFull readCreditCardInvoice(creditCardID, creditCardInvoiceID)

Read Credit Card Invoice

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { ReadCreditCardInvoiceRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  const body = {
    // number | Credit Card ID
    creditCardID: 1,
    // number | Credit Card Invoice ID
    creditCardInvoiceID: 1,
  } satisfies ReadCreditCardInvoiceRequest;

  try {
    const data = await api.readCreditCardInvoice(body);
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
| **creditCardID** | `number` | Credit Card ID | [Defaults to `undefined`] |
| **creditCardInvoiceID** | `number` | Credit Card Invoice ID | [Defaults to `undefined`] |

### Return type

[**CreditCardInvoiceFull**](CreditCardInvoiceFull.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credit Card Invoice |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateCreditCard

> CreditCard updateCreditCard(creditCardID, creditCardInput)

Update Credit Card

### Example

```ts
import {
  Configuration,
  CreditCardsApi,
} from '';
import type { UpdateCreditCardRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CreditCardsApi(config);

  const body = {
    // number | Credit Card ID
    creditCardID: 1,
    // CreditCardInput
    creditCardInput: ...,
  } satisfies UpdateCreditCardRequest;

  try {
    const data = await api.updateCreditCard(body);
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
| **creditCardID** | `number` | Credit Card ID | [Defaults to `undefined`] |
| **creditCardInput** | [CreditCardInput](CreditCardInput.md) |  | |

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credit Card |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

