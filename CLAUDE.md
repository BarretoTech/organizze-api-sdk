# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a monorepo for auto-generated SDK client libraries for the Organizze API (Brazilian personal finance platform). The project generates type-safe Python and TypeScript/JavaScript clients from an OpenAPI specification.

**Key Architecture:**

- Single source of truth: `specs/openapi.yaml` defines the entire API
- Auto-generation: Clients are generated using OpenAPI Generator
- Monorepo structure: Multiple client libraries managed with moon build system
- Toolchain management: proto manages all tools (moon, Node.js, Python, npm, uv)

## Development Toolchain

This project uses [proto](https://moonrepo.dev/proto) for toolchain management and [moon](https://moonrepo.dev) for task orchestration.

### Initial Setup

```bash
# Install proto (if not already installed)
# Follow instructions at https://moonrepo.dev/proto

# Install all required tools (moon, Node.js, Python, npm, uv)
proto use
```

## Common Commands

### Client Generation

**Generate all clients from OpenAPI spec:**

```bash
moon run :generate-client
```

**Generate specific client:**

```bash
# Python client
moon run python-client:generate-client

# TypeScript client
moon run typescript-client:generate-client
```

### Testing

**Python:**

```bash
# All tests (unit + integration)
moon run python-client:test

# Unit tests only
moon run python-client:test -- -m unit

# Integration tests (requires .env with credentials)
moon run python-client:test -- -m integration

# Specific test file
moon run python-client:test -- tests/integration/test_users_api_integration.py -v
```

**TypeScript:**

```bash
# All tests
moon run typescript-client:test
```

### Building

**Python:**

```bash
moon run python-client:build
# Output: clients/python/dist/
```

**TypeScript:**

```bash
moon run typescript-client:build
# Output: clients/typescript/dist/
```

### Publishing

**Bump version and publish (local only):**

```bash
# Python
moon run python-client:bump
moon run python-client:publish

# TypeScript
moon run typescript-client:bump
moon run typescript-client:publish
```

## Code Architecture

### Monorepo Structure

```
.
├── specs/
│   └── openapi.yaml          # Single source of truth for API definition
├── clients/
│   ├── config/               # OpenAPI Generator configurations
│   │   ├── python.json       # Python generator config
│   │   └── typescript.json   # TypeScript generator config
│   ├── python/               # Python SDK (auto-generated + custom tests)
│   │   ├── organizze_api/    # Generated SDK code
│   │   ├── test/             # Auto-generated tests
│   │   └── tests/            # Hand-written integration tests
│   └── typescript/           # TypeScript SDK (auto-generated + custom tests)
│       ├── apis/             # Generated API classes
│       ├── models/           # Generated models
│       └── tests/            # Hand-written tests
└── .moon/
    └── workspace.yml         # Moon build system configuration
```

### Generation Pipeline

1. **Source**: `specs/openapi.yaml` contains the complete API specification
2. **Configuration**: Client-specific configs in `clients/config/{python,typescript}.json`
3. **Generation**: OpenAPI Generator creates client code via moon tasks
4. **Customization**:
   - Generated code should NOT be manually edited (will be overwritten)
   - Custom tests live in separate directories (`tests/` for hand-written, `test/` for generated)
   - Client configuration lives in `pyproject.toml` (Python) and `package.json` (TypeScript)

### Important Files to Modify

**When updating the API:**

- Edit `specs/openapi.yaml` only
- Run regeneration commands
- Update integration tests if endpoints changed

**When updating client metadata (versions, descriptions, etc.):**

- Python: `clients/python/pyproject.toml`
- TypeScript: `clients/typescript/package.json`

**When updating generation configuration:**

- `clients/config/python.json` or `clients/config/typescript.json`
- Be aware: changes may affect all generated code

### Moon Build System

- Projects defined in `.moon/workspace.yml` (points to `clients/*`)
- Each client has its own `moon.yml` with tasks
- Tasks can depend on each other (e.g., `build` depends on `generate-client`)
- Use `:task` to run for all projects, `project:task` for specific projects

### Testing Strategy

**Python:**

- Auto-generated tests in `test/` (don't modify)
- Hand-written integration tests in `tests/integration/`
- Uses pytest with markers: `@pytest.mark.integration` and `@pytest.mark.unit`
- Integration tests require `.env` with `ORGANIZZE_EMAIL` and `ORGANIZZE_API_KEY`

**TypeScript:**

- Unit tests verify SDK structure (no API calls)
- Integration tests make real API calls (require `.env`)
- Uses Node.js built-in test runner (node:test)
- Test setup utilities in `tests/setup.ts`

## Important Implementation Notes

### API Specification Accuracy

The `specs/openapi.yaml` in this repository may differ from the official Organizze API documentation. This specification has been refined based on real-world API testing and should be considered more accurate than the official docs. When making changes, test against the actual API behavior.

### Authentication Requirements

All Organizze API requests require:

1. HTTP Basic Auth (email + API token)
2. User-Agent header (format: "AppName (email@example.com)")

Missing the User-Agent header results in 400 errors. Both clients handle this automatically via configuration.

### Generated Code Guidelines

- **Never manually edit generated files** in `organizze_api/`, `apis/`, or `models/` directories
- To fix issues, update `specs/openapi.yaml` or generator configs, then regenerate
- Generated code is recreated on every generation run
- Custom code belongs in test files or separate utilities

### Type Checking

**Python:**

- Uses mypy for type checking
- Configuration in `pyproject.toml` under `[tool.mypy]`
- Strict typing enabled for `organizze_api.configuration` module
- Run: `moon run python-client:typecheck` (configuration auto-discovered)

**TypeScript:**

- Uses TypeScript compiler for type checking
- Configuration in `tsconfig.json`
- Generates `.d.ts` type definition files
- Build includes type checking automatically

### Version Management

Package versions are managed separately:

- Python: `pyproject.toml` line 3 (`version = "x.y.z"`)
- TypeScript: `package.json` line 3 (`"version": "x.y.z"`)

Use `moon bump` tasks for automated patch version increments.
