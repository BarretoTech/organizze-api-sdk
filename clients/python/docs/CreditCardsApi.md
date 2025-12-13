# organizze_api.CreditCardsApi

All URIs are relative to *https://api.organizze.com.br/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit_card**](CreditCardsApi.md#create_credit_card) | **POST** /credit_cards | Create Credit Card
[**delete_credit_card**](CreditCardsApi.md#delete_credit_card) | **DELETE** /credit_cards/{creditCardID} | Delete Credit Card
[**list_credit_card_invoice_payments**](CreditCardsApi.md#list_credit_card_invoice_payments) | **GET** /credit_cards/{creditCardID}/invoices/{creditCardInvoiceID}/payments | List Credit Card Invoice Payments
[**list_credit_card_invoices**](CreditCardsApi.md#list_credit_card_invoices) | **GET** /credit_cards/{creditCardID}/invoices | List Credit Card Invoices
[**list_credit_cards**](CreditCardsApi.md#list_credit_cards) | **GET** /credit_cards | List Credit Cards
[**read_credit_card**](CreditCardsApi.md#read_credit_card) | **GET** /credit_cards/{creditCardID} | Read Credit Card
[**read_credit_card_invoice**](CreditCardsApi.md#read_credit_card_invoice) | **GET** /credit_cards/{creditCardID}/invoices/{creditCardInvoiceID} | Read Credit Card Invoice
[**update_credit_card**](CreditCardsApi.md#update_credit_card) | **PUT** /credit_cards/{creditCardID} | Update Credit Card


# **create_credit_card**
> CreditCard create_credit_card(credit_card_input)

Create Credit Card

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.credit_card import CreditCard
from organizze_api.models.credit_card_input import CreditCardInput
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
    api_instance = organizze_api.CreditCardsApi(api_client)
    credit_card_input = organizze_api.CreditCardInput() # CreditCardInput | 

    try:
        # Create Credit Card
        api_response = api_instance.create_credit_card(credit_card_input)
        print("The response of CreditCardsApi->create_credit_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->create_credit_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_input** | [**CreditCardInput**](CreditCardInput.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Credit Card |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credit_card**
> CreditCard delete_credit_card(credit_card_id)

Delete Credit Card

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.credit_card import CreditCard
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
    api_instance = organizze_api.CreditCardsApi(api_client)
    credit_card_id = 1 # int | Credit Card ID

    try:
        # Delete Credit Card
        api_response = api_instance.delete_credit_card(credit_card_id)
        print("The response of CreditCardsApi->delete_credit_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->delete_credit_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_id** | **int**| Credit Card ID | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Card |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_card_invoice_payments**
> List[Transaction] list_credit_card_invoice_payments(credit_card_id, credit_card_invoice_id)

List Credit Card Invoice Payments

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
    api_instance = organizze_api.CreditCardsApi(api_client)
    credit_card_id = 1 # int | Credit Card ID
    credit_card_invoice_id = 1 # int | Credit Card Invoice ID

    try:
        # List Credit Card Invoice Payments
        api_response = api_instance.list_credit_card_invoice_payments(credit_card_id, credit_card_invoice_id)
        print("The response of CreditCardsApi->list_credit_card_invoice_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->list_credit_card_invoice_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_id** | **int**| Credit Card ID | 
 **credit_card_invoice_id** | **int**| Credit Card Invoice ID | 

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
**200** | List of Credit Card Invoice Payments |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_card_invoices**
> List[CreditCardInvoice] list_credit_card_invoices(credit_card_id)

List Credit Card Invoices

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.credit_card_invoice import CreditCardInvoice
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
    api_instance = organizze_api.CreditCardsApi(api_client)
    credit_card_id = 1 # int | Credit Card ID

    try:
        # List Credit Card Invoices
        api_response = api_instance.list_credit_card_invoices(credit_card_id)
        print("The response of CreditCardsApi->list_credit_card_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->list_credit_card_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_id** | **int**| Credit Card ID | 

### Return type

[**List[CreditCardInvoice]**](CreditCardInvoice.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Credit Card Invoices |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_cards**
> List[CreditCard] list_credit_cards()

List Credit Cards

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.credit_card import CreditCard
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
    api_instance = organizze_api.CreditCardsApi(api_client)

    try:
        # List Credit Cards
        api_response = api_instance.list_credit_cards()
        print("The response of CreditCardsApi->list_credit_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->list_credit_cards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CreditCard]**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Credit Cards |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_credit_card**
> CreditCard read_credit_card(credit_card_id)

Read Credit Card

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.credit_card import CreditCard
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
    api_instance = organizze_api.CreditCardsApi(api_client)
    credit_card_id = 1 # int | Credit Card ID

    try:
        # Read Credit Card
        api_response = api_instance.read_credit_card(credit_card_id)
        print("The response of CreditCardsApi->read_credit_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->read_credit_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_id** | **int**| Credit Card ID | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Card |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_credit_card_invoice**
> CreditCardInvoiceFull read_credit_card_invoice(credit_card_id, credit_card_invoice_id)

Read Credit Card Invoice

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.credit_card_invoice_full import CreditCardInvoiceFull
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
    api_instance = organizze_api.CreditCardsApi(api_client)
    credit_card_id = 1 # int | Credit Card ID
    credit_card_invoice_id = 1 # int | Credit Card Invoice ID

    try:
        # Read Credit Card Invoice
        api_response = api_instance.read_credit_card_invoice(credit_card_id, credit_card_invoice_id)
        print("The response of CreditCardsApi->read_credit_card_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->read_credit_card_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_id** | **int**| Credit Card ID | 
 **credit_card_invoice_id** | **int**| Credit Card Invoice ID | 

### Return type

[**CreditCardInvoiceFull**](CreditCardInvoiceFull.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Card Invoice |  -  |
**404** | Item Not Found |  -  |
**401** | Authentication issues |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_card**
> CreditCard update_credit_card(credit_card_id, credit_card_input)

Update Credit Card

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (userAgent):

```python
import organizze_api
from organizze_api.models.credit_card import CreditCard
from organizze_api.models.credit_card_input import CreditCardInput
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
    api_instance = organizze_api.CreditCardsApi(api_client)
    credit_card_id = 1 # int | Credit Card ID
    credit_card_input = organizze_api.CreditCardInput() # CreditCardInput | 

    try:
        # Update Credit Card
        api_response = api_instance.update_credit_card(credit_card_id, credit_card_input)
        print("The response of CreditCardsApi->update_credit_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditCardsApi->update_credit_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_id** | **int**| Credit Card ID | 
 **credit_card_input** | [**CreditCardInput**](CreditCardInput.md)|  | 

### Return type

[**CreditCard**](CreditCard.md)

### Authorization

[basicAuth](../README.md#basicAuth), [userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credit Card |  -  |
**400** | Bad request (e.g., missing User-Agent header) |  -  |
**401** | Authentication issues |  -  |
**404** | Item Not Found |  -  |
**422** | Validation errors |  -  |
**0** | Authentication issues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

