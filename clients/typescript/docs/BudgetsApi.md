# BudgetsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAnnualBudgets**](BudgetsApi.md#listannualbudgets) | **GET** /budgets/{year} | Get Annual Budgets |
| [**listCurrentMonthBudgets**](BudgetsApi.md#listcurrentmonthbudgets) | **GET** /budgets | Get Current Month Budgets |
| [**listMonthlyBudgets**](BudgetsApi.md#listmonthlybudgets) | **GET** /budgets/{year}/{month} | Get Monthly Budgets |



## listAnnualBudgets

> Array&lt;Budget&gt; listAnnualBudgets(year)

Get Annual Budgets

### Example

```ts
import {
  Configuration,
  BudgetsApi,
} from '';
import type { ListAnnualBudgetsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BudgetsApi(config);

  const body = {
    // number | Year (YYYY)
    year: 2018,
  } satisfies ListAnnualBudgetsRequest;

  try {
    const data = await api.listAnnualBudgets(body);
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
| **year** | `number` | Year (YYYY) | [Defaults to `undefined`] |

### Return type

[**Array&lt;Budget&gt;**](Budget.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Budgets |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listCurrentMonthBudgets

> Array&lt;Budget&gt; listCurrentMonthBudgets()

Get Current Month Budgets

### Example

```ts
import {
  Configuration,
  BudgetsApi,
} from '';
import type { ListCurrentMonthBudgetsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BudgetsApi(config);

  try {
    const data = await api.listCurrentMonthBudgets();
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

[**Array&lt;Budget&gt;**](Budget.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Budgets |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listMonthlyBudgets

> Array&lt;Budget&gt; listMonthlyBudgets(year, month)

Get Monthly Budgets

### Example

```ts
import {
  Configuration,
  BudgetsApi,
} from '';
import type { ListMonthlyBudgetsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new BudgetsApi(config);

  const body = {
    // number | Year (YYYY)
    year: 2018,
    // number | Month (1-12 or 01-12)
    month: 8,
  } satisfies ListMonthlyBudgetsRequest;

  try {
    const data = await api.listMonthlyBudgets(body);
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
| **year** | `number` | Year (YYYY) | [Defaults to `undefined`] |
| **month** | `number` | Month (1-12 or 01-12) | [Defaults to `undefined`] |

### Return type

[**Array&lt;Budget&gt;**](Budget.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Budgets |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

