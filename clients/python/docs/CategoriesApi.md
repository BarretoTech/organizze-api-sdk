# organizze_api.CategoriesApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category**](CategoriesApi.md#create_category) | **POST** /categories | Create Category
[**delete_category**](CategoriesApi.md#delete_category) | **DELETE** /categories/{categoryID} | Delete Category
[**list_categories**](CategoriesApi.md#list_categories) | **GET** /categories | List Categories
[**read_category**](CategoriesApi.md#read_category) | **GET** /categories/{categoryID} | Read Category
[**update_category**](CategoriesApi.md#update_category) | **PUT** /categories/{categoryID} | Update Category


# **create_category**
> Category create_category(category_input)

Create Category

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.category import Category
from organizze_api.models.category_input import CategoryInput
from organizze_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.organizze.com.br/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = organizze_api.Configuration(
    host = "https://api.organizze.com.br/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = organizze_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
with organizze_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizze_api.CategoriesApi(api_client)
    category_input = organizze_api.CategoryInput() # CategoryInput | 

    try:
        # Create Category
        api_response = api_instance.create_category(category_input)
        print("The response of CategoriesApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_input** | [**CategoryInput**](CategoryInput.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Category |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category**
> Category delete_category(category_id)

Delete Category

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.category import Category
from organizze_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.organizze.com.br/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = organizze_api.Configuration(
    host = "https://api.organizze.com.br/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = organizze_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
with organizze_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizze_api.CategoriesApi(api_client)
    category_id = 1 # int | Category ID

    try:
        # Delete Category
        api_response = api_instance.delete_category(category_id)
        print("The response of CategoriesApi->delete_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID | 

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories**
> List[Category] list_categories()

List Categories

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.category import Category
from organizze_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.organizze.com.br/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = organizze_api.Configuration(
    host = "https://api.organizze.com.br/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = organizze_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
with organizze_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizze_api.CategoriesApi(api_client)

    try:
        # List Categories
        api_response = api_instance.list_categories()
        print("The response of CategoriesApi->list_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->list_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Category]**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Categories |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_category**
> Category read_category(category_id)

Read Category

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.category import Category
from organizze_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.organizze.com.br/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = organizze_api.Configuration(
    host = "https://api.organizze.com.br/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = organizze_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
with organizze_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizze_api.CategoriesApi(api_client)
    category_id = 1 # int | Category ID

    try:
        # Read Category
        api_response = api_instance.read_category(category_id)
        print("The response of CategoriesApi->read_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->read_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID | 

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category**
> Category update_category(category_id, category_input)

Update Category

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.category import Category
from organizze_api.models.category_input import CategoryInput
from organizze_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.organizze.com.br/rest/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = organizze_api.Configuration(
    host = "https://api.organizze.com.br/rest/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = organizze_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
with organizze_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organizze_api.CategoriesApi(api_client)
    category_id = 1 # int | Category ID
    category_input = organizze_api.CategoryInput() # CategoryInput | 

    try:
        # Update Category
        api_response = api_instance.update_category(category_id, category_input)
        print("The response of CategoriesApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoriesApi->update_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category ID | 
 **category_input** | [**CategoryInput**](CategoryInput.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

