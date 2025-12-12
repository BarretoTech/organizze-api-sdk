# Integration Tests

This directory contains integration tests for the Organizze API SDK that make real API calls.

## Setup

1. Copy the `.env.example` file to `.env` in the `clients/python` directory:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Organizze credentials:
   ```
   ORGANIZZE_EMAIL=your.email@example.com
   ORGANIZZE_API_KEY=your_api_key_here
   ```

3. Get your API key from [Organizze Settings](https://app.organizze.com.br/configuracoes/api-keys)

## Running Tests

Run all integration tests:
```bash
pytest tests/integration/ -v
```

Run a specific test file:
```bash
pytest tests/integration/test_users_api_integration.py -v
```

Run a specific test:
```bash
pytest tests/integration/test_users_api_integration.py::TestUsersApiIntegration::test_list_users -v
```

Run with detailed output:
```bash
pytest tests/integration/ -v -s
```

## Test Coverage

The integration tests cover:

- **Users API**: List and read users
- **Categories API**: List, read, create, update, delete categories
- **Bank Accounts API**: List, read, create, update, delete bank accounts
- **Transactions API**: List, read, create, update, delete transactions
- **Budgets API**: List current month, monthly, and annual budgets
- **Credit Cards API**: List, read, create, update, delete credit cards and invoices

## Important Notes

- These tests make **real API calls** to your Organizze account
- Some tests create temporary data and clean up afterwards
- Tests that modify data (create/update/delete) will attempt cleanup even if they fail
- Make sure you have the necessary permissions in your Organizze account

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ORGANIZZE_EMAIL` | Yes | Your Organizze account email |
| `ORGANIZZE_API_KEY` | Yes | Your Organizze API key/token |
| `ORGANIZZE_USER_AGENT` | No | Custom User-Agent header (defaults to test identifier) |
