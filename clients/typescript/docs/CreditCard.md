
# CreditCard


## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string
`description` | string
`cardNetwork` | string
`closingDay` | number
`dueDay` | number
`limitCents` | number
`archived` | boolean
`_default` | boolean
`institutionId` | string
`institutionName` | string
`createdAt` | Date
`updatedAt` | Date
`type` | string

## Example

```typescript
import type { CreditCard } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "description": null,
  "cardNetwork": null,
  "closingDay": null,
  "dueDay": null,
  "limitCents": null,
  "archived": null,
  "_default": null,
  "institutionId": null,
  "institutionName": null,
  "createdAt": null,
  "updatedAt": null,
  "type": null,
} satisfies CreditCard

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as CreditCard
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


