# Organizze API SDK for Typescript/Javascript

Connect to your personal finance data on [Organizze](https://organizze.com.br).

## Disclaimer

This package and its owner are not affiliated with Organizze and offers no guarantee with regards to API stability or reliability.
More legal information about license and liabilities, please check the [license file](./LICENSE)

## Installation

- For NPM: `npm install --save organizze-api-sdk`
- For Yarn: `yarn add organizze-api-sdk`
- For pNpm: `pnpm install organizze-api-sdk`

## Compatiblity

- Browsers: Any modern browser capable of supporting ES6
- Node.JS: >= 18 due to the usage of the Fetch API

## Quick Start

```typescript
import { UsersApi } from "organizze-api-sdk";
```

## Available APIs and operations

| API             | Operation                     |
| --------------- | ----------------------------- |
| BankAccountsApi | listBankAccounts              |
| BankAccountsApi | readBankAccount               |
| CategoriesApi   | listCategories                |
| CategoriesApi   | readCategory                  |
| UsersApi        | listUsers                     |
| UsersApi        | readUser                      |
| CreditCardsApi  | listCreditCards               |
| CreditCardsApi  | readCreditCard                |
| CreditCardsApi  | listCreditCardInvoices        |
| CreditCardsApi  | readCreditCardInvoice         |
| CreditCardsApi  | listCreditCardInvoicePayments |
| TransactionsApi | listTransactions              |
| TransactionsApi | createTransaction             |
| TransactionsApi | readTransaction               |
| TransactionsApi | updateTransaction             |
| TransactionsApi | deleteTransaction             |
