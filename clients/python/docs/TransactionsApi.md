# organizze_api.TransactionsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /transactions | Create Transaction
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /transactions/{transactionID} | Delete Transaction
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /transactions | List Transactions
[**read_transaction**](TransactionsApi.md#read_transaction) | **GET** /transactions/{transactionID} | Read Transaction
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /transactions/{transactionID} | Update Transaction


# **create_transaction**
> Transaction create_transaction(create_transaction_request)

Create Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.create_transaction_request import CreateTransactionRequest
from organizze_api.models.transaction import Transaction
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
    api_instance = organizze_api.TransactionsApi(api_client)
    create_transaction_request = organizze_api.CreateTransactionRequest() # CreateTransactionRequest | 

    try:
        # Create Transaction
        api_response = api_instance.create_transaction(create_transaction_request)
        print("The response of TransactionsApi->create_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transaction_request** | [**CreateTransactionRequest**](CreateTransactionRequest.md)|  | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transaction |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction**
> Transaction delete_transaction(transaction_id, delete_transaction_request)

Delete Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.delete_transaction_request import DeleteTransactionRequest
from organizze_api.models.transaction import Transaction
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
    api_instance = organizze_api.TransactionsApi(api_client)
    transaction_id = 1 # int | Transaction ID
    delete_transaction_request = organizze_api.DeleteTransactionRequest() # DeleteTransactionRequest | 

    try:
        # Delete Transaction
        api_response = api_instance.delete_transaction(transaction_id, delete_transaction_request)
        print("The response of TransactionsApi->delete_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| Transaction ID | 
 **delete_transaction_request** | [**DeleteTransactionRequest**](DeleteTransactionRequest.md)|  | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> List[Transaction] list_transactions(start_date=start_date, end_date=end_date, account_id=account_id)

List Transactions

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.transaction import Transaction
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
    api_instance = organizze_api.TransactionsApi(api_client)
    start_date = '2015-09-01' # date | ISO8601 Date with the start period for filtering (optional)
    end_date = '2015-10-01' # date | ISO8601 Date with the end period for filtering (optional)
    account_id = 1 # int | Account ID for filtering (optional)

    try:
        # List Transactions
        api_response = api_instance.list_transactions(start_date=start_date, end_date=end_date, account_id=account_id)
        print("The response of TransactionsApi->list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**| ISO8601 Date with the start period for filtering | [optional] 
 **end_date** | **date**| ISO8601 Date with the end period for filtering | [optional] 
 **account_id** | **int**| Account ID for filtering | [optional] 

### Return type

[**List[Transaction]**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Transactions |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_transaction**
> Transaction read_transaction(transaction_id)

Read Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.transaction import Transaction
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
    api_instance = organizze_api.TransactionsApi(api_client)
    transaction_id = 1 # int | Transaction ID

    try:
        # Read Transaction
        api_response = api_instance.read_transaction(transaction_id)
        print("The response of TransactionsApi->read_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->read_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| Transaction ID | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> Transaction update_transaction(transaction_id, update_transaction_request)

Update Transaction

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.transaction import Transaction
from organizze_api.models.update_transaction_request import UpdateTransactionRequest
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
    api_instance = organizze_api.TransactionsApi(api_client)
    transaction_id = 1 # int | Transaction ID
    update_transaction_request = organizze_api.UpdateTransactionRequest() # UpdateTransactionRequest | 

    try:
        # Update Transaction
        api_response = api_instance.update_transaction(transaction_id, update_transaction_request)
        print("The response of TransactionsApi->update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| Transaction ID | 
 **update_transaction_request** | [**UpdateTransactionRequest**](UpdateTransactionRequest.md)|  | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

