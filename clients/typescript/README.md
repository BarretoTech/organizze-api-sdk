# Organizze API SDK for TypeScript/JavaScript

Auto-generated TypeScript/JavaScript client library for the [Organizze](https://organizze.com.br) personal finance API.

This SDK provides type-safe access to your Organizze financial data, based on the official API documentation at https://github.com/organizze/api-doc.

## Disclaimer

This package and its owner are not affiliated with Organizze and offer no guarantee with regards to API stability or reliability. For legal information about license and liabilities, please check the [license file](./LICENSE).

## Installation

```bash
# NPM
npm install --save organizze-api-sdk

# Yarn
yarn add organizze-api-sdk

# pNpm
pnpm install organizze-api-sdk
```

## Compatibility

- **Browsers**: Any modern browser capable of supporting ES6
- **Node.js**: >= 18 (due to the usage of the Fetch API)

## Authentication

All Organizze API requests require:

1. **HTTP Basic Authentication**

   - Username: Your Organizze account email
   - Password: API token from [https://app.organizze.com.br/configuracoes/api-keys](https://app.organizze.com.br/configuracoes/api-keys)

2. **User-Agent Header** (REQUIRED)
   - Format: `ApplicationName (email@example.com)`
   - **Important**: Omitting this header will result in `400 Bad Request` errors

## Quick Start

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
console.log(accounts);

// Create a transaction
const transactionsApi = new TransactionsApi(config);
const transaction = await transactionsApi.createTransaction({
  description: "Groceries",
  date: "2025-12-12",
  amount_cents: -5000, // negative for expenses, positive for income
  category_id: 123,
  account_id: 456,
});
console.log(transaction);
```

## Usage Examples

### Listing Bank Accounts

```typescript
import { Configuration, BankAccountsApi } from "organizze-api-sdk";

const config = new Configuration({
  basePath: "https://api.organizze.com.br/rest/v2",
  username: "your.email@example.com",
  password: "your_api_token",
  headers: { "User-Agent": "MyApp (your.email@example.com)" },
});

const api = new BankAccountsApi(config);
const accounts = await api.listBankAccounts();
```

### Reading a Specific Bank Account

```typescript
const accountId = 123;
const account = await api.readBankAccount({ id: accountId });
```

### Managing Transactions

```typescript
import { Configuration, TransactionsApi } from "organizze-api-sdk";

const config = new Configuration({
  basePath: "https://api.organizze.com.br/rest/v2",
  username: "your.email@example.com",
  password: "your_api_token",
  headers: { "User-Agent": "MyApp (your.email@example.com)" },
});

const api = new TransactionsApi(config);

// List all transactions
const transactions = await api.listTransactions();

// Create a new transaction
const newTransaction = await api.createTransaction({
  description: "Salary",
  date: "2025-01-01",
  amount_cents: 500000, // R$ 5,000.00
  category_id: 456,
  account_id: 789,
});

// Read a specific transaction
const transaction = await api.readTransaction({ id: 123 });

// Update a transaction
const updated = await api.updateTransaction({
  id: 123,
  transaction: {
    description: "Updated description",
    amount_cents: -3000,
  },
});

// Delete a transaction
await api.deleteTransaction({ id: 123 });
```

### Working with Categories

```typescript
import { Configuration, CategoriesApi } from "organizze-api-sdk";

const config = new Configuration({
  basePath: "https://api.organizze.com.br/rest/v2",
  username: "your.email@example.com",
  password: "your_api_token",
  headers: { "User-Agent": "MyApp (your.email@example.com)" },
});

const api = new CategoriesApi(config);

// List all categories
const categories = await api.listCategories();

// Read a specific category
const category = await api.readCategory({ id: 123 });
```

### Managing Credit Cards

```typescript
import { Configuration, CreditCardsApi } from "organizze-api-sdk";

const config = new Configuration({
  basePath: "https://api.organizze.com.br/rest/v2",
  username: "your.email@example.com",
  password: "your_api_token",
  headers: { "User-Agent": "MyApp (your.email@example.com)" },
});

const api = new CreditCardsApi(config);

// List all credit cards
const cards = await api.listCreditCards();

// Read a specific credit card
const card = await api.readCreditCard({ id: 123 });

// List invoices for a credit card
const invoices = await api.listCreditCardInvoices({ creditCardId: 123 });

// Read a specific invoice
const invoice = await api.readCreditCardInvoice({
  creditCardId: 123,
  id: 456,
});

// List payments for an invoice
const payments = await api.listCreditCardInvoicePayments({
  creditCardId: 123,
  invoiceId: 456,
});
```

### Accessing User Information

```typescript
import { Configuration, UsersApi } from "organizze-api-sdk";

const config = new Configuration({
  basePath: "https://api.organizze.com.br/rest/v2",
  username: "your.email@example.com",
  password: "your_api_token",
  headers: { "User-Agent": "MyApp (your.email@example.com)" },
});

const api = new UsersApi(config);

// List all users
const users = await api.listUsers();

// Read a specific user
const user = await api.readUser({ id: 123 });
```

## Available APIs and Operations

Quick reference table of all available operations. Click on any API or operation name for detailed documentation.

| API                                          | Operation                                                                               | Description                                |
| -------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------ |
| [BankAccountsApi](./docs/BankAccountsApi.md) | [listBankAccounts](./docs/BankAccountsApi.md#listbankaccounts)                          | List all bank accounts                     |
| [BankAccountsApi](./docs/BankAccountsApi.md) | [readBankAccount](./docs/BankAccountsApi.md#readbankaccount)                            | Get details of a specific bank account     |
| [BudgetsApi](./docs/BudgetsApi.md)           | [listCurrentMonthBudgets](./docs/BudgetsApi.md#listcurrentmonthbudgets)                 | List budgets for the current month         |
| [BudgetsApi](./docs/BudgetsApi.md)           | [listYearMonthBudgets](./docs/BudgetsApi.md#listyearmonthbudgets)                       | List budgets for a specific year and month |
| [CategoriesApi](./docs/CategoriesApi.md)     | [listCategories](./docs/CategoriesApi.md#listcategories)                                | List all transaction categories            |
| [CategoriesApi](./docs/CategoriesApi.md)     | [readCategory](./docs/CategoriesApi.md#readcategory)                                    | Get details of a specific category         |
| [CreditCardsApi](./docs/CreditCardsApi.md)   | [listCreditCards](./docs/CreditCardsApi.md#listcreditcards)                             | List all credit cards                      |
| [CreditCardsApi](./docs/CreditCardsApi.md)   | [readCreditCard](./docs/CreditCardsApi.md#readcreditcard)                               | Get details of a specific credit card      |
| [CreditCardsApi](./docs/CreditCardsApi.md)   | [listCreditCardInvoices](./docs/CreditCardsApi.md#listcreditcardinvoices)               | List invoices for a credit card            |
| [CreditCardsApi](./docs/CreditCardsApi.md)   | [readCreditCardInvoice](./docs/CreditCardsApi.md#readcreditcardinvoice)                 | Get details of a specific invoice          |
| [CreditCardsApi](./docs/CreditCardsApi.md)   | [listCreditCardInvoicePayments](./docs/CreditCardsApi.md#listcreditcardinvoicepayments) | List payments for a credit card invoice    |
| [TransactionsApi](./docs/TransactionsApi.md) | [listTransactions](./docs/TransactionsApi.md#listtransactions)                          | List all transactions                      |
| [TransactionsApi](./docs/TransactionsApi.md) | [createTransaction](./docs/TransactionsApi.md#createtransaction)                        | Create a new transaction                   |
| [TransactionsApi](./docs/TransactionsApi.md) | [readTransaction](./docs/TransactionsApi.md#readtransaction)                            | Get details of a specific transaction      |
| [TransactionsApi](./docs/TransactionsApi.md) | [updateTransaction](./docs/TransactionsApi.md#updatetransaction)                        | Update an existing transaction             |
| [TransactionsApi](./docs/TransactionsApi.md) | [deleteTransaction](./docs/TransactionsApi.md#deletetransaction)                        | Delete a transaction                       |
| [UsersApi](./docs/UsersApi.md)               | [listUsers](./docs/UsersApi.md#listusers)                                               | List all users                             |
| [UsersApi](./docs/UsersApi.md)               | [readUser](./docs/UsersApi.md#readuser)                                                 | Get details of a specific user             |

## Features

This SDK supports the complete Organizze API, including:

- **Bank Accounts** - List and view bank account details
- **Categories** - Manage transaction categories
- **Credit Cards** - Manage credit cards, invoices, and payments
- **Transactions** - Create and manage transactions (single, recurring, and installments)
- **Budgets** - Track and manage monthly/yearly budgets
- **Users** - Access user information

## API Reference Documentation

### API Classes

Detailed documentation for each API class:

- [BankAccountsApi](./docs/BankAccountsApi.md) - Bank account operations
- [BudgetsApi](./docs/BudgetsApi.md) - Budget management operations
- [CategoriesApi](./docs/CategoriesApi.md) - Category management operations
- [CreditCardsApi](./docs/CreditCardsApi.md) - Credit card, invoice, and payment operations
- [TransactionsApi](./docs/TransactionsApi.md) - Transaction management operations
- [UsersApi](./docs/UsersApi.md) - User information operations

### Data Models

Documentation for request/response types and models:

**Core Models:**

- [BankAccount](./docs/BankAccount.md) - Bank account data structure
- [BankAccountInput](./docs/BankAccountInput.md) - Bank account creation/update input
- [Budget](./docs/Budget.md) - Budget data structure
- [Category](./docs/Category.md) - Category data structure
- [CategoryInput](./docs/CategoryInput.md) - Category creation/update input
- [CreditCard](./docs/CreditCard.md) - Credit card data structure
- [CreditCardInput](./docs/CreditCardInput.md) - Credit card creation/update input
- [CreditCardInvoice](./docs/CreditCardInvoice.md) - Credit card invoice data structure
- [CreditCardInvoiceFull](./docs/CreditCardInvoiceFull.md) - Complete invoice data with details
- [Transaction](./docs/Transaction.md) - Transaction data structure
- [TransactionInput](./docs/TransactionInput.md) - Transaction creation/update input
- [User](./docs/User.md) - User data structure

**Transaction Types:**

- [InstallmentTransaction](./docs/InstallmentTransaction.md) - Installment transaction structure
- [InstallmentTransactionAllOfInstallmentsAttributes](./docs/InstallmentTransactionAllOfInstallmentsAttributes.md) - Installment-specific attributes
- [RecurringTransaction](./docs/RecurringTransaction.md) - Recurring transaction structure
- [RecurringTransactionAllOfRecurrenceAttributes](./docs/RecurringTransactionAllOfRecurrenceAttributes.md) - Recurrence-specific attributes

**Request/Response Models:**

- [CreateTransactionRequest](./docs/CreateTransactionRequest.md) - Transaction creation request
- [UpdateTransactionRequest](./docs/UpdateTransactionRequest.md) - Transaction update request
- [DeleteTransactionRequest](./docs/DeleteTransactionRequest.md) - Transaction deletion request

**Additional Models:**

- [Tag](./docs/Tag.md) - Tag data structure
- [TransactionTagsInner](./docs/TransactionTagsInner.md) - Transaction tag structure

**Error Models:**

- [FailedAuthentication](./docs/FailedAuthentication.md) - Authentication failure response
- [NotFound](./docs/NotFound.md) - Resource not found response
- [ValidationError](./docs/ValidationError.md) - Validation error response

## Error Handling

```typescript
import { Configuration, TransactionsApi } from "organizze-api-sdk";

const config = new Configuration({
  basePath: "https://api.organizze.com.br/rest/v2",
  username: "your.email@example.com",
  password: "your_api_token",
  headers: { "User-Agent": "MyApp (your.email@example.com)" },
});

const api = new TransactionsApi(config);

try {
  const transaction = await api.readTransaction({ id: 123 });
  console.log(transaction);
} catch (error) {
  console.error("API Error:", error);
}
```

## Important Notes

1. **User-Agent Header**: Always include a User-Agent header with your application name and contact email. Requests without this header will fail with a 400 error.

2. **Amount Format**: Transaction amounts are in cents (e.g., -5000 = -R$ 50.00). Use negative values for expenses and positive values for income.

3. **Date Format**: Dates should be in `YYYY-MM-DD` format (e.g., "2025-01-15").

4. **Authentication**: Keep your API token secure. Never commit it to version control or expose it in client-side code.

## API Documentation

For more details about the Organizze API, visit:

- Official API Documentation: https://github.com/organizze/api-doc
- Get your API token: https://app.organizze.com.br/configuracoes/api-keys

## Support

This is an auto-generated client library. For issues or contributions, please visit the [main repository](https://github.com/BarretoTech/organizze-api-sdk).

## License

See the [LICENSE](./LICENSE) file for details.
