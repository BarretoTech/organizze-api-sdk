# organizze_api.BankAccountsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bank_account**](BankAccountsApi.md#create_bank_account) | **POST** /accounts | Create Bank Account
[**delete_bank_account**](BankAccountsApi.md#delete_bank_account) | **DELETE** /accounts/{bankAccountID} | Delete Bank Account
[**list_bank_accounts**](BankAccountsApi.md#list_bank_accounts) | **GET** /accounts | List Bank Accounts
[**read_bank_account**](BankAccountsApi.md#read_bank_account) | **GET** /accounts/{bankAccountID} | Read Account
[**update_bank_account**](BankAccountsApi.md#update_bank_account) | **PUT** /accounts/{bankAccountID} | Update Bank Account


# **create_bank_account**
> BankAccount create_bank_account(bank_account_input)

Create Bank Account

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.bank_account import BankAccount
from organizze_api.models.bank_account_input import BankAccountInput
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
    api_instance = organizze_api.BankAccountsApi(api_client)
    bank_account_input = organizze_api.BankAccountInput() # BankAccountInput | 

    try:
        # Create Bank Account
        api_response = api_instance.create_bank_account(bank_account_input)
        print("The response of BankAccountsApi->create_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->create_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_input** | [**BankAccountInput**](BankAccountInput.md)|  | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Bank Account |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bank_account**
> BankAccount delete_bank_account(bank_account_id)

Delete Bank Account

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.bank_account import BankAccount
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
    api_instance = organizze_api.BankAccountsApi(api_client)
    bank_account_id = 1 # int | Bank Account ID

    try:
        # Delete Bank Account
        api_response = api_instance.delete_bank_account(bank_account_id)
        print("The response of BankAccountsApi->delete_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->delete_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**| Bank Account ID | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bank Account |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_bank_accounts**
> List[BankAccount] list_bank_accounts()

List Bank Accounts

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.bank_account import BankAccount
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
    api_instance = organizze_api.BankAccountsApi(api_client)

    try:
        # List Bank Accounts
        api_response = api_instance.list_bank_accounts()
        print("The response of BankAccountsApi->list_bank_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->list_bank_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BankAccount]**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Bank Accounts |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_bank_account**
> BankAccount read_bank_account(bank_account_id)

Read Account

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.bank_account import BankAccount
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
    api_instance = organizze_api.BankAccountsApi(api_client)
    bank_account_id = 1 # int | Bank Account ID

    try:
        # Read Account
        api_response = api_instance.read_bank_account(bank_account_id)
        print("The response of BankAccountsApi->read_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->read_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**| Bank Account ID | 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bank Account |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_account**
> BankAccount update_bank_account(bank_account_id, bank_account_input=bank_account_input)

Update Bank Account

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.bank_account import BankAccount
from organizze_api.models.bank_account_input import BankAccountInput
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
    api_instance = organizze_api.BankAccountsApi(api_client)
    bank_account_id = 1 # int | Bank Account ID
    bank_account_input = organizze_api.BankAccountInput() # BankAccountInput |  (optional)

    try:
        # Update Bank Account
        api_response = api_instance.update_bank_account(bank_account_id, bank_account_input=bank_account_input)
        print("The response of BankAccountsApi->update_bank_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankAccountsApi->update_bank_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_id** | **int**| Bank Account ID | 
 **bank_account_input** | [**BankAccountInput**](BankAccountInput.md)|  | [optional] 

### Return type

[**BankAccount**](BankAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bank Account |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

