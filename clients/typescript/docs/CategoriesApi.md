# CategoriesApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCategory**](CategoriesApi.md#createcategory) | **POST** /categories | Create Category |
| [**deleteCategory**](CategoriesApi.md#deletecategory) | **DELETE** /categories/{categoryID} | Delete Category |
| [**listCategories**](CategoriesApi.md#listcategories) | **GET** /categories | List Categories |
| [**readCategory**](CategoriesApi.md#readcategory) | **GET** /categories/{categoryID} | Read Category |
| [**updateCategory**](CategoriesApi.md#updatecategory) | **PUT** /categories/{categoryID} | Update Category |



## createCategory

> Category createCategory(categoryInput)

Create Category

### Example

```ts
import {
  Configuration,
  CategoriesApi,
} from '';
import type { CreateCategoryRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CategoriesApi(config);

  const body = {
    // CategoryInput
    categoryInput: ...,
  } satisfies CreateCategoryRequest;

  try {
    const data = await api.createCategory(body);
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
| **categoryInput** | [CategoryInput](CategoryInput.md) |  | |

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Category |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteCategory

> Category deleteCategory(categoryID)

Delete Category

### Example

```ts
import {
  Configuration,
  CategoriesApi,
} from '';
import type { DeleteCategoryRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CategoriesApi(config);

  const body = {
    // number | Category ID
    categoryID: 1,
  } satisfies DeleteCategoryRequest;

  try {
    const data = await api.deleteCategory(body);
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
| **categoryID** | `number` | Category ID | [Defaults to `undefined`] |

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Category |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listCategories

> Array&lt;Category&gt; listCategories()

List Categories

### Example

```ts
import {
  Configuration,
  CategoriesApi,
} from '';
import type { ListCategoriesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CategoriesApi(config);

  try {
    const data = await api.listCategories();
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

[**Array&lt;Category&gt;**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Categories |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readCategory

> Category readCategory(categoryID)

Read Category

### Example

```ts
import {
  Configuration,
  CategoriesApi,
} from '';
import type { ReadCategoryRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CategoriesApi(config);

  const body = {
    // number | Category ID
    categoryID: 1,
  } satisfies ReadCategoryRequest;

  try {
    const data = await api.readCategory(body);
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
| **categoryID** | `number` | Category ID | [Defaults to `undefined`] |

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Category |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateCategory

> Category updateCategory(categoryID, categoryInput)

Update Category

### Example

```ts
import {
  Configuration,
  CategoriesApi,
} from '';
import type { UpdateCategoryRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new CategoriesApi(config);

  const body = {
    // number | Category ID
    categoryID: 1,
    // CategoryInput
    categoryInput: ...,
  } satisfies UpdateCategoryRequest;

  try {
    const data = await api.updateCategory(body);
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
| **categoryID** | `number` | Category ID | [Defaults to `undefined`] |
| **categoryInput** | [CategoryInput](CategoryInput.md) |  | |

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/plain`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Category |  -  |
| **400** | Bad request (e.g., missing User-Agent header) |  -  |
| **401** | Authentication issues |  -  |
| **404** | Item Not Found |  -  |
| **422** | Validation errors |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

