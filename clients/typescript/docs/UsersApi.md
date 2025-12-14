# UsersApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listUsers**](UsersApi.md#listusers) | **GET** /users | List Users |
| [**readUser**](UsersApi.md#readuser) | **GET** /users/{userID} | Read User |



## listUsers

> Array&lt;User&gt; listUsers()

List Users

### Example

```ts
import {
  Configuration,
  UsersApi,
} from '';
import type { ListUsersRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new UsersApi(config);

  try {
    const data = await api.listUsers();
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

[**Array&lt;User&gt;**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Users |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## readUser

> User readUser(userID)

Read User

### Example

```ts
import {
  Configuration,
  UsersApi,
} from '';
import type { ReadUserRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure HTTP basic authorization: basicAuth
    username: "YOUR USERNAME",
    password: "YOUR PASSWORD",
    // To configure API key authorization: userAgent
    apiKey: "YOUR API KEY",
  });
  const api = new UsersApi(config);

  const body = {
    // number | User ID
    userID: 1,
  } satisfies ReadUserRequest;

  try {
    const data = await api.readUser(body);
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
| **userID** | `number` | User ID | [Defaults to `undefined`] |

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User |  -  |
| **404** | Item Not Found |  -  |
| **401** | Authentication issues |  -  |
| **0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

