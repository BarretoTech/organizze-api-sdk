
# BankAccountInput

Schema for creating or updating a bank account

## Properties

Name | Type
------------ | -------------
`name` | string
`institutionId` | string
`description` | string
`archived` | boolean
`_default` | boolean
`type` | string

## Example

```typescript
import type { BankAccountInput } from ''

// TODO: Update the object below with actual values
const example = {
  "name": null,
  "institutionId": null,
  "description": null,
  "archived": null,
  "_default": null,
  "type": null,
} satisfies BankAccountInput

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BankAccountInput
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


