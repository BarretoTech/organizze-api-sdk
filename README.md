# Organizze API SDK

This repository provides auto-generated client libraries for the [Organizze](https://organizze.com.br) API, based on the official documentation at https://github.com/organizze/api-doc.

The intention of this repo is to simplify the life of developers trying to integrate their own personal finance with [Organizze](https://organizze.com.br/).

## Disclaimer

This repo and its owner are not affiliated with Organizze and offer no guarantee with regards to API stability or reliability.
More legal information about license and liabilities, please check the [license file](./LICENSE).

## Available Clients

| Language              | Status | Package                                                | Source                                        |
| --------------------- | ------ | ------------------------------------------------------ | --------------------------------------------- |
| Javascript/Typescript | ✅     | [NPM](https://www.npmjs.com/package/organizze-api-sdk) | [`clients/typescript`](./clients/typescript/) |
| Python                | ✅     | [PyPI](https://pypi.org/project/organizze_api/)        | [`clients/python`](./clients/python/)         |

## Features

All clients support the complete Organizze API, including:

- **Bank Accounts** - List, create, update, and delete bank accounts
- **Categories** - Manage transaction categories
- **Credit Cards** - Manage credit cards and invoices
- **Transactions** - Create and manage transactions (single, recurring, and installments)
- **Budgets** - Track and manage monthly/yearly budgets
- **Users** - Access user information

## Installation & Usage

### TypeScript

#### Installation

```bash
npm install organizze-api-sdk
```

#### Usage

```typescript
import {
  Configuration,
  BankAccountsApi,
  TransactionsApi,
} from "organizze-api-sdk";

// Configure authentication
const config = new Configuration({
  basePath: "https://api.organizze.com.br/rest/v2",
  username: "your.email@example.com",
  password: "your_api_token",
  headers: {
    "User-Agent": "MyApp (your.email@example.com)",
  },
});

// List bank accounts
const bankAccountsApi = new BankAccountsApi(config);
const accounts = await bankAccountsApi.listBankAccounts();

// Create a transaction
const transactionsApi = new TransactionsApi(config);
const transaction = await transactionsApi.createTransaction({
  description: "Groceries",
  date: "2025-12-12",
  amount_cents: -5000,
  category_id: 123,
  account_id: 456,
});
```

### Python

#### Installation

```bash
# From PyPI (recommended)
pip install organizze_api

# Or from source
cd clients/python
pip install -e .

# Or directly from git
pip install git+https://github.com/BarretoTech/organizze-api-sdk.git#subdirectory=clients/python
```

#### Usage

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

    # Create a transaction
    transactions_api = organizze_api.TransactionsApi(api_client)
    transaction = organizze_api.Transaction(
        description="Groceries",
        date="2025-12-12",
        amount_cents=-5000,
        category_id=123,
        account_id=456
    )
    result = transactions_api.create_transaction(transaction)

    # Get current month budgets
    budgets_api = organizze_api.BudgetsApi(api_client)
    budgets = budgets_api.list_current_month_budgets()
```

## API Authentication

All Organizze API requests require:

1. **HTTP Basic Auth**

   - Username: Your Organizze account email
   - Password: API token from [https://app.organizze.com.br/configuracoes/api-keys](https://app.organizze.com.br/configuracoes/api-keys)

2. **User-Agent Header** (Required)
   - Format: `ApplicationName (email@example.com)`
   - Omitting this header returns `400 Bad Request`

## Development

### Regenerating Clients

This project uses [OpenAPI Generator](https://openapi-generator.tech) to generate clients from the OpenAPI specification.

#### Prerequisites

- Node.js 18.14.2 (see `.nvmrc`)
- npm 11.6.2+

#### Generate TypeScript Client

```bash
npx @openapitools/openapi-generator-cli generate \
  -i specs/openapi.yaml \
  -g typescript-fetch \
  -o clients/typescript \
  -c clients/config/typescript.json
```

#### Generate Python Client

```bash
npx @openapitools/openapi-generator-cli generate \
  -i specs/openapi.yaml \
  -g python \
  -o clients/python \
  -c clients/config/python.json
```

### Updating the OpenAPI Specification

The OpenAPI specification is located at [`specs/openapi.yaml`](./specs/openapi.yaml).

To update it:

1. Edit the `specs/openapi.yaml` file
2. Regenerate the clients using the commands above
3. Test the generated clients
4. Submit a pull request

## Contributing

Do you see an endpoint not properly documented? Fork this repo and propose changes through a Pull Request. Contributions are welcome!

### How to Contribute

1. Fork the repository
2. Update the OpenAPI specification in `specs/openapi.yaml`
3. Regenerate the clients
4. Test your changes
5. Submit a pull request with a clear description of the changes

## License

See the [LICENSE](./LICENSE) file for details.
