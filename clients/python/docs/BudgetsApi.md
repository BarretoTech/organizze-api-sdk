# organizze_api.BudgetsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_annual_budgets**](BudgetsApi.md#list_annual_budgets) | **GET** /budgets/{year} | Get Annual Budgets
[**list_current_month_budgets**](BudgetsApi.md#list_current_month_budgets) | **GET** /budgets | Get Current Month Budgets
[**list_monthly_budgets**](BudgetsApi.md#list_monthly_budgets) | **GET** /budgets/{year}/{month} | Get Monthly Budgets


# **list_annual_budgets**
> List[Budget] list_annual_budgets(year)

Get Annual Budgets

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.budget import Budget
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
    api_instance = organizze_api.BudgetsApi(api_client)
    year = 2018 # int | Year (YYYY)

    try:
        # Get Annual Budgets
        api_response = api_instance.list_annual_budgets(year)
        print("The response of BudgetsApi->list_annual_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->list_annual_budgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year (YYYY) | 

### Return type

[**List[Budget]**](Budget.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Budgets |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_current_month_budgets**
> List[Budget] list_current_month_budgets()

Get Current Month Budgets

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.budget import Budget
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
    api_instance = organizze_api.BudgetsApi(api_client)

    try:
        # Get Current Month Budgets
        api_response = api_instance.list_current_month_budgets()
        print("The response of BudgetsApi->list_current_month_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->list_current_month_budgets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Budget]**](Budget.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Budgets |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_monthly_budgets**
> List[Budget] list_monthly_budgets(year, month)

Get Monthly Budgets

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.budget import Budget
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
    api_instance = organizze_api.BudgetsApi(api_client)
    year = 2018 # int | Year (YYYY)
    month = 8 # int | Month (1-12 or 01-12)

    try:
        # Get Monthly Budgets
        api_response = api_instance.list_monthly_budgets(year, month)
        print("The response of BudgetsApi->list_monthly_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->list_monthly_budgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| Year (YYYY) | 
 **month** | **int**| Month (1-12 or 01-12) | 

### Return type

[**List[Budget]**](Budget.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Budgets |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

