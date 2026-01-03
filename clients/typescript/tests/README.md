# TypeScript SDK Tests

This directory contains tests for the Organizze API TypeScript SDK using Node's built-in test runner.

## Test Types

- **Unit Tests** (`tests/unit/`): Test SDK instantiation and method availability (no API calls)
- **Integration Tests** (`tests/integration/`): Test real API interactions (require valid credentials)

## Running Tests

### Unit Tests (Default)

```bash
npm test
# or
npm run test:unit
```

Unit tests verify that:
- API classes can be instantiated
- All expected methods exist
- Configuration is properly handled

**No credentials required** - runs immediately.

### Integration Tests

Integration tests make real API calls and require valid Organizze credentials.

1. **Set up credentials:**

   ```bash
   cp .env.example .env
   # Edit .env and add your credentials
   ```

2. **Run integration tests:**

   ```bash
   npm run test:integration
   ```

   Integration tests will **fail** if credentials are not set in `.env`.

### All Tests

Run both unit and integration tests:

```bash
npm run test:all
```

### Watch Mode

Run unit tests in watch mode (re-runs on file changes):

```bash
npm run test:watch
```

## Environment Variables

Create a `.env` file (copy from `.env.example`) with:

- `ORGANIZZE_EMAIL`: Your Organizze account email
- `ORGANIZZE_API_KEY`: Your API token from [Organizze API Settings](https://app.organizze.com.br/configuracoes/api-keys)
- `ORGANIZZE_BASE_URL`: API base URL (default: https://api.organizze.com.br/rest/v2)

## Test Structure

```
tests/
├── setup.ts                           # Test configuration utilities
├── unit/                              # Unit tests (no API calls)
│   ├── bank-accounts.test.ts
│   ├── budgets.test.ts
│   ├── categories.test.ts
│   ├── credit-cards.test.ts
│   ├── transactions.test.ts
│   └── users.test.ts
└── integration/                       # Integration tests (real API calls)
    ├── bank-accounts.test.ts
    ├── budgets.test.ts
    ├── categories.test.ts
    ├── credit-cards.test.ts
    ├── transactions.test.ts
    └── users.test.ts
```

## Writing New Tests

Tests use Node's built-in test runner (`node:test`) and assertions (`node:assert`):

```typescript
import { describe, it } from 'node:test';
import assert from 'node:assert';
import { YourApi, Configuration } from '../index';

describe('YourApi', () => {
  it('should do something', () => {
    // Your test here
    assert.ok(true);
  });
});
```

For integration tests, use the configuration helper from `setup.ts`:

```typescript
import { getTestConfig } from '../setup';

it('should call API', async () => {
  const config = getTestConfig();
  const api = new YourApi(config);

  const result = await api.yourMethod();
  assert.ok(result);
});
```

**Note**: Integration tests automatically fail if credentials are not set. No need for manual skipping.
