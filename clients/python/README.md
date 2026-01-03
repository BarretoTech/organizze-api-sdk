# Organizze API - Python SDK

[![PyPI version](https://badge.fury.io/py/organizze-api.svg)](https://pypi.org/project/organizze_api/)
[![Python versions](https://img.shields.io/pypi/pyversions/organizze-api.svg)](https://pypi.org/project/organizze_api/)

Auto-generated Python client library for the [Organizze](https://organizze.com.br) personal finance API.

This SDK provides type-safe access to your Organizze financial data, based on the official API documentation at https://github.com/organizze/api-doc.

## Disclaimer

This package and its owner are not affiliated with Organizze and offer no guarantee with regards to API stability or reliability. For legal information about license and liabilities, please check the [license file](./LICENSE).

## Requirements

- Python 3.9+
- Dependencies: urllib3, python-dateutil, pydantic, typing-extensions

## Installation

### From PyPI (Recommended)

```bash
pip install organizze_api
```

### From Source

```bash
# Clone the repository
git clone https://github.com/BarretoTech/organizze-api-sdk.git
cd organizze-api-sdk/clients/python

# Install
pip install -e .
```

### From Git

```bash
pip install git+https://github.com/BarretoTech/organizze-api-sdk.git#subdirectory=clients/python
```

## Authentication

All Organizze API requests require:

1. **HTTP Basic Authentication**
   - Username: Your Organizze account email
   - Password: API token from [https://app.organizze.com.br/configuracoes/api-keys](https://app.organizze.com.br/configuracoes/api-keys)

2. **User-Agent Header** (REQUIRED)
   - Format: `ApplicationName (email@example.com)`
   - **Important**: Omitting this header will result in `400 Bad Request` errors

## Quick Start

```python
import organizze_api
from organizze_api.rest import ApiException

# Configure authentication
configuration = organizze_api.Configuration(
    host="https://api.organizze.com.br/rest/v2",
    username="your.email@example.com",
    password="your_api_token"
)

# Set required User-Agent header
configuration.api_key['userAgent'] = 'MyApp (your.email@example.com)'

# Use the API
with organizze_api.ApiClient(configuration) as api_client:
    # List bank accounts
    bank_accounts_api = organizze_api.BankAccountsApi(api_client)
    accounts = bank_accounts_api.list_bank_accounts()
    print(accounts)

    # Create a transaction
    transactions_api = organizze_api.TransactionsApi(api_client)
    transaction = organizze_api.Transaction(
        description="Groceries",
        date="2025-01-15",
        amount_cents=-5000,  # negative for expenses, positive for income
        category_id=123,
        account_id=456
    )
    result = transactions_api.create_transaction(transaction)
    print(result)
```

## Usage Examples

### Managing Bank Accounts

```python
import organizze_api

configuration = organizze_api.Configuration(
    host="https://api.organizze.com.br/rest/v2",
    username="your.email@example.com",
    password="your_api_token"
)
configuration.api_key['userAgent'] = 'MyApp (your.email@example.com)'

with organizze_api.ApiClient(configuration) as api_client:
    api = organizze_api.BankAccountsApi(api_client)

    # List all bank accounts
    accounts = api.list_bank_accounts()

    # Read a specific bank account
    account = api.read_bank_account(bank_account_id=123)

    # Create a new bank account
    new_account = organizze_api.BankAccount(
        name="Savings Account",
        description="My savings"
    )
    created = api.create_bank_account(new_account)

    # Update a bank account
    updated = api.update_bank_account(
        bank_account_id=123,
        bank_account=organizze_api.BankAccount(name="Updated Name")
    )

    # Delete a bank account
    api.delete_bank_account(bank_account_id=123)
```

### Working with Transactions

```python
import organizze_api
from datetime import date

configuration = organizze_api.Configuration(
    host="https://api.organizze.com.br/rest/v2",
    username="your.email@example.com",
    password="your_api_token"
)
configuration.api_key['userAgent'] = 'MyApp (your.email@example.com)'

with organizze_api.ApiClient(configuration) as api_client:
    api = organizze_api.TransactionsApi(api_client)

    # List all transactions
    transactions = api.list_transactions()

    # Create a transaction
    transaction = organizze_api.Transaction(
        description="Salary",
        date="2025-01-01",
        amount_cents=500000,  # R$ 5,000.00
        category_id=456,
        account_id=789
    )
    created = api.create_transaction(transaction)

    # Read a specific transaction
    transaction = api.read_transaction(transaction_id=123)

    # Update a transaction
    updated = api.update_transaction(
        transaction_id=123,
        transaction=organizze_api.Transaction(
            description="Updated description",
            amount_cents=-3000
        )
    )

    # Delete a transaction
    api.delete_transaction(transaction_id=123)
```

### Managing Categories

```python
import organizze_api

configuration = organizze_api.Configuration(
    host="https://api.organizze.com.br/rest/v2",
    username="your.email@example.com",
    password="your_api_token"
)
configuration.api_key['userAgent'] = 'MyApp (your.email@example.com)'

with organizze_api.ApiClient(configuration) as api_client:
    api = organizze_api.CategoriesApi(api_client)

    # List all categories
    categories = api.list_categories()

    # Read a specific category
    category = api.read_category(category_id=123)

    # Create a new category
    new_category = organizze_api.Category(
        name="Entertainment",
        color="#FF5733"
    )
    created = api.create_category(new_category)
```

### Working with Credit Cards

```python
import organizze_api

configuration = organizze_api.Configuration(
    host="https://api.organizze.com.br/rest/v2",
    username="your.email@example.com",
    password="your_api_token"
)
configuration.api_key['userAgent'] = 'MyApp (your.email@example.com)'

with organizze_api.ApiClient(configuration) as api_client:
    api = organizze_api.CreditCardsApi(api_client)

    # List all credit cards
    cards = api.list_credit_cards()

    # Read a specific credit card
    card = api.read_credit_card(credit_card_id=123)

    # List invoices for a credit card
    invoices = api.list_credit_card_invoices(credit_card_id=123)

    # Read a specific invoice
    invoice = api.read_credit_card_invoice(
        credit_card_id=123,
        credit_card_invoice_id=456
    )

    # List payments for an invoice
    payments = api.list_credit_card_invoice_payments(
        credit_card_id=123,
        credit_card_invoice_id=456
    )
```

### Managing Budgets

```python
import organizze_api

configuration = organizze_api.Configuration(
    host="https://api.organizze.com.br/rest/v2",
    username="your.email@example.com",
    password="your_api_token"
)
configuration.api_key['userAgent'] = 'MyApp (your.email@example.com)'

with organizze_api.ApiClient(configuration) as api_client:
    api = organizze_api.BudgetsApi(api_client)

    # Get current month budgets
    current_budgets = api.list_current_month_budgets()

    # Get budgets for a specific month
    monthly_budgets = api.list_monthly_budgets(year=2025, month=1)

    # Get annual budgets
    annual_budgets = api.list_annual_budgets(year=2025)
```

### Error Handling

```python
import organizze_api
from organizze_api.rest import ApiException

configuration = organizze_api.Configuration(
    host="https://api.organizze.com.br/rest/v2",
    username="your.email@example.com",
    password="your_api_token"
)
configuration.api_key['userAgent'] = 'MyApp (your.email@example.com)'

with organizze_api.ApiClient(configuration) as api_client:
    api = organizze_api.TransactionsApi(api_client)

    try:
        transaction = api.read_transaction(transaction_id=123)
        print(transaction)
    except ApiException as e:
        print(f"API Error: {e.status} - {e.reason}")
        print(f"Response body: {e.body}")
```

## Features

This SDK supports the complete Organizze API, including:

- **Bank Accounts** - Create, list, update, and delete bank accounts
- **Categories** - Manage transaction categories
- **Credit Cards** - Manage credit cards, invoices, and payments
- **Transactions** - Create and manage transactions (single, recurring, and installments)
- **Budgets** - Track and manage monthly/yearly budgets
- **Users** - Access user information

## Documentation for API Endpoints

All URIs are relative to *https://api.organizze.com.br/rest/v2*

| Class             | Method                                                                                            | HTTP request                                                                 | Description                       |
| ----------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------- |
| _BankAccountsApi_ | [**create_bank_account**](docs/BankAccountsApi.md#create_bank_account)                            | **POST** /accounts                                                           | Create Bank Account               |
| _BankAccountsApi_ | [**delete_bank_account**](docs/BankAccountsApi.md#delete_bank_account)                            | **DELETE** /accounts/{bankAccountID}                                         | Delete Bank Account               |
| _BankAccountsApi_ | [**list_bank_accounts**](docs/BankAccountsApi.md#list_bank_accounts)                              | **GET** /accounts                                                            | List Bank Accounts                |
| _BankAccountsApi_ | [**read_bank_account**](docs/BankAccountsApi.md#read_bank_account)                                | **GET** /accounts/{bankAccountID}                                            | Read Account                      |
| _BankAccountsApi_ | [**update_bank_account**](docs/BankAccountsApi.md#update_bank_account)                            | **PUT** /accounts/{bankAccountID}                                            | Update Bank Account               |
| _BudgetsApi_      | [**list_annual_budgets**](docs/BudgetsApi.md#list_annual_budgets)                                 | **GET** /budgets/{year}                                                      | Get Annual Budgets                |
| _BudgetsApi_      | [**list_current_month_budgets**](docs/BudgetsApi.md#list_current_month_budgets)                   | **GET** /budgets                                                             | Get Current Month Budgets         |
| _BudgetsApi_      | [**list_monthly_budgets**](docs/BudgetsApi.md#list_monthly_budgets)                               | **GET** /budgets/{year}/{month}                                              | Get Monthly Budgets               |
| _CategoriesApi_   | [**create_category**](docs/CategoriesApi.md#create_category)                                      | **POST** /categories                                                         | Create Category                   |
| _CategoriesApi_   | [**delete_category**](docs/CategoriesApi.md#delete_category)                                      | **DELETE** /categories/{categoryID}                                          | Delete Category                   |
| _CategoriesApi_   | [**list_categories**](docs/CategoriesApi.md#list_categories)                                      | **GET** /categories                                                          | List Categories                   |
| _CategoriesApi_   | [**read_category**](docs/CategoriesApi.md#read_category)                                          | **GET** /categories/{categoryID}                                             | Read Category                     |
| _CategoriesApi_   | [**update_category**](docs/CategoriesApi.md#update_category)                                      | **PUT** /categories/{categoryID}                                             | Update Category                   |
| _CreditCardsApi_  | [**create_credit_card**](docs/CreditCardsApi.md#create_credit_card)                               | **POST** /credit_cards                                                       | Create Credit Card                |
| _CreditCardsApi_  | [**delete_credit_card**](docs/CreditCardsApi.md#delete_credit_card)                               | **DELETE** /credit_cards/{creditCardID}                                      | Delete Credit Card                |
| _CreditCardsApi_  | [**list_credit_card_invoice_payments**](docs/CreditCardsApi.md#list_credit_card_invoice_payments) | **GET** /credit_cards/{creditCardID}/invoices/{creditCardInvoiceID}/payments | List Credit Card Invoice Payments |
| _CreditCardsApi_  | [**list_credit_card_invoices**](docs/CreditCardsApi.md#list_credit_card_invoices)                 | **GET** /credit_cards/{creditCardID}/invoices                                | List Credit Card Invoices         |
| _CreditCardsApi_  | [**list_credit_cards**](docs/CreditCardsApi.md#list_credit_cards)                                 | **GET** /credit_cards                                                        | List Credit Cards                 |
| _CreditCardsApi_  | [**read_credit_card**](docs/CreditCardsApi.md#read_credit_card)                                   | **GET** /credit_cards/{creditCardID}                                         | Read Credit Card                  |
| _CreditCardsApi_  | [**read_credit_card_invoice**](docs/CreditCardsApi.md#read_credit_card_invoice)                   | **GET** /credit_cards/{creditCardID}/invoices/{creditCardInvoiceID}          | Read Credit Card Invoice          |
| _CreditCardsApi_  | [**update_credit_card**](docs/CreditCardsApi.md#update_credit_card)                               | **PUT** /credit_cards/{creditCardID}                                         | Update Credit Card                |
| _TransactionsApi_ | [**create_transaction**](docs/TransactionsApi.md#create_transaction)                              | **POST** /transactions                                                       | Create Transaction                |
| _TransactionsApi_ | [**delete_transaction**](docs/TransactionsApi.md#delete_transaction)                              | **DELETE** /transactions/{transactionID}                                     | Delete Transaction                |
| _TransactionsApi_ | [**list_transactions**](docs/TransactionsApi.md#list_transactions)                                | **GET** /transactions                                                        | List Transactions                 |
| _TransactionsApi_ | [**read_transaction**](docs/TransactionsApi.md#read_transaction)                                  | **GET** /transactions/{transactionID}                                        | Read Transaction                  |
| _TransactionsApi_ | [**update_transaction**](docs/TransactionsApi.md#update_transaction)                              | **PUT** /transactions/{transactionID}                                        | Update Transaction                |
| _UsersApi_        | [**list_users**](docs/UsersApi.md#list_users)                                                     | **GET** /users                                                               | List Users                        |
| _UsersApi_        | [**read_user**](docs/UsersApi.md#read_user)                                                       | **GET** /users/{userID}                                                      | Read User                         |

## API Reference Documentation

### API Classes

Detailed documentation for each API class:

- [BankAccountsApi](docs/BankAccountsApi.md) - Bank account operations (create, list, read, update, delete)
- [BudgetsApi](docs/BudgetsApi.md) - Budget management operations (current month, monthly, annual)
- [CategoriesApi](docs/CategoriesApi.md) - Category management operations (create, list, read, update, delete)
- [CreditCardsApi](docs/CreditCardsApi.md) - Credit card, invoice, and payment operations
- [TransactionsApi](docs/TransactionsApi.md) - Transaction management operations (create, list, read, update, delete)
- [UsersApi](docs/UsersApi.md) - User information operations

### Data Models

Documentation for request/response types and models:

**Core Models:**
- [BankAccount](docs/BankAccount.md) - Bank account data structure
- [Budget](docs/Budget.md) - Budget data structure
- [Category](docs/Category.md) - Category data structure
- [CreditCard](docs/CreditCard.md) - Credit card data structure
- [CreditCardInvoice](docs/CreditCardInvoice.md) - Credit card invoice data structure
- [CreditCardInvoiceFull](docs/CreditCardInvoiceFull.md) - Complete invoice data with details
- [Transaction](docs/Transaction.md) - Transaction data structure
- [User](docs/User.md) - User data structure

**Transaction Types:**
- [InstallmentTransaction](docs/InstallmentTransaction.md) - Installment transaction structure
- [InstallmentTransactionAllOfInstallmentsAttributes](docs/InstallmentTransactionAllOfInstallmentsAttributes.md) - Installment-specific attributes
- [RecurringTransaction](docs/RecurringTransaction.md) - Recurring transaction structure
- [RecurringTransactionAllOfRecurrenceAttributes](docs/RecurringTransactionAllOfRecurrenceAttributes.md) - Recurrence-specific attributes

**Request/Response Models:**
- [CreateTransactionRequest](docs/CreateTransactionRequest.md) - Transaction creation request
- [UpdateTransactionRequest](docs/UpdateTransactionRequest.md) - Transaction update request
- [DeleteTransactionRequest](docs/DeleteTransactionRequest.md) - Transaction deletion request

**Error Models:**
- [FailedAuthentication](docs/FailedAuthentication.md) - Authentication failure response
- [NotFound](docs/NotFound.md) - Resource not found response
- [ValidationError](docs/ValidationError.md) - Validation error response

## Important Notes

1. **User-Agent Header**: Always include a User-Agent header with your application name and contact email. Requests without this header will fail with a 400 error.

2. **Amount Format**: Transaction amounts are in cents (e.g., -5000 = -R$ 50.00). Use negative values for expenses and positive values for income.

3. **Date Format**: Dates should be in `YYYY-MM-DD` format (e.g., "2025-01-15").

4. **Authentication**: Keep your API token secure. Never commit it to version control or expose it in publicly accessible code.

5. **Type Safety**: This SDK uses Pydantic for data validation, providing runtime type checking and better IDE support.

## Testing

Execute `pytest` to run the tests:

```bash
pytest
```

## API Documentation

For more details about the Organizze API, visit:
- Official API Documentation: https://github.com/organizze/api-doc
- Get your API token: https://app.organizze.com.br/configuracoes/api-keys

## Support

This is an auto-generated client library. For issues or contributions, please visit the [main repository](https://github.com/BarretoTech/organizze-api-sdk).

## License

See the [LICENSE](./LICENSE) file for details.
