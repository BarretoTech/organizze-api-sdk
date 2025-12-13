# Tag Integration Tests

This document describes the integration tests for Tag functionality in the Organizze API SDK.

## Overview

The tag integration tests verify that the SDK correctly handles tags as objects (with a `name` property) when communicating with the Organizze API. These tests ensure proper serialization and deserialization of tags in API requests and responses.

## Test Coverage

The following tag-specific integration tests are included in `test_transactions_api_integration.py`:

### 1. `test_list_transactions_with_tags`
- **Purpose**: Verify that transactions returned by the API have tags properly deserialized as Tag objects
- **What it tests**:
  - Tags are returned as a list of Tag objects
  - Each tag is a proper Tag instance with a `name` property
  - Tag names are strings
- **Output**: Displays count of transactions with tags and a sample

### 2. `test_create_transaction_with_tags`
- **Purpose**: Test creating a new transaction with tags
- **What it tests**:
  - Tags can be serialized and sent to the API
  - Created transaction returns with tags as Tag objects
  - Multiple tags can be added to a transaction
- **Cleanup**: Automatically deletes the created transaction

### 3. `test_update_transaction_tags`
- **Purpose**: Test updating tags on an existing transaction
- **What it tests**:
  - Tags can be modified through the update endpoint
  - Updated tags are properly returned as Tag objects
- **Cleanup**: Automatically deletes the created transaction

### 4. `test_read_transaction_verifies_tag_objects`
- **Purpose**: Verify that reading a specific transaction returns tags as Tag objects
- **What it tests**:
  - Individual transaction read returns proper Tag objects
  - Tag structure is preserved through read operations

## Running the Tests

### Prerequisites

1. Set up environment variables with your Organizze API credentials:
```bash
export ORGANIZZE_EMAIL="your-email@example.com"
export ORGANIZZE_API_KEY="your-api-key"
export ORGANIZZE_USER_AGENT="YourApp (your-email@example.com)"
```

2. Make sure you have transactions with tags in your Organizze account (for read tests)

### Run All Integration Tests

```bash
cd clients/python
python -m pytest tests/integration/test_transactions_api_integration.py -v
```

### Run Only Tag-Related Tests

```bash
cd clients/python
python -m pytest tests/integration/test_transactions_api_integration.py::TestTransactionsApiIntegration::test_list_transactions_with_tags -v
python -m pytest tests/integration/test_transactions_api_integration.py::TestTransactionsApiIntegration::test_create_transaction_with_tags -v
python -m pytest tests/integration/test_transactions_api_integration.py::TestTransactionsApiIntegration::test_update_transaction_tags -v
python -m pytest tests/integration/test_transactions_api_integration.py::TestTransactionsApiIntegration::test_read_transaction_verifies_tag_objects -v
```

### Run with Verbose Output

```bash
cd clients/python
python -m pytest tests/integration/test_transactions_api_integration.py -v -s
```

The `-s` flag shows print statements, which display useful information about tags found during testing.

## Expected Tag Format

### API Response Format
```json
{
  "id": 2477483422,
  "description": "Despesa fixa",
  "tags": [
    {"name": "expenses"},
    {"name": "recurring"}
  ]
}
```

### SDK Representation
```python
from organizze_api.models.transaction import Transaction
from organizze_api.models.tag import Tag

# Tags are represented as Tag objects
transaction = Transaction.from_dict(api_response)
for tag in transaction.tags:
    print(tag.name)  # Access the name property
```

## Test Data Cleanup

All integration tests that create transactions automatically clean up after themselves by deleting the created transactions, even if the test fails. This ensures your Organizze account doesn't get cluttered with test data.

## Troubleshooting

### "No transactions with tags found"
Some tests require existing transactions with tags. If you see this warning, add some tags to existing transactions in your Organizze account first.

### Authentication Errors
Make sure your `ORGANIZZE_EMAIL` and `ORGANIZZE_API_KEY` environment variables are set correctly. You can generate an API key at: https://app.organizze.com.br/configuracoes/api-keys

### "Missing User-Agent header"
Set the `ORGANIZZE_USER_AGENT` environment variable with the format: `ApplicationName (email@example.com)`

## CI/CD Integration

These tests can be integrated into CI/CD pipelines by setting the environment variables as secrets:

```yaml
# Example GitHub Actions
env:
  ORGANIZZE_EMAIL: ${{ secrets.ORGANIZZE_EMAIL }}
  ORGANIZZE_API_KEY: ${{ secrets.ORGANIZZE_API_KEY }}
  ORGANIZZE_USER_AGENT: "CI/CD Bot (ci@example.com)"
```
