
# BankAccount


## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string
`institutionId` | string
`institutionName` | string
`description` | string
`kind` | string
`archived` | boolean
`createdAt` | Date
`updatedAt` | Date
`_default` | boolean
`type` | string

## Example

```typescript
import type { BankAccount } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "institutionId": null,
  "institutionName": null,
  "description": null,
  "kind": null,
  "archived": null,
  "createdAt": null,
  "updatedAt": null,
  "_default": null,
  "type": null,
} satisfies BankAccount

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BankAccount
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


